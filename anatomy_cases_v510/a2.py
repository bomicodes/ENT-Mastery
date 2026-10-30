"""Anatomy-for-OR-case content, batch a2 (otology skull base, rhinology, thyroid/parathyroid/salivary)."""
CASES = {}

CASES["retrosigmoid-skull-base"] = {
    "title": "Retrosigmoid Skull-Base Approach",
    "region": "Otology / Neurotology",
    "summary": "A suboccipital craniotomy just posterior to the sigmoid sinus and inferior to the transverse sinus opens the cerebellopontine angle (CPA) from behind, giving access to the brainstem, cranial nerves V-XI and the porus of the internal auditory canal (IAC) while leaving the labyrinth intact. Safety depends on locating the transverse-sigmoid junction so that neither sinus is torn, and on knowing that the facial nerve usually lies on the anterior (hidden) face of a vestibular schwannoma, with AICA looping close to the porus.",
    "layers": [
        {"step": "Positioning and soft tissue", "structures": ["skin", "occipitalis / posterior auricular muscle", "SCM, splenius capitis and longissimus capitis insertions", "occipital artery", "lesser occipital nerve", "mastoid emissary vein"],
         "note": "Retroauricular curvilinear or lazy-S incision a few cm behind the postauricular crease. Reflect the muscles as one musculoperiosteal layer for a watertight closure. The occipital artery runs medially in the lower field, deep to splenius capitis. The mastoid emissary vein exits a foramen near the posterior mastoid and drains into the sigmoid; it marks the sinus and should be waxed rather than torn."},
        {"step": "Bone landmarks and craniotomy", "structures": ["asterion", "digastric groove", "mastoid air cells", "transverse sinus (superior edge)", "sigmoid sinus (anterior edge)"],
         "note": "The asterion approximates the transverse-sigmoid junction, though the relationship varies. Place the first burr hole slightly inferior and medial to the asterion. Strip dura off the inner table before using the craniotome. Expose the posterior edge of the sigmoid sinus anteriorly and the inferior edge of the transverse sinus superiorly; together they form the superolateral corner of the window. Wax any opened mastoid cells at once."},
        {"step": "Dural opening and CSF release", "structures": ["posterior fossa dura", "petrosal (anterior) surface of cerebellar hemisphere", "cisterna magna / lateral cerebellomedullary cistern"],
         "note": "Open the dura as a flap based on the sigmoid sinus. Elevate the inferolateral cerebellum gently superomedially to open the lateral cerebellomedullary cistern near the lower cranial nerves and release CSF. The cerebellum then falls away medially, so fixed retraction is minimal."},
        {"step": "CPA survey: lower neurovascular complex", "structures": ["CN IX, X, XI entering the jugular foramen", "PICA", "flocculus", "choroid plexus at the foramen of Luschka"],
         "note": "The lower complex is the most inferior and comes into view first as the cerebellum relaxes. IX is the most rostral fibre bundle at the jugular foramen; X follows as many rootlets just below it. Choroid plexus protruding from the foramen of Luschka sits just posterior to IX/X and points up toward the VII/VIII root entry zone."},
        {"step": "CPA survey: middle and upper complexes", "structures": ["CN VII / VIII complex and AICA", "nervus intermedius", "CN V and superior petrosal vein (Dandy) near the tentorium", "CN VI deep, ascending along the clivus anterior to the VII/VIII complex"],
         "note": "VII leaves the brainstem at the pontomedullary junction, anterior and slightly rostral to VIII. AICA loops around or into the porus. Superiorly, the superior petrosal vein drains into the superior petrosal sinus close to CN V. Preserve it where possible."},
        {"step": "Tumor debulking and arachnoid dissection", "structures": ["tumor capsule", "arachnoid planes", "brainstem surface", "facial nerve (usually anterior / anterosuperior on the capsule)"],
         "note": "Stimulate the posterior capsule to confirm there is no nerve on it, then debulk from inside. Fold the capsule in on itself and develop the arachnoid plane medially at the brainstem, where VII and VIII are found at the root entry zone. Then work laterally toward the porus."},
        {"step": "Drilling the posterior IAC wall", "structures": ["posterior lip of porus acusticus", "IAC dura", "endolymphatic duct / operculum and vestibular aqueduct", "posterior semicircular canal and crus commune (lateral limit)", "jugular bulb (inferior)", "retrofacial / petrous air cells"],
         "note": "Coagulate and incise the dura over the posterior IAC and drill the posterior wall with a diamond burr. The lateral limit is set by the posterior canal and crus commune, which lie lateral and slightly posterior; measure the safe drilling distance on preoperative CT. The operculum of the endolymphatic duct is a useful warning sign. A high jugular bulb can limit inferior drilling."},
        {"step": "IAC contents and lateral dissection", "structures": ["transverse (falciform) crest", "superior and inferior vestibular nerves (posterior)", "facial nerve (anterosuperior)", "cochlear nerve (anteroinferior)", "labyrinthine artery"],
         "note": "The vestibular nerves lie posterior and are seen first. Dissect tumor medial-to-lateral within the canal, or lateral-to-medial once the fundus is visible, so traction does not avulse the cochlear nerve at the modiolus."},
        {"step": "Closure", "structures": ["opened air cells (posterior IAC, mastoid)", "dura", "bone flap / cranioplasty", "musculoperiosteal layer"],
         "note": "Seal all opened air cells with wax, muscle or fat; a missed cell is the usual route for CSF rhinorrhea through the middle ear and Eustachian tube. Close the dura watertight or patch it, replace the bone or perform cranioplasty, and close the muscle in layers."}
    ],
    "landmarks": [
        {"structure": "Transverse-sigmoid junction", "how_to_find": "The asterion (meeting point of the lambdoid, parietomastoid and occipitomastoid sutures) usually overlies or lies close to the junction, but the relationship varies between patients, so treat it as an approximation. A line from the zygomatic root to the inion approximates the transverse sinus. Follow the mastoid emissary vein anteriorly to the sigmoid. Confirm on CT or MRV.", "why": "Defines the superolateral corner of the craniotomy and prevents a sinus tear"},
        {"structure": "Facial nerve root exit zone", "how_to_find": "At the pontomedullary junction, anterior to and slightly above the VIII root entry. Look just rostral to the flocculus and the choroid plexus tuft from the foramen of Luschka. Confirm with low-current stimulation before dissecting.", "why": "The proximal nerve is the most constant place to identify VII when tumor has distorted it"},
        {"structure": "Facial nerve on the tumor capsule", "how_to_find": "Expect it on the anterior, often anterosuperior, capsule surface, splayed thin. Map the posterior capsule with the stimulator before every incision.", "why": "VII is hidden behind the tumor in this view"},
        {"structure": "Lower cranial nerves (IX-XI)", "how_to_find": "Inferior part of the field, entering the jugular foramen. IX is the most superior and is separated from X by a dural septum; XI rises from below with spinal rootlets.", "why": "Keep cottonoids and retraction above them to avoid dysphagia and aspiration"},
        {"structure": "Posterior IAC wall and lateral drilling limit", "how_to_find": "Porus on the posterior petrous face above the jugular foramen. Drill laterally only as far as the CT-measured distance to the posterior canal and crus commune. Stop if the endolymphatic duct operculum or blue-lined canal appears.", "why": "Hearing preservation requires an intact labyrinth"},
        {"structure": "Superior petrosal vein (Dandy)", "how_to_find": "Upper CPA near the tentorium and CN V, draining into the superior petrosal sinus", "why": "Avulsion causes brisk bleeding; sacrifice carries a small venous infarct risk"},
        {"structure": "AICA loop", "how_to_find": "Middle complex, often looping around VII/VIII at or into the porus. It gives off the labyrinthine artery.", "why": "Must be dissected off the capsule rather than coagulated"}
    ],
    "danger": [
        {"structure": "Sigmoid and transverse sinuses", "where": "Anterior and superior edges of the craniotomy, immediately deep to the bone", "protect": "Burr hole inferomedial to the asterion, strip dura from the inner table before cutting, and drill over the sinus with a diamond burr. If a tear occurs, use head-up positioning, irrigation and hemostatic packing.", "injury": "Hemorrhage, venous air embolism, and sinus thrombosis or venous infarction, especially if the sinus is dominant"},
        {"structure": "AICA and labyrinthine artery", "where": "Looping on VII/VIII at the porus; the labyrinthine artery enters the IAC", "protect": "Sharp arachnoid dissection off the capsule, no coagulation of loops near the porus, and papaverine for vasospasm", "injury": "Hearing loss from cochlear ischemia; AICA infarct of the lateral pons and middle cerebellar peduncle"},
        {"structure": "Facial nerve", "where": "Anterior or anterosuperior capsule surface, and anterosuperior at the fundus", "protect": "Map with the stimulator, debulk before dissecting the capsule, dissect in small segments along the nerve axis, and accept residual tumor if the nerve is inseparable", "injury": "Facial paralysis"},
        {"structure": "CN IX-XI", "where": "Inferior CPA at the jugular foramen, just below the tumor's inferior pole", "protect": "Arachnoid dissection, cottonoid protection, minimal bipolar near the nerves, and monitoring of X if used", "injury": "Dysphagia, aspiration, hoarseness, shoulder weakness"},
        {"structure": "Labyrinth (posterior canal, crus commune, vestibule)", "where": "Lateral to the posterior IAC wall", "protect": "CT-guided drilling limit and diamond burr; stop at the operculum or vestibular aqueduct", "injury": "Sensorineural hearing loss"},
        {"structure": "Cerebellum and brainstem", "where": "Medial; retracted to open the CPA", "protect": "Release CSF first, use minimal fixed retraction, and preserve petrosal and brainstem veins where possible", "injury": "Cerebellar edema or hematoma, ataxia, brainstem injury"}
    ],
    "variants": [
        "Dominant (usually right) transverse/sigmoid sinus, or hypoplastic contralateral sinus, which raises the stakes of sinus injury",
        "High-riding jugular bulb reaching the IAC floor, which limits inferior drilling of the posterior IAC wall",
        "AICA loop extending into the IAC, which is adherent to tumor and at risk",
        "Large mastoid emissary vein or anteriorly placed sigmoid sinus",
        "Pneumatized posterior IAC lip and retrofacial cells, which increase CSF leak risk"
    ],
    "imaging_check": [
        "MRI: tumor size, CPA versus intracanalicular extent, and fundal CSF cap on T2 (a cap suggests the fundus is clear)",
        "Brainstem compression, fourth-ventricle effacement and hydrocephalus",
        "CT temporal bone: distance from porus to posterior canal and crus commune, vestibular aqueduct position, and pneumatization of the posterior IAC lip",
        "Jugular bulb height relative to the IAC floor",
        "Sinus dominance and patency on MRV or CT venography"
    ],
    "blood_nerve": [
        ["CPA arteries", "SCA (upper complex, CN V), AICA (middle complex, VII/VIII, labyrinthine artery usually from AICA), PICA (lower complex, IX-XI)"],
        ["Venous drainage", "Superior petrosal vein to superior petrosal sinus; transverse to sigmoid sinus to jugular bulb; mastoid emissary vein to sigmoid"],
        ["Scalp and muscle", "Occipital and posterior auricular arteries; lesser and greater occipital nerves (incisional headache and numbness)"],
        ["IAC nerves", "VII anterosuperior, cochlear anteroinferior, superior and inferior vestibular posterior"]
    ],
    "pimp": [
        {"q": "Which sutures meet at the asterion?", "a": "Lambdoid, parietomastoid and occipitomastoid sutures"},
        {"q": "Which artery usually gives off the labyrinthine (internal auditory) artery?", "a": "AICA"},
        {"q": "Arrange the nerves in the lateral IAC.", "a": "Facial anterosuperior, cochlear anteroinferior, superior vestibular posterosuperior, inferior vestibular posteroinferior (seven-up, Coke down)"},
        {"q": "What separates the superior and inferior compartments, and the facial from the superior vestibular nerve, at the fundus?", "a": "Transverse (falciform) crest horizontally; Bill's bar (vertical crest) separates VII from the SVN"},
        {"q": "In which direction does a vestibular schwannoma most often displace the facial nerve?", "a": "Anteriorly, most often anterosuperiorly"},
        {"q": "What does choroid plexus at the foramen of Luschka help you find?", "a": "The VII/VIII root entry zone just above it, and IX/X just anterior to it"},
        {"q": "Name the three neurovascular complexes of the CPA.", "a": "Upper: SCA with CN III, IV, V. Middle: AICA with CN VI, VII, VIII. Lower: PICA with CN IX, X, XI, XII (Rhoton)"},
        {"q": "Main advantages of retrosigmoid over translabyrinthine?", "a": "Hearing can be preserved and the CPA and brainstem are widely seen. Downsides are limited view of the lateral fundus, cerebellar retraction and more postoperative headache"},
        {"q": "Through which route does a CSF leak after retrosigmoid surgery usually present as rhinorrhea?", "a": "Opened posterior IAC or mastoid air cells, then the middle ear, then the Eustachian tube"}
    ],
    "atlas_topics": ["Retrosigmoid / CPA Approach Corridor", "IAC / CPA / Labyrinth Relationships", "Jugular Foramen / Hypoglossal Canal / Lower Cranial Nerves"],
    "sources": [
        ["Brackmann, Shelton, Arriaga. Otologic Surgery, 4e: Retrosigmoid approach to the CPA", ""],
        ["Cummings Otolaryngology 7e: Vestibular schwannoma and CPA surgery chapters", ""],
        ["Rhoton AL. The cerebellopontine angle and posterior fossa cranial nerves by the retrosigmoid approach. Neurosurgery 2000;47(3 Suppl)", ""],
        ["Pasha & Golub, Otolaryngology-Head and Neck Surgery: Clinical Reference Guide 6e: Otology / skull base", ""]
    ]
}

CASES["translabyrinthine-skull-base"] = {
    "title": "Translabyrinthine Skull-Base Approach",
    "region": "Otology / Neurotology",
    "summary": "The translabyrinthine approach removes the mastoid and the entire bony labyrinth to reach the internal auditory canal (IAC) and cerebellopontine angle from lateral, with almost no cerebellar retraction. Hearing on that side is lost. The facial nerve can be identified at the fundus, lateral to the tumor. Safety depends on keeping the fallopian canal intact as the labyrinth is drilled around the second genu and mastoid segment, and on respecting the sigmoid sinus and jugular bulb that frame the corridor.",
    "layers": [
        {"step": "Incision and flap", "structures": ["postauricular skin", "temporalis fascia", "musculoperiosteal (Palva-type) flap", "spine of Henle", "mastoid cortex"],
         "note": "Use a wide C-shaped postauricular incision placed further posterior than for a routine mastoid so the sigmoid sinus and posterior fossa dura can be exposed. Keep a vascularized musculoperiosteal flap for closure."},
        {"step": "Complete mastoidectomy", "structures": ["tegmen mastoideum (superior)", "sigmoid sinus (posterior)", "sinodural angle (Citelli)", "posterior bony EAC wall (anterior, thinned but intact)", "antrum and lateral semicircular canal", "short process of incus", "digastric ridge"],
         "note": "Saucerize widely. Thin the bone over the middle fossa dura and the sigmoid. Identify the lateral canal in the antrum floor and the incus in the fossa incudis; together they give the depth and orientation of the facial nerve."},
        {"step": "Decompress sigmoid sinus and posterior fossa dura", "structures": ["sigmoid sinus", "superior petrosal sinus (along the upper petrous ridge)", "presigmoid posterior fossa dura", "endolymphatic sac (inferior to Donaldson's line)", "Trautmann triangle"],
         "note": "Remove bone a few mm behind the sigmoid; a thin island of bone (Bill's island) may be left on the sinus. Skeletonize the presigmoid dura medially toward the IAC. The superior petrosal sinus runs along the junction of the middle and posterior fossa dura and marks the upper edge of the corridor."},
        {"step": "Skeletonize the mastoid facial nerve", "structures": ["second genu (below and posterior to the lateral canal)", "mastoid segment of the facial nerve", "digastric ridge pointing to the stylomastoid foramen", "facial recess and retrofacial air cells"],
         "note": "Leave a thin shell of fallopian canal bone; do not uncover the sheath. The nerve runs anterior and lateral to the posterior canal, so the mastoid segment forms the anterior wall of the labyrinthectomy."},
        {"step": "Labyrinthectomy", "structures": ["lateral SCC", "posterior SCC (its ampulla lies inferior, near the mastoid facial nerve)", "superior SCC and subarcuate artery (center of the arc)", "crus commune", "ampullae of the lateral and superior canals (anterior, near the tympanic and labyrinthine facial segments)"],
         "note": "Open the lateral canal first and follow it posteriorly to the posterior canal, then the crus commune and superior canal. Leave the anterior lateral-canal ampulla bone for last; it lies just above the tympanic facial segment and second genu."},
        {"step": "Vestibule", "structures": ["vestibule (medial to the oval window, deep to the lateral canal ampulla)", "saccular (spherical) and utricular (elliptical) recesses", "medial wall of vestibule (backs onto the IAC fundus)"],
         "note": "Opening the vestibule shows how deep the IAC is: its medial wall is the lateral end of the canal. Stay posterior to the second genu and below the labyrinthine facial segment."},
        {"step": "Skeletonize the IAC", "structures": ["superior trough (between IAC and middle fossa dura)", "inferior trough (between IAC and jugular bulb)", "cochlear aqueduct (inferior limit)", "IAC dura (porus to fundus, about 270 degrees)", "transverse crest and Bill's bar at the fundus"],
         "note": "Drill the troughs above and below with a diamond burr until the IAC is a blue-lined cylinder. Work medial to lateral toward the fundus, where the bone is densest and the labyrinthine facial nerve lies anterosuperior. The cochlear aqueduct marks the safe inferior limit; CN IX lies just medial and inferior to it."},
        {"step": "Dural opening and tumor removal", "structures": ["superior vestibular nerve (posterior to Bill's bar)", "facial nerve (anterosuperior at the fundus; anterior on the tumor medially)", "cochlear nerve", "AICA", "brainstem", "lower cranial nerves"],
         "note": "Find the facial nerve at the fundus by reflecting the superior vestibular nerve inferiorly and posteriorly off Bill's bar. Debulk and then dissect the capsule off VII medially, in small segments with stimulation."},
        {"step": "Closure", "structures": ["incus and tensor tympani region", "aditus / Eustachian tube orifice", "abdominal fat graft", "musculoperiosteal flap"],
         "note": "Remove the incus and pack the aditus and Eustachian tube (muscle or fascia, sometimes bone wax). Fill the defect with abdominal fat and close in layers to prevent CSF otorhinorrhea."}
    ],
    "landmarks": [
        {"structure": "Lateral semicircular canal", "how_to_find": "Dense, smooth, yellow-white bone in the antrum floor, medial to the short process of the incus", "why": "Sets the depth and plane of the facial nerve and the start of the labyrinthectomy"},
        {"structure": "Mastoid facial nerve / second genu", "how_to_find": "Below and slightly anterior to the lateral canal, medial to the short process of the incus. It descends along a line from the inferior lateral canal to the anterior end of the digastric ridge.", "why": "Forms the anterior boundary of the labyrinthectomy and the IAC exposure"},
        {"structure": "Endolymphatic sac", "how_to_find": "Thickened dura between the sigmoid and the posterior canal, inferior to Donaldson's line (the plane of the lateral canal extended posteriorly through the posterior canal)", "why": "Confirms the presigmoid dura and the posterior canal position"},
        {"structure": "Subarcuate artery", "how_to_find": "Runs through the center of the superior canal arc in the petromastoid canal toward the posterior fossa dura", "why": "Bleeds when drilled; marks the arc of the superior canal"},
        {"structure": "IAC", "how_to_find": "Deep to the vestibule, running roughly parallel to the EAC in the axial plane. Define it by drilling troughs above (toward the middle fossa dura) and below (toward the jugular bulb), then thin the bone to blue.", "why": "Must be skeletonized before the dura is opened"},
        {"structure": "Bill's bar", "how_to_find": "Vertical crest at the superior fundus. The facial nerve is anterior to it and the superior vestibular nerve posterior.", "why": "The most reliable place to identify VII before tumor dissection"},
        {"structure": "Cochlear aqueduct", "how_to_find": "Small channel inferior to the IAC that opens medially near the jugular foramen and may release CSF when opened", "why": "Marks the inferior limit of drilling; CN IX lies just below"}
    ],
    "danger": [
        {"structure": "Facial nerve (mastoid segment, second genu, labyrinthine segment)", "where": "Anterior wall of the labyrinthectomy, and anterosuperior at the fundus within the narrow labyrinthine canal", "protect": "Leave fallopian canal bone, use a large diamond burr with copious irrigation parallel to the nerve, and identify at Bill's bar before tumor dissection", "injury": "Facial paralysis; heat injury causes delayed palsy"},
        {"structure": "Sigmoid sinus and jugular bulb", "where": "Posterior and inferior to the corridor; a high bulb can reach the IAC floor", "protect": "Skeletonize with diamond, leave Bill's island or eggshell bone, and press down a high bulb with bone wax or Surgicel", "injury": "Hemorrhage, air embolism, and loss of inferior exposure"},
        {"structure": "Superior petrosal sinus and middle fossa dura", "where": "Along the upper petrous ridge and the sinodural angle", "protect": "Gentle decompression and bipolar or packing for bleeding", "injury": "Venous bleeding, temporal lobe retraction injury"},
        {"structure": "Petrous ICA", "where": "Anteromedial to the cochlea; not exposed in the standard corridor, only in transotic or transcochlear extensions", "protect": "Stay posterior to the cochlea and do not drill anterior to the fundus without intent", "injury": "Catastrophic hemorrhage, stroke"},
        {"structure": "AICA, brainstem and lower cranial nerves", "where": "Medial CPA; IX-XI inferior near the jugular foramen and cochlear aqueduct", "protect": "Sharp arachnoid dissection, keep the inferior drilling above the cochlear aqueduct, and low bipolar settings", "injury": "Brainstem infarct, dysphagia, aspiration, hoarseness"},
        {"structure": "CSF pathway via the middle ear", "where": "Aditus, Eustachian tube, perilabyrinthine and petrous apex cells", "protect": "Remove the incus, pack the aditus and Eustachian tube, wax cells, and place a fat graft", "injury": "CSF otorhinorrhea, meningitis"}
    ],
    "variants": [
        "Anteriorly placed (forward) sigmoid sinus or contracted sclerotic mastoid, which narrows the presigmoid corridor",
        "High or dehiscent jugular bulb approaching the IAC",
        "Low-lying middle fossa dura / tegmen",
        "Anomalous or dehiscent facial nerve course",
        "Large mastoid emissary vein or prominent subarcuate artery"
    ],
    "imaging_check": [
        "MRI: tumor size, brainstem compression, and fundal involvement",
        "CT: sigmoid sinus position, jugular bulb height relative to the IAC, and tegmen height (the corridor is limited by these)",
        "Mastoid pneumatization and petrous apex cells (CSF leak risk)",
        "Contralateral ear status and audiogram, because ipsilateral hearing is sacrificed",
        "Facial canal course and dehiscence"
    ],
    "blood_nerve": [
        ["Arterial", "Labyrinthine artery (usually from AICA) to the inner ear; subarcuate artery; AICA in the CPA; stylomastoid artery to the mastoid facial nerve"],
        ["Venous", "Sigmoid sinus, superior petrosal sinus, jugular bulb, mastoid emissary vein"],
        ["Neural (IAC)", "VII anterosuperior, cochlear anteroinferior, SVN and IVN posterior; nervus intermedius between VII and VIII"],
        ["Facial nerve segments", "Meatal, labyrinthine (narrowest), geniculate, tympanic, second genu, mastoid"]
    ],
    "pimp": [
        {"q": "Define Donaldson's line and why it matters.", "a": "The plane of the lateral canal extended posteriorly, bisecting the posterior canal. The endolymphatic sac lies inferior to it."},
        {"q": "What are the boundaries of Trautmann triangle?", "a": "Sigmoid sinus (posterior), superior petrosal sinus / middle fossa dura (superior) and the bony labyrinth / posterior canal (anterior)"},
        {"q": "What forms the crus commune?", "a": "The non-ampullated ends of the superior and posterior canals"},
        {"q": "Which canal ampullae lie closest to the tympanic and labyrinthine facial nerve?", "a": "The lateral and superior canal ampullae, anteriorly"},
        {"q": "Narrowest segment of the fallopian canal?", "a": "Labyrinthine segment, at the meatal foramen"},
        {"q": "How do you identify the facial nerve at the fundus?", "a": "Bill's bar: VII lies anterior to it; reflect the superior vestibular nerve posteriorly and inferiorly"},
        {"q": "What is the inferior limit of drilling, and what lies just beyond it?", "a": "The cochlear aqueduct; CN IX at the jugular foramen"},
        {"q": "Why remove the incus and pack the Eustachian tube?", "a": "To block CSF from the middle ear reaching the nasopharynx"},
        {"q": "What runs through the arc of the superior canal?", "a": "The subarcuate artery in the petromastoid canal"}
    ],
    "atlas_topics": ["Translabyrinthine Approach Corridor", "IAC / CPA / Labyrinth Relationships", "Facial Nerve — Intratemporal Course"],
    "sources": [
        ["Brackmann, Shelton, Arriaga. Otologic Surgery, 4e: Translabyrinthine approach", ""],
        ["Cummings Otolaryngology 7e: Surgery of the cerebellopontine angle / vestibular schwannoma", ""],
        ["Myers EN. Operative Otolaryngology, 2e: Translabyrinthine approach", ""],
        ["K.J. Lee's Essential Otolaryngology 12e: Temporal bone anatomy", ""]
    ]
}

CASES["jugular-foramen-tumor"] = {
    "title": "Jugular Foramen Tumor Approach",
    "region": "Otology / Neurotology",
    "summary": "Jugular foramen tumors (paraganglioma, schwannoma, meningioma) grow from the jugular bulb and lower cranial nerve compartment. That compartment sits between the facial nerve laterally, the vertical petrous ICA anteriorly, the labyrinth superiorly and the neck below. Safe removal needs proximal and distal control of the IJV, sigmoid sinus and ICA from the neck and mastoid. CN IX-XI run on the medial wall of the jugular bulb, so preserving that wall is how nerve function is kept.",
    "layers": [
        {"step": "Cervical exposure", "structures": ["SCM", "posterior belly of digastric", "IJV", "ICA and ECA", "CN X, XI, XII", "occipital artery", "transverse process of C1"],
         "note": "Use a postauricular incision extended into the neck. Identify the IJV, ICA and CN X-XII below the tumor first. XI crosses the IJV at about the C1 transverse process. XII loops forward beneath the occipital artery. The ascending pharyngeal artery, the main tumor feeder, arises medially from the proximal ECA."},
        {"step": "Mastoidectomy and facial nerve", "structures": ["mastoid facial nerve", "stylomastoid foramen", "digastric ridge", "sigmoid sinus", "facial recess and retrofacial cells"],
         "note": "Perform a complete mastoidectomy, then skeletonize the mastoid facial segment to the stylomastoid foramen. Depending on the approach, leave the nerve in a fallopian bridge (infralabyrinthine / transjugular), or reroute it anteriorly (Fisch infratemporal type A) to expose the jugular bulb and vertical ICA."},
        {"step": "Infralabyrinthine / retrofacial corridor", "structures": ["posterior SCC (superior limit)", "jugular bulb dome", "retrofacial and infralabyrinthine air cells", "cochlear aqueduct"],
         "note": "Drill between the mastoid facial nerve (anterior), posterior canal (superior) and sigmoid / jugular bulb (posterior-inferior). Keep the otic capsule intact when hearing is to be preserved."},
        {"step": "Venous control", "structures": ["sigmoid sinus (proximal)", "IJV (distal)", "condylar emissary vein"],
         "note": "Occlude the sigmoid extraluminally (packing between bone and dura, or ligation) above the tumor. Ligate the IJV in the neck. The bulb still bleeds from the inferior petrosal sinus and condylar veins after this."},
        {"step": "Jugular bulb and medial wall", "structures": ["lateral wall of jugular bulb", "inferior petrosal sinus openings (medial wall)", "CN IX, X, XI (deep to the medial wall)", "Jacobson's nerve / inferior tympanic canaliculus"],
         "note": "Open the lateral wall and remove intraluminal tumor. Control inferior petrosal sinus bleeding with Surgicel packing rather than suction. Leave the medial venous wall when the nerves function, because IX-XI run just deep to it."},
        {"step": "Petrous ICA", "structures": ["caroticojugular spine", "vertical petrous ICA", "carotid canal periosteum", "horizontal petrous ICA (Fisch C3-C4 extension)"],
         "note": "The vertical ICA lies anterior to the jugular bulb and is separated from it by the caroticojugular spine. Follow it from the neck upward into the carotid canal. Dissect tumor in a subperiosteal or subadventitial plane only with proximal control in hand."},
        {"step": "Intradural / posterior fossa extension", "structures": ["posterior fossa dura", "lower cranial nerve rootlets", "PICA", "vertebral artery (inferomedial)", "hypoglossal canal"],
         "note": "Intradural tumor is approached through the presigmoid / retrosigmoid dura. The hypoglossal canal lies inferomedial to the jugular foramen above the occipital condyle."},
        {"step": "Reconstruction", "structures": ["Eustachian tube", "EAC (blind-sac closure in a type A approach)", "abdominal fat", "temporalis / SCM rotation flaps"],
         "note": "Obliterate the Eustachian tube and air cells, close the dura watertight, and fill dead space with fat and vascularized muscle."}
    ],
    "landmarks": [
        {"structure": "IJV and CN XI in the upper neck", "how_to_find": "Palpate the C1 transverse process between the mastoid tip and the mandibular angle. XI crosses the IJV here, usually superficial (lateral / anterior) to it (about 80% in cadaveric series), deep (medial / posterior) to it in about 20%, and rarely through a split vein.", "why": "Distal venous control and nerve preservation start here"},
        {"structure": "Cervical ICA", "how_to_find": "Posteromedial to the ECA and medial to the IJV, deep to the posterior belly of digastric and the styloid. Follow it superiorly; it has no branches in the neck.", "why": "Proximal arterial control before the tumor is mobilized"},
        {"structure": "CN X, XII, IX in the neck", "how_to_find": "X lies in the carotid sheath between and posterior to the ICA and IJV. XII emerges between them, passes lateral to the ICA and ECA and loops under the occipital artery. IX passes forward between ICA and ECA deep to the styloid with stylopharyngeus.", "why": "Tracing nerves from the neck upward identifies them before they enter the tumor"},
        {"structure": "Facial nerve at the stylomastoid foramen", "how_to_find": "At the anterior end of the digastric ridge, medial to the tympanomastoid suture", "why": "Must be skeletonized or rerouted before working at the bulb"},
        {"structure": "Jugular bulb", "how_to_find": "Inferior to the posterior canal and medial to the mastoid facial nerve, reached through retrofacial / infralabyrinthine cells. It is continuous with the sigmoid above.", "why": "Center of the tumor in glomus jugulare"},
        {"structure": "Caroticojugular spine", "how_to_find": "Bony crest between the jugular fossa and carotid canal on the skull-base undersurface. The inferior tympanic canaliculus (Jacobson's nerve) is on it.", "why": "Separates the jugular bulb from the vertical ICA; erosion indicates carotid involvement"}
    ],
    "danger": [
        {"structure": "Internal carotid artery", "where": "Vertical petrous segment directly anterior to the jugular bulb across the caroticojugular spine; the cervical ICA medial to the IJV", "protect": "Preoperative angiography, embolization and balloon test occlusion when encasement is expected. Proximal cervical control before tumor work, and a subperiosteal or subadventitial plane.", "injury": "Exsanguinating hemorrhage, stroke"},
        {"structure": "Jugular bulb, inferior petrosal sinus and condylar veins", "where": "Medial bulb wall openings, between IX and X", "protect": "Proximal sigmoid occlusion and distal IJV ligation, then Surgicel packing of the IPS openings. Avoid blind suction or deep packing that compresses the nerves.", "injury": "Brisk venous bleeding, air embolism, nerve compression from overpacking"},
        {"structure": "CN IX-XI (and XII via the hypoglossal canal)", "where": "Deep to the medial wall of the jugular bulb (Rhoton's intrajugular, or neural, compartment); XII separately, inferomedial in the hypoglossal canal", "protect": "Preserve the medial venous wall when nerves function, monitor X and XII, and leave adherent tumor when needed", "injury": "Dysphagia, aspiration, vocal fold paralysis, shoulder drop, tongue weakness. Acute combined deficits are poorly compensated, especially in elderly patients."},
        {"structure": "Facial nerve", "where": "Mastoid segment and stylomastoid foramen, lateral to the bulb", "protect": "Fallopian bridge where possible. If rerouting, handle with its soft-tissue cuff at the stylomastoid foramen.", "injury": "Weakness, frequently temporary after anterior rerouting; permanent paralysis if injured"},
        {"structure": "Vertebral artery", "where": "Posteroinferior, near the C1 transverse foramen and occipital condyle in far-lateral extensions", "protect": "Identify it in the suboccipital triangle before condylar drilling", "injury": "Hemorrhage, posterior circulation stroke"},
        {"structure": "Dura / CSF", "where": "Posterior fossa dura medial to the sigmoid and bulb; intradural tumor", "protect": "Watertight closure, Eustachian tube obliteration, and fat plus vascularized flap", "injury": "CSF leak, meningitis"}
    ],
    "variants": [
        "Dominant ipsilateral sigmoid sinus or hypoplastic/absent contralateral transverse sinus, which makes sigmoid sacrifice dangerous",
        "High or dehiscent jugular bulb",
        "CN XI passing medial (deep) to the IJV",
        "Large condylar emissary vein, or inferior petrosal sinus draining by multiple channels",
        "Multicentric paragangliomas (carotid body, vagal, contralateral), particularly in SDHx mutation carriers"
    ],
    "imaging_check": [
        "CT temporal bone: erosion of the caroticojugular spine, carotid canal, otic capsule, facial canal, hypoglossal canal and jugular foramen margins",
        "MRI: intradural extension, relation to the brainstem, and salt-and-pepper flow voids",
        "Angiography: feeders (ascending pharyngeal and others), ICA involvement, balloon test occlusion and embolization",
        "Venous phase: contralateral sinus patency and venous drainage pattern",
        "Screen for multicentric or bilateral tumors. Clinically, check catecholamines and baseline CN IX-XII and hearing."
    ],
    "blood_nerve": [
        ["Tumor supply (paraganglioma)", "Ascending pharyngeal artery (inferior tympanic branch) chiefly; also stylomastoid (posterior auricular/occipital), caroticotympanic (ICA), and middle meningeal branches"],
        ["Venous", "Sigmoid sinus and inferior petrosal sinus to the jugular bulb to the IJV; condylar emissary veins"],
        ["Jugular foramen nerves", "IX with Jacobson's nerve; X with Arnold's nerve; XI. XII is separate in the hypoglossal canal."],
        ["Sympathetics", "Superior cervical ganglion posteromedial to the ICA at C2 (Horner if injured)"]
    ],
    "pimp": [
        {"q": "Classic compartments of the jugular foramen and their contents?", "a": "Classic two-part scheme: pars nervosa (anteromedial) with IX, Jacobson's nerve and the inferior petrosal sinus; pars vascularis (posterolateral) with X, XI, Arnold's nerve and the jugular bulb. Rhoton's three-part scheme: petrosal (IPS), sigmoid (bulb) and intrajugular (IX, X, XI) compartments."},
        {"q": "Main arterial supply of a glomus jugulare?", "a": "Ascending pharyngeal artery (inferior tympanic branch)"},
        {"q": "Where do Jacobson's and Arnold's nerves travel?", "a": "Jacobson's (IX tympanic branch) in the inferior tympanic canaliculus. Arnold's (X auricular branch) in the mastoid canaliculus."},
        {"q": "Name the syndromes: IX-XI; IX-XII; IX-XII plus sympathetics.", "a": "Vernet; Collet-Sicard; Villaret"},
        {"q": "Key maneuver and cost of the Fisch infratemporal type A approach?", "a": "Anterior rerouting of the facial nerve; cost is conductive hearing loss (blind-sac EAC closure) and risk of facial weakness"},
        {"q": "Why does the bulb keep bleeding after sigmoid and IJV ligation?", "a": "Inflow from the inferior petrosal sinus and condylar veins on the medial wall"},
        {"q": "What does Fisch class C imply?", "a": "Erosion of the carotid canal, graded C1-C4 by extent along the ICA"},
        {"q": "Order of XII and the occipital artery in the neck?", "a": "XII hooks around beneath the occipital artery (its SCM branch) and then passes forward lateral to ICA and ECA"}
    ],
    "atlas_topics": ["Jugular Foramen / Infratemporal Approach Corridor", "Jugular Foramen / Hypoglossal Canal / Lower Cranial Nerves", "Vagus / Sympathetic Chain / Carotid Space"],
    "sources": [
        ["Brackmann, Shelton, Arriaga. Otologic Surgery, 4e: Glomus tumors / jugular foramen surgery", ""],
        ["Cummings Otolaryngology 7e: Tumors of the jugular foramen / temporal bone paragangliomas", ""],
        ["Fisch U, Mattox D. Microsurgery of the Skull Base (infratemporal fossa approaches)", ""],
        ["Rhoton AL. Jugular foramen. Neurosurgery 2000;47(3 Suppl)", ""]
    ]
}

CASES["endoscopic-sinus-surgery"] = {
    "title": "Endoscopic Sinus Surgery / Ethmoidectomy",
    "region": "Rhinology / Skull Base",
    "summary": "Ethmoidectomy opens a stack of cells that sits between two thin walls: the lamina papyracea laterally and the ethmoid roof / lateral lamella of the cribriform plate superiorly and medially. Safe dissection keeps the orbit identified laterally at all times, enters the posterior ethmoid low and medial through the basal lamella, and uses the skull base as a known superior boundary. The skull base generally slopes downward from anterior to posterior (and from lateral to medial toward the cribriform plate), so it is identified first posteriorly, where the roof is lower and the bone thicker, and then followed forward; the slope varies between patients and sides and is measured on sagittal CT. The anterior ethmoid artery and any Onodi cell, with the optic nerve and carotid next to it, are checked on CT before surgery.",
    "layers": [
        {"step": "Middle meatus entry", "structures": ["middle turbinate (medial limit)", "uncinate process", "ethmoid infundibulum", "natural maxillary ostium"],
         "note": "Medialize the middle turbinate gently, without fracturing its skull-base attachment. Uncinectomy and maxillary antrostomy reveal the orbital floor and the medial orbital wall, which give a lateral reference at a known height."},
        {"step": "Ethmoid bulla", "structures": ["ethmoid bulla (second lamella)", "lamina papyracea (lateral)", "suprabullar and retrobullar recesses (sinus lateralis)", "anterior ethmoid artery (in or behind the suprabullar recess)"],
         "note": "Enter the bulla medially and inferiorly. Take down its lateral wall to show the lamina, which runs in roughly the same sagittal plane as the medial maxillary wall. If the bulla lamella does not reach the skull base, a suprabullar recess lies above it. The AEA usually crosses the roof in this region, just behind the bulla lamella / in the roof of the suprabullar recess, at the posterior limit of the frontal recess; its exact position is confirmed on CT."},
        {"step": "Basal lamella", "structures": ["basal (ground) lamella of the middle turbinate (third lamella)", "vertical (coronal) and horizontal (axial) portions"],
         "note": "The basal lamella separates the anterior ethmoid from the posterior ethmoid. Penetrate its vertical portion inferiorly and medially, just above the horizontal part and lateral to the turbinate, to stay far from the skull base and orbit. Preserve the horizontal portion so the middle turbinate stays stable."},
        {"step": "Posterior ethmoid", "structures": ["posterior ethmoid cells (drain into the superior meatus)", "superior turbinate", "posterior ethmoid artery", "skull base (lower here)"],
         "note": "The posterior ethmoid cells are fewer, larger and lower in height. Identify the skull base posteriorly, where the bone is thicker, and follow it forward. The posterior ethmoid artery crosses the roof just anterior to the anterior sphenoid wall."},
        {"step": "Sphenoid face and Onodi check", "structures": ["anterior wall of sphenoid", "Onodi (sphenoethmoidal) cell", "optic nerve", "ICA"],
         "note": "The last posterior ethmoid cell borders the sphenoid face. A cell extending superolateral to the sphenoid is an Onodi cell, and its lateral wall may carry the optic nerve and occasionally the ICA. Enter the sphenoid medially and inferiorly."},
        {"step": "Skull base skeletonization, posterior to anterior", "structures": ["fovea ethmoidalis", "lateral lamella of cribriform plate (medial, thinnest)", "anterior ethmoid artery (in a canal or in a mesentery below the roof)", "frontal recess (anterior limit)"],
         "note": "Remove partitions along the roof working posterior to anterior with through-cutting instruments, never by pulling cells down. Do not dissect medially along the middle turbinate attachment where the lateral lamella is thinnest."},
        {"step": "Final inspection", "structures": ["lamina papyracea", "skull base", "middle turbinate", "AEA and PEA"],
         "note": "Inspect for exposed orbital fat, CSF and bleeding from ethmoid arteries. Confirm the middle turbinate is stable and not lateralized."}
    ],
    "landmarks": [
        {"structure": "Lamina papyracea", "how_to_find": "Follow the medial orbital wall up from the orbital floor seen through the maxillary antrostomy; it lies in the plane of the medial maxillary wall. Ballotting the globe shows movement if the lamina is dehiscent.", "why": "The lateral boundary that must stay in view throughout the case"},
        {"structure": "Basal lamella entry point", "how_to_find": "Directly behind the bulla, inferomedially, just above the horizontal portion and lateral to the turbinate vertical attachment", "why": "Safe entry into the posterior ethmoid"},
        {"structure": "Skull base", "how_to_find": "Identify it first in the posterior ethmoid or sphenoid (thicker bone, lower height), or at the planum through a sphenoidotomy, then follow it anteriorly", "why": "A known superior limit so you do not chase disease upward blindly"},
        {"structure": "Anterior ethmoid artery", "how_to_find": "Coronal CT shows the anterior ethmoid foramen as a notch (beak) in the medial orbital wall between the superior oblique and medial rectus. Endoscopically it usually crosses the roof at the posterior limit of the frontal recess, just behind the skull-base attachment of the bulla lamella or in the roof of the suprabullar recess (position varies; check CT). It may hang in a mesentery below the roof.", "why": "Transection with retraction into the orbit causes retrobulbar hematoma"},
        {"structure": "Sphenoid ostium (transnasal check)", "how_to_find": "Medial to the superior turbinate in the sphenoethmoidal recess, classically about 1-1.5 cm above the choanal arch (cadaveric series report up to about 2-3 cm, so use the superior turbinate and the midline as the main guides)", "why": "Confirms the sphenoid before the transethmoid opening, so the posterior ethmoid is not mistaken for the sphenoid"},
        {"structure": "Middle turbinate vertical attachment", "how_to_find": "Medial boundary of dissection, attached to the lateral lamella and cribriform plate", "why": "Twisting or medial dissection here risks CSF leak"}
    ],
    "danger": [
        {"structure": "Lamina papyracea, orbital fat and medial rectus", "where": "Lateral wall of the ethmoid; the medial rectus sits close behind the periorbita at mid-height", "protect": "Keep the lamina identified, angle instruments medially, turn off the microdebrider near the lamina, and stop when fat appears", "injury": "Orbital hematoma, diplopia from medial rectus injury, enophthalmos"},
        {"structure": "Lateral lamella of cribriform plate / skull base", "where": "Superomedial, at the middle turbinate attachment; the thinnest bone, longest in Keros type III", "protect": "Measure Keros depth and asymmetry on coronal CT, dissect posterior to anterior along the roof, and use no medial-pulling strokes", "injury": "CSF leak, meningitis, intracranial injury"},
        {"structure": "Anterior and posterior ethmoid arteries", "where": "Crossing the ethmoid roof from orbit to olfactory fossa; the AEA is at the back of the frontal recess", "protect": "Locate on CT, avoid avulsion, and use bipolar if cut. Avoid monopolar near the orbit.", "injury": "Retrobulbar hematoma (urgent lateral canthotomy and cantholysis), intracranial bleeding. Do not embolize: these are ICA-system (ophthalmic) branches."},
        {"structure": "Optic nerve", "where": "Lateral wall of the posterior ethmoid / Onodi cell and the superolateral sphenoid", "protect": "Identify the Onodi cell on CT and use no powered or blind lateral work at the apex", "injury": "Blindness"},
        {"structure": "Internal carotid artery", "where": "Lateral sphenoid wall, and occasionally the lateral wall of an Onodi cell", "protect": "Enter the sphenoid medially and inferiorly, and do not twist septations that insert on the carotid prominence", "injury": "Catastrophic hemorrhage, stroke, pseudoaneurysm"},
        {"structure": "Middle turbinate", "where": "Medial; the basal lamella horizontal portion anchors it", "protect": "Preserve the horizontal basal lamella and the axilla and avoid mucosal stripping", "injury": "Lateralization, synechiae, frontal recess obstruction"}
    ],
    "variants": [
        "Onodi (sphenoethmoidal) cell with the optic nerve and sometimes the ICA in its wall",
        "Keros type III or asymmetric skull-base heights between sides",
        "Haller (infraorbital ethmoid) cell narrowing the infundibulum",
        "Concha bullosa or paradoxical middle turbinate",
        "Dehiscent lamina papyracea, or AEA running in a mesentery below the roof"
    ],
    "imaging_check": [
        "Keros classification and right-left asymmetry of the olfactory fossa",
        "Lamina papyracea dehiscence or prior fracture",
        "AEA position (notch in the medial orbital wall; canal versus mesentery)",
        "Onodi cell, and optic or carotid dehiscence in the sphenoid",
        "Uncinate attachment, maxillary sinus height (orbital floor level) and basal lamella position"
    ],
    "blood_nerve": [
        ["Arterial", "AEA and PEA (ophthalmic, from the ICA) supply the ethmoid roof and upper septum; SPA (maxillary, from the ECA) supplies the lateral wall and turbinates"],
        ["Venous", "Ethmoid veins to the ophthalmic veins to the cavernous sinus (route of intracranial and orbital spread)"],
        ["Sensory", "Anterior ethmoidal nerve (V1, nasociliary); posterior lateral nasal nerves (V2 via the pterygopalatine ganglion)"],
        ["Special sense", "Olfactory epithelium at the cribriform plate, superior septum and superior turbinate"]
    ],
    "pimp": [
        {"q": "Give the Keros types.", "a": "Olfactory fossa depth: I is 1-3 mm, II is 4-7 mm, III is 8-16 mm"},
        {"q": "Name the ethmoid lamellae in order.", "a": "1 uncinate, 2 bulla, 3 basal lamella of the middle turbinate, 4 superior turbinate (5 supreme turbinate if present)"},
        {"q": "Where do the anterior and posterior ethmoid cells drain?", "a": "Anterior into the middle meatus; posterior into the superior meatus (sphenoethmoidal recess region)"},
        {"q": "What is an Onodi cell?", "a": "A posterior ethmoid cell pneumatizing superolateral to the sphenoid sinus. The optic nerve, and sometimes the ICA, are at risk."},
        {"q": "What is the classic orbital-wall distance rule for the ethmoid arteries?", "a": "About 24-12-6 mm along the medial orbital wall: anterior lacrimal crest to AEA foramen, AEA to PEA, PEA to optic canal. These are averages; individual distances vary by several mm (PEA to optic canal is often reported as about 4-7 mm), so never rely on them in place of CT."},
        {"q": "Thinnest part of the anterior skull base?", "a": "Lateral lamella of the cribriform plate"},
        {"q": "AEA origin, and why not embolize it?", "a": "Ophthalmic artery from the ICA; embolization risks blindness and stroke"},
        {"q": "What is the sinus lateralis?", "a": "The suprabullar and retrobullar recess space, bounded by the bulla, basal lamella, lamina and skull base"},
        {"q": "What is the first step for retrobulbar hematoma?", "a": "Lateral canthotomy with inferior cantholysis, plus medical decompression and ophthalmology"}
    ],
    "atlas_topics": ["Sinonasal Lateral Wall / Ostiomeatal Complex", "Ethmoid Skull Base / Lateral Lamella / AEA", "Orbit — Compartments / Canthi / Lacrimal System"],
    "sources": [
        ["Cummings Otolaryngology 7e: Primary and revision endoscopic sinus surgery; sinonasal anatomy", ""],
        ["Stammberger H. Functional Endoscopic Sinus Surgery: The Messerklinger Technique", ""],
        ["Wormald PJ. Endoscopic Sinus Surgery: Anatomy, Three-Dimensional Reconstruction, and Surgical Technique", ""],
        ["Keros P. Uber die praktische Bedeutung der Niveauunterschiede der Lamina cribrosa des Ethmoids. 1962", ""]
    ]
}

CASES["septoplasty"] = {
    "title": "Septoplasty",
    "region": "Rhinology / Skull Base",
    "summary": "Septoplasty corrects an obstructing septum by working in the avascular subperichondrial and subperiosteal planes. It removes or straightens deviated quadrangular cartilage, perpendicular plate, vomer and maxillary crest while preserving a dorsal and caudal L-strut that holds up the nasal dorsum and tip. Safety rests on keeping at least one mucoperichondrial flap intact at each point, protecting the keystone area, and never twisting the perpendicular plate where it joins the cribriform plate.",
    "layers": [
        {"step": "Infiltration and incision", "structures": ["septal mucosa", "caudal septum", "membranous septum / columella", "medial crural footplates"],
         "note": "Hemitransfixion incision at the caudal septal margin gives access to the caudal septum and nasal spine. A Killian incision 1-1.5 cm behind the caudal edge preserves the caudal attachments but leaves caudal deflections unreachable."},
        {"step": "Subperichondrial flap", "structures": ["mucoperichondrium", "quadrangular cartilage (blue-gray)"],
         "note": "Cut through the perichondrium until the bluish cartilage is seen, then elevate with a Cottle elevator in a bloodless, white, glistening plane. Bleeding and pink tissue mean you are too superficial."},
        {"step": "Inferior tunnels and maxillary crest", "structures": ["maxillary crest and premaxilla", "decussating fibres at the chondro-premaxillary junction", "periosteum of the nasal floor", "incisive canal / nasopalatine nerve (anterior floor)"],
         "note": "Perichondrium and periosteum are not continuous at the crest, so tears are common here. Raise a separate inferior subperiosteal tunnel from the nasal floor and join it to the superior tunnel by sharp division of the fibres."},
        {"step": "Bony-cartilaginous junction and contralateral side", "structures": ["chondro-ethmoidal junction (posterosuperior)", "chondro-vomerine junction (posteroinferior, common spur site)", "contralateral mucoperichondrium / mucoperiosteum"],
         "note": "Disarticulate the cartilage from the bone posteriorly and cross to the opposite side there. Elevate the contralateral subperiosteal flap over the bone."},
        {"step": "Bony septum", "structures": ["perpendicular plate of ethmoid (superior / posterior)", "vomer (inferior / posterior)", "sphenoid rostrum", "cribriform plate (superior attachment of the perpendicular plate)"],
         "note": "Remove deviated bone with through-cutting forceps. Do not rock or twist the perpendicular plate, because force is transmitted to the cribriform plate."},
        {"step": "Cartilage resection and L-strut", "structures": ["dorsal strut", "caudal strut", "keystone area (septum, upper lateral cartilages and nasal bones junction)", "anterior nasal spine"],
         "note": "Resect or score only the obstructing segment and keep a dorsal and caudal strut of at least about 1-1.5 cm. A caudal deflection may need repositioning and suturing to the nasal spine periosteum."},
        {"step": "Closure", "structures": ["hemitransfixion incision", "mucoperichondrial flaps", "quilting sutures", "splints"],
         "note": "Close the incision and quilt the flaps together to remove dead space. Repair any tears so that tears on the two sides do not lie opposite each other."}
    ],
    "landmarks": [
        {"structure": "Subperichondrial plane", "how_to_find": "Score the cartilage until it shows blue-gray and elevate under the shiny perichondrium; the correct plane is nearly bloodless", "why": "Wrong-plane elevation causes bleeding, flap thinning and perforation"},
        {"structure": "Bony-cartilaginous junction", "how_to_find": "Feel the change in resistance as the Freer passes from cartilage to bone posteriorly; disarticulate along this line", "why": "Safe place to cross to the opposite side and reach deviated bone"},
        {"structure": "Maxillary crest", "how_to_find": "Along the nasal floor at the base of the septum; reach it from an inferior tunnel elevated off the nasal floor", "why": "Spurs and crest deviation cause floor obstruction, and the decussating fibres here tear flaps"},
        {"structure": "Keystone area", "how_to_find": "Junction under the rhinion where the dorsal septum meets the nasal bones and upper lateral cartilages; palpate the dorsum externally", "why": "Resection or disruption here causes saddle nose"},
        {"structure": "Anterior nasal spine", "how_to_find": "Palpable at the base of the columella in the hemitransfixion incision; the caudal septum sits on or beside it", "why": "Anchor point for repositioning a dislocated caudal septum"}
    ],
    "danger": [
        {"structure": "Opposing mucoperichondrial flaps", "where": "Both sides of the septum; most at risk over spurs and the maxillary crest", "protect": "Stay strictly subperichondrial, use separate inferior tunnels, and repair tears so they are not opposite each other", "injury": "Septal perforation"},
        {"structure": "Dorsal and caudal L-strut / keystone", "where": "Dorsal septum beneath the nasal bones and the caudal septum above the nasal spine", "protect": "Preserve at least about 1-1.5 cm of strut, avoid resection at the keystone, and do not twist the perpendicular plate", "injury": "Saddle nose, tip ptosis, columellar retraction"},
        {"structure": "Cribriform plate / skull base", "where": "Superior attachment of the perpendicular plate", "protect": "Through-cutting instruments and no rocking or twisting of high posterior bone", "injury": "CSF rhinorrhea, anosmia"},
        {"structure": "Nasopalatine nerve and vessels", "where": "Incisive canal at the anterior nasal floor and premaxilla", "protect": "Avoid aggressive dissection and resection at the premaxilla", "injury": "Numbness of the upper incisors and anterior palate, bleeding"},
        {"structure": "Septal blood supply (Kiesselbach area, posterior septal artery)", "where": "Anterior septum (Little's area) and posterior septum near the sphenoid face", "protect": "Stay in the subperichondrial plane, quilt or splint, and control bleeding before closure", "injury": "Septal hematoma leading to cartilage necrosis or abscess, and epistaxis"}
    ],
    "variants": [
        "Caudal septal dislocation off the anterior nasal spine",
        "Spur at the chondro-vomerine junction along the maxillary crest",
        "Contralateral concha bullosa or compensatory inferior turbinate hypertrophy",
        "Pneumatized septum or sphenoid rostrum extension",
        "Prior septal surgery with scarred or absent cartilage (flaps adhere and tear easily)"
    ],
    "imaging_check": [
        "Not routinely imaged. Clinically check anterior rhinoscopy and nasal endoscopy for the site of deviation (caudal, high dorsal, posterior bony, spur).",
        "Cottle or modified Cottle maneuver and valve assessment to separate septal from valve obstruction",
        "External nasal support: dorsum, tip projection and caudal septal position",
        "Existing perforation or prior surgery",
        "CT only if there is concurrent sinus disease or planned sinus surgery"
    ],
    "blood_nerve": [
        ["Arterial (Kiesselbach plexus)", "Anterior ethmoid (ICA), sphenopalatine posterior septal branch (ECA), greater palatine via the incisive canal, superior labial septal branch (facial)"],
        ["Posterior", "Posterior septal artery crossing the sphenoid face below the ostium (pedicle of the nasoseptal flap)"],
        ["Sensory", "Nasopalatine nerve (V2) posteroinferiorly; anterior ethmoidal nerve (V1) anterosuperiorly"],
        ["Framework", "Quadrangular cartilage, perpendicular plate of ethmoid, vomer, maxillary and palatine crests, premaxilla"]
    ],
    "pimp": [
        {"q": "Which arteries form Kiesselbach plexus?", "a": "Anterior ethmoid, sphenopalatine (septal branch), greater palatine and superior labial arteries"},
        {"q": "Name the components of the nasal septum.", "a": "Quadrangular cartilage, perpendicular plate of ethmoid, vomer, maxillary and palatine crests; membranous septum anteriorly"},
        {"q": "Why do flaps tear at the maxillary crest?", "a": "Perichondrium and periosteum are not continuous there (decussating fibres), so separate inferior tunnels are needed"},
        {"q": "Minimum L-strut width?", "a": "At least about 1 cm dorsally and caudally; many surgeons leave 1.5 cm"},
        {"q": "What is the keystone area?", "a": "The junction of the dorsal septum, nasal bones and upper lateral cartilages; disruption causes saddle deformity"},
        {"q": "Normal internal nasal valve angle?", "a": "About 10-15 degrees, between the septum and the caudal edge of the upper lateral cartilage"},
        {"q": "Why is septal hematoma urgent?", "a": "The cartilage depends on perichondrial diffusion; hematoma causes necrosis, abscess and saddle nose"},
        {"q": "What passes through the incisive canal?", "a": "Nasopalatine nerve and the terminal greater palatine / sphenopalatine (nasopalatine) vessels"}
    ],
    "atlas_topics": ["Nasal Support / Valve Anatomy", "Sinonasal Lateral Wall / Ostiomeatal Complex"],
    "sources": [
        ["Cummings Otolaryngology 7e: Nasal septal surgery chapter", ""],
        ["Bailey's Head and Neck Surgery-Otolaryngology 5e: Septoplasty and nasal obstruction", ""],
        ["Pasha & Golub, Clinical Reference Guide 6e: Rhinology / nasal anatomy", ""]
    ]
}

CASES["maxillary-antrostomy"] = {
    "title": "Endoscopic Maxillary Antrostomy",
    "region": "Rhinology / Skull Base",
    "summary": "A maxillary antrostomy widens the natural ostium. The ostium sits in the floor of the ethmoid infundibulum, hidden behind the uncinate process, and mucociliary clearance runs toward it. The operation fails if an accessory ostium is enlarged instead, and is unsafe if dissection strays anteriorly into the nasolacrimal duct or laterally and superiorly into the orbit.",
    "layers": [
        {"step": "Middle meatus survey", "structures": ["middle turbinate", "uncinate process", "maxillary line", "ethmoid bulla", "hiatus semilunaris"],
         "note": "The maxillary line is the curved ridge on the lateral wall from the middle turbinate axilla toward the inferior turbinate. It marks the frontal process of the maxilla and the nasolacrimal duct; the uncinate attaches just behind it."},
        {"step": "Uncinectomy", "structures": ["uncinate process (free posterior edge)", "ethmoid infundibulum", "lamina papyracea (lateral, behind the uncinate)", "lacrimal bone (anterior)"],
         "note": "Incise or back-bite the uncinate and remove its horizontal (inferior) part. Keep instruments parallel to the lamina rather than pointing laterally, particularly when the uncinate is lateralized against it."},
        {"step": "Find the natural ostium", "structures": ["natural maxillary ostium", "floor of the infundibulum", "posterior fontanelle (common site of accessory ostia)"],
         "note": "Use a 30-45 degree scope. The ostium is an oblique opening in the floor of the infundibulum at about the level of the lower edge of the middle turbinate. Slide a ball probe inferolaterally behind the uncinate to find it."},
        {"step": "Enlarge posteriorly and inferiorly", "structures": ["posterior fontanelle", "inferior turbinate attachment (inferior limit)", "palatine bone / posterior wall of maxillary sinus", "posterior lateral nasal artery (SPA branch)"],
         "note": "Widen through the soft fontanelle tissue posteriorly and inferiorly. Join any accessory ostium to the natural ostium. Excessive posterior extension reaches SPA branches."},
        {"step": "Respect anterior and superior limits", "structures": ["nasolacrimal duct (anterior, hard bone)", "orbital floor (superior)", "infraorbital nerve canal (sinus roof)"],
         "note": "Stop anteriorly when the bone becomes hard (the frontal process and lacrimal canal). The orbital floor forms the roof of the antrostomy."},
        {"step": "Inspect the sinus", "structures": ["maxillary sinus walls", "infraorbital nerve", "alveolar recess", "zygomatic recess"],
         "note": "Use angled endoscopes. Treat only disease that needs removal and preserve healthy mucosa."}
    ],
    "landmarks": [
        {"structure": "Natural maxillary ostium", "how_to_find": "Remove the inferior uncinate, then look into the infundibulum floor with an angled scope at about the level of the lower middle-turbinate edge. A curved ball probe slid inferolaterally behind the uncinate drops into it. It lies anterior to any posterior fontanelle accessory ostium.", "why": "The antrostomy must include it or recirculation persists"},
        {"structure": "Nasolacrimal duct", "how_to_find": "Under the maxillary line, anterior to the uncinate attachment, in hard bone a few mm in front of the natural ostium. It opens under the inferior turbinate (Hasner valve).", "why": "Anterior limit of the antrostomy"},
        {"structure": "Orbital floor and lamina papyracea", "how_to_find": "Superior edge of the antrostomy; with an angled scope the orbital floor is seen as the sinus roof, and it continues into the lamina above", "why": "Superior and lateral limits; it also guides the ethmoid dissection that follows"},
        {"structure": "Posterior fontanelle", "how_to_find": "Membranous area behind the natural ostium, above the inferior turbinate attachment. Accessory ostia here look round and posteriorly placed.", "why": "Must be connected to the natural ostium, not mistaken for it"},
        {"structure": "Infraorbital nerve", "how_to_find": "Ridge in the sinus roof running anteriorly; it may hang on a septation or be dehiscent", "why": "Angled instruments in the sinus can injure it"}
    ],
    "danger": [
        {"structure": "Orbit (lamina papyracea and orbital floor)", "where": "Lateral to the uncinate and superior to the antrostomy. Most at risk in a hypoplastic sinus or atelectatic uncinate apposed to the lamina.", "protect": "Swing the back-biter medially, do not push laterally through the infundibulum, and review CT for a lateralized uncinate", "injury": "Orbital fat exposure, hematoma, medial rectus injury, diplopia"},
        {"structure": "Nasolacrimal duct", "where": "Anterior to the natural ostium under the maxillary line", "protect": "Stop at hard bone anteriorly and use a back-biter only on thin bone", "injury": "Epiphora, dacryocystitis"},
        {"structure": "Accessory ostium / recirculation", "where": "Posterior fontanelle accessory ostium separate from the natural ostium", "protect": "Identify the natural ostium and join both openings into one", "injury": "Persistent sinusitis from mucus circulating out of one opening and back into the other"},
        {"structure": "Posterior lateral nasal artery (SPA branch)", "where": "Posterior and inferior limits of the antrostomy near the palatine bone", "protect": "Limit the posterior extent and use bipolar if a branch bleeds", "injury": "Intraoperative or delayed epistaxis"},
        {"structure": "Infraorbital nerve", "where": "Sinus roof, possibly dehiscent", "protect": "Gentle work with angled instruments in the roof", "injury": "Cheek and upper lip numbness"}
    ],
    "variants": [
        "Haller (infraorbital ethmoid) cell narrowing the infundibulum from above",
        "Hypoplastic maxillary sinus / silent sinus with a lateralized uncinate against the lamina",
        "Accessory ostia in the fontanelles (common)",
        "Pneumatized uncinate, or uncinate attaching to the lamina, skull base or middle turbinate",
        "Dehiscent infraorbital canal or nerve suspended on a septation"
    ],
    "imaging_check": [
        "Uncinate position (lateralized or atelectatic) and the infundibulum width",
        "Maxillary sinus size, hypoplasia and orbital floor height",
        "Haller cells and lamina dehiscence",
        "Infraorbital canal position and septations",
        "Odontogenic source (periapical lucency, oroantral fistula) that needs dental management"
    ],
    "blood_nerve": [
        ["Arterial", "Posterior lateral nasal branches of the SPA; infraorbital and alveolar branches of the maxillary artery to the sinus"],
        ["Sensory", "V2: infraorbital nerve and superior alveolar nerves (posterior, middle, anterior) in the sinus walls"],
        ["Drainage", "Mucociliary flow is directed to the natural ostium, then through the infundibulum and hiatus semilunaris to the middle meatus"]
    ],
    "pimp": [
        {"q": "Boundaries of the ethmoid infundibulum?", "a": "Medially the uncinate, laterally the lamina papyracea / frontal process of the maxilla, posteriorly the bulla. It opens medially through the hiatus semilunaris."},
        {"q": "Where does the uncinate attach superiorly, and why does it matter?", "a": "Most often to the lamina (forming the recessus terminalis), so the frontal sinus drains medial to the uncinate. Otherwise to the skull base or middle turbinate, and then the frontal drains into the infundibulum."},
        {"q": "Where does the nasolacrimal duct open?", "a": "Inferior meatus under the inferior turbinate, at the valve of Hasner"},
        {"q": "Why must accessory and natural ostia be joined?", "a": "Mucociliary flow goes to the natural ostium regardless, so mucus exits and re-enters through the accessory opening (recirculation)"},
        {"q": "What is a Haller cell?", "a": "An infraorbital ethmoid cell along the orbital floor / medial maxillary roof that can narrow the infundibulum"},
        {"q": "What are the fontanelles?", "a": "Membranous areas of the medial maxillary wall above the inferior turbinate, anterior and posterior to the uncinate's inferior attachment"},
        {"q": "Silent sinus syndrome: anatomy?", "a": "Chronic ostial obstruction with negative pressure collapses the sinus walls. The orbital floor sinks (enophthalmos, hypoglobus) and the uncinate lateralizes."}
    ],
    "atlas_topics": ["Sinonasal Lateral Wall / Ostiomeatal Complex", "Orbit — Compartments / Canthi / Lacrimal System"],
    "sources": [
        ["Cummings Otolaryngology 7e: Endoscopic sinus surgery; anatomy of the lateral nasal wall", ""],
        ["Wormald PJ. Endoscopic Sinus Surgery, 4e", ""],
        ["Stammberger H. Functional Endoscopic Sinus Surgery", ""]
    ]
}

CASES["sphenoidotomy"] = {
    "title": "Endoscopic Sphenoidotomy",
    "region": "Rhinology / Skull Base",
    "summary": "The sphenoid sinus lies directly against the optic nerves, cavernous ICAs, sella and clivus, so the opening must start at the natural ostium and be enlarged inferiorly and medially, away from these structures. The ostium is found medial to the superior turbinate in the sphenoethmoidal recess. Inside, carotid and optic bulges and septations that insert on them are identified before any lateral or superior work.",
    "layers": [
        {"step": "Transnasal corridor", "structures": ["inferior and middle turbinates", "choana and posterior choanal arch", "septum", "superior turbinate"],
         "note": "Lateralize or medialize the middle turbinate gently. Look above the choana, between the septum and the superior turbinate, to find the sphenoethmoidal recess."},
        {"step": "Sphenoethmoidal recess and ostium", "structures": ["sphenoethmoidal recess", "natural sphenoid ostium (medial to the superior turbinate)", "olfactory mucosa (superior)"],
         "note": "The ostium is usually medial to the superior turbinate, above the level of its inferior edge and within about 1 cm of the midline. It is classically described as about 1-1.5 cm above the choanal arch, but cadaveric series report up to about 2-3 cm, so the superior turbinate is the more reliable guide. Resecting the lower part of the superior turbinate improves exposure; preserve its upper part, which carries olfactory mucosa."},
        {"step": "Enlarge inferiorly and medially", "structures": ["anterior sphenoid wall", "sphenoid rostrum / posterior septum", "posterior septal artery (crosses the sphenoid face below the ostium)"],
         "note": "Use a Kerrison or mushroom punch directed inferiorly and medially. The posterior septal artery crosses between the ostium and the choana; bipolar it, or preserve it if a nasoseptal flap may be needed."},
        {"step": "Transethmoid alternative", "structures": ["posterior ethmoid", "Onodi cell", "anterior sphenoid wall"],
         "note": "If coming through the ethmoid, enter the sphenoid at its lowest and most medial point. Confirm the opening against the transnasal ostium so a posterior ethmoid or Onodi cell is not mistaken for the sphenoid."},
        {"step": "Sinus survey", "structures": ["sella turcica (posterosuperior midline)", "planum sphenoidale (superior)", "clival recess (posteroinferior)", "optic prominence (superolateral)", "carotid prominence (lateral, paraclival / parasellar)", "lateral opticocarotid recess", "intersinus septum"],
         "note": "Identify the bulges before using powered instruments laterally or superiorly. Intersinus septa are often off midline and may insert onto the carotid prominence; remove them with through-cutting tools, never by twisting."},
        {"step": "Lateral recess (when pneumatized)", "structures": ["V2 / foramen rotundum (superolateral)", "vidian canal (floor, inferomedial)", "lateral recess under the greater wing"],
         "note": "A pneumatized lateral recess extends between V2 and the vidian nerve. It is a common site for lateral sphenoid encephalocele and CSF leak."}
    ],
    "landmarks": [
        {"structure": "Natural sphenoid ostium", "how_to_find": "Medial to the superior turbinate in the sphenoethmoidal recess, close to the septum (within about 1 cm of the midline), above the level of the superior turbinate's inferior edge. Classically about 1-1.5 cm above the posterior choanal arch, though reported distances range up to about 2-3 cm. Gently lateralize the superior turbinate or resect its inferior part to see it.", "why": "Safe entry point, inferior and medial to the optic nerve and ICA"},
        {"structure": "Posterior septal artery", "how_to_find": "Crosses the anterior sphenoid face horizontally between the inferior margin of the ostium and the choanal arch", "why": "Bleeds with inferior enlargement; it is the nasoseptal flap pedicle"},
        {"structure": "Optic nerve prominence", "how_to_find": "Superolateral wall, running from the sellar region anteriorly toward the orbital apex; the lateral opticocarotid recess sits just below it", "why": "Must be seen before any superolateral instrumentation"},
        {"structure": "Carotid prominence", "how_to_find": "Lateral wall below the optic prominence and lateral to the sella, curving from the parasellar to the paraclival segment", "why": "Can be dehiscent; septations may insert on it"},
        {"structure": "Sella and clival recess", "how_to_find": "Midline posterior wall: the sella bulges posterosuperiorly with the clival recess below", "why": "Orientation for midline skull base work"}
    ],
    "danger": [
        {"structure": "Internal carotid artery", "where": "Lateral sphenoid wall; dehiscent in a minority; septations may insert on it", "protect": "Map on CT, open inferomedially, use no powered lateral work and no twisting of septa", "injury": "Massive hemorrhage, stroke, pseudoaneurysm"},
        {"structure": "Optic nerve", "where": "Superolateral sphenoid wall, or lateral wall of an Onodi cell", "protect": "Confirm on CT, enter via the natural ostium inferomedially, and avoid heat or suction on the prominence", "injury": "Blindness"},
        {"structure": "Skull base (planum, sella, lateral recess)", "where": "Superior and posterior walls; lateral recess", "protect": "Enlarge inferiorly first and keep instruments below the ostium level when starting", "injury": "CSF leak, meningitis"},
        {"structure": "Posterior septal artery", "where": "Anterior sphenoid face, inferior to the ostium", "protect": "Bipolar before taking bone inferiorly, or preserve it for a flap", "injury": "Postoperative posterior epistaxis; loss of the nasoseptal flap pedicle"},
        {"structure": "Olfactory mucosa", "where": "Upper superior turbinate and opposing septum", "protect": "Resect only the inferior superior turbinate", "injury": "Hyposmia"}
    ],
    "variants": [
        "Pneumatization type: conchal (minimal, mainly pediatric), presellar, sellar (most common in adults), postsellar / extensive",
        "Onodi cell mimicking the sphenoid and carrying the optic nerve",
        "Dehiscent bone over the ICA or optic nerve",
        "Intersinus septum off midline, inserting on the carotid canal",
        "Lateral recess pneumatization into the pterygoid process or greater wing"
    ],
    "imaging_check": [
        "Pneumatization type and septation insertion points (axial and coronal)",
        "ICA and optic canal dehiscence; opticocarotid recess pneumatization",
        "Onodi cell",
        "Skull-base defects or encephalocele, especially in the lateral recess",
        "Ostium position relative to the superior turbinate (sagittal)"
    ],
    "blood_nerve": [
        ["Arterial", "Posterior septal and posterior lateral nasal branches of the SPA; posterior ethmoid artery superiorly"],
        ["Lateral wall relations", "Cavernous sinus containing the ICA and CN VI, with CN III, IV, V1 and V2 in its lateral wall"],
        ["Sensory", "Posterior ethmoidal nerve (V1) and V2 branches through the pterygopalatine ganglion"],
        ["Floor", "Vidian nerve and artery in the vidian canal"]
    ],
    "pimp": [
        {"q": "Where is the sphenoid ostium relative to the superior turbinate?", "a": "Medial to it, in the sphenoethmoidal recess"},
        {"q": "Which pneumatization type is most common in adults?", "a": "Sellar"},
        {"q": "Which cranial nerve runs free within the cavernous sinus beside the ICA?", "a": "CN VI (abducens). III, IV, V1 and V2 run in the lateral wall."},
        {"q": "What is the lateral opticocarotid recess?", "a": "The pneumatized optic strut of the anterior clinoid, between the optic nerve above and the ICA below"},
        {"q": "Pedicle of the nasoseptal flap?", "a": "Posterior septal artery (from the SPA), crossing the sphenoid face between the ostium and the choana"},
        {"q": "Which nerves bound the lateral recess?", "a": "V2 (foramen rotundum) superolaterally and the vidian nerve inferomedially"},
        {"q": "Why not twist the intersinus septum?", "a": "It may insert on the carotid canal and fracture into the ICA"}
    ],
    "atlas_topics": ["Sphenoid / Central Skull Base", "Sinonasal Lateral Wall / Ostiomeatal Complex", "Anterior / Central Cranial Base Foramina"],
    "sources": [
        ["Cummings Otolaryngology 7e: Endoscopic sinus surgery; endoscopic skull base anatomy", ""],
        ["Wormald PJ. Endoscopic Sinus Surgery, 4e: Sphenoid", ""],
        ["Kassam / Snyderman endoscopic endonasal anatomy literature (sphenoid landmarks)", ""]
    ]
}

CASES["draf"] = {
    "title": "Frontal Sinusotomy / Draf II-III",
    "region": "Rhinology / Skull Base",
    "summary": "The frontal sinus drains down an hourglass pathway, the frontal recess, which is bounded by the orbit laterally, the skull base and anterior ethmoid artery posteriorly, the middle turbinate medially, and the agger nasi and frontal beak anteriorly. Variable cells crowd the recess. Draf procedures remove these cells and then widen the outflow: IIa between the lamina and the middle turbinate, IIb from the lamina to the septum, and III joining both sides across the midline. The safe working zone is anterior and medial, away from the skull base and the AEA.",
    "layers": [
        {"step": "Anterior ethmoid and agger nasi", "structures": ["middle turbinate axilla and anterior attachment", "agger nasi cell", "superior uncinate attachment"],
         "note": "The agger nasi lies anterior and superior to the middle turbinate axilla, deep to the maxillary line. Removing its posterior and medial walls ('uncapping the egg') opens the lower frontal recess."},
        {"step": "Map frontal cells on CT", "structures": ["agger nasi / supra agger / supra agger frontal cells (anterior)", "suprabullar / suprabullar frontal / supraorbital ethmoid cells (posterior)", "frontal septal cell (medial)"],
         "note": "Using the IFAC framework, decide on multiplanar CT whether the drainage pathway runs medial, lateral or posterior to each cell before removing partitions. A supraorbital ethmoid cell can look like a second frontal sinus, and the AEA often runs along its posterior wall."},
        {"step": "Clear the recess from below upward", "structures": ["lamina papyracea / medial orbital wall (lateral)", "skull base and AEA (posterior)", "frontal beak (anterior)", "middle turbinate (medial)"],
         "note": "Use angled scopes and curved instruments. Fracture cell walls forward and medially away from the skull base, and remove the fragments without stripping mucosa circumferentially."},
        {"step": "Frontal ostium (Draf IIa)", "structures": ["frontal sinus ostium (narrowest point of the hourglass)", "posterior table", "frontal sinus floor"],
         "note": "Identify the true lumen (with image guidance or a seeker that passes freely and transilluminates). IIa means the opening runs from the lamina to the middle turbinate."},
        {"step": "Medial extension (Draf IIb)", "structures": ["anterior middle turbinate attachment", "frontal sinus floor medial to the turbinate", "nasal septum (medial limit)", "olfactory fossa (posteromedial)"],
         "note": "Resect the anterior middle turbinate attachment and drill the frontal floor medially to the septum. The posterior limit is the skull base: the olfactory fossa lies just behind and medial to the frontal floor."},
        {"step": "Midline opening (Draf III / EMLP)", "structures": ["superior septum (septal window)", "frontal intersinus septum", "frontal beak / nasofrontal process", "first olfactory fibres", "periosteum over the frontal process of the maxilla and skin (lateral-anterior limits)"],
         "note": "Create a septal window below the frontal floor. Drill the floor and beak across the midline to form the 'frontal T'. The first olfactory fibre marks the posterior limit. Laterally, drill until the periosteum of the frontal process or the orbit is reached on each side."},
        {"step": "Final check", "structures": ["frontal opening", "skull base", "orbit", "remaining mucosa"],
         "note": "Use 45-70 degree scopes to confirm no residual cell caps or obstructing partitions remain. Preserve mucosa, especially posteriorly, to limit circumferential scarring."}
    ],
    "landmarks": [
        {"structure": "Agger nasi cell", "how_to_find": "Anterior and superior to the middle turbinate axilla, beneath the maxillary line; it is the most anterior ethmoid cell", "why": "Its posterior wall forms the anterior wall of the frontal recess; removing it is the first step"},
        {"structure": "Frontal drainage pathway", "how_to_find": "On sagittal, coronal and axial CT, trace the outflow from the frontal ostium down past each cell, then follow it endoscopically with a seeker. It is medial to the uncinate when the uncinate attaches to the lamina.", "why": "Cells are removed in relation to the pathway, not blindly"},
        {"structure": "Anterior ethmoid artery", "how_to_find": "Posterior border of the frontal recess, usually just behind the skull-base attachment of the bulla lamella (roof of the suprabullar recess) or along the back of a supraorbital ethmoid cell; position varies. On coronal CT, look for the notch in the medial orbital wall.", "why": "Posterior limit of frontal dissection"},
        {"structure": "First olfactory fibre", "how_to_find": "Elevate septal mucosa just posterior to the frontal T at the anterior cribriform plate; the first fibres run into the olfactory fossa", "why": "Posterior limit of the Draf III drillout"},
        {"structure": "Frontal beak", "how_to_find": "Thick bone anterior to the frontal ostium, felt as a ledge; drill it forward to increase the anteroposterior diameter", "why": "The main bony obstruction to a wide opening"},
        {"structure": "Lateral limit", "how_to_find": "The lamina / medial orbital wall in Draf II, and the periosteum of the frontal process of the maxilla in Draf III", "why": "Defines how wide drilling can go"}
    ],
    "danger": [
        {"structure": "Anterior ethmoid artery", "where": "Posterior frontal recess at or just below the skull base; it may run free in a mesentery", "protect": "Locate on CT, keep posterior dissection minimal, and use bipolar if cut. Never avulse it.", "injury": "Retrobulbar hematoma (canthotomy), intracranial bleeding"},
        {"structure": "Skull base / lateral lamella / posterior table", "where": "Posterior and posteromedial to the frontal recess; the olfactory fossa sits just behind the frontal floor medially", "protect": "Work anteriorly, drill the beak rather than the posterior table, and respect the first olfactory fibre", "injury": "CSF leak, anosmia, intracranial injury"},
        {"structure": "Orbit (lamina papyracea, periorbita)", "where": "Lateral wall of the recess", "protect": "Fracture cells medially and identify the lamina before lateral drilling", "injury": "Orbital fat injury, hematoma, diplopia"},
        {"structure": "Lacrimal sac and duct", "where": "Anteroinferior to the lateral drilling in Draf III", "protect": "Stay above and behind the sac and identify the frontal process periosteum", "injury": "Epiphora"},
        {"structure": "Frontal recess mucosa", "where": "Circumference of the new opening", "protect": "Preserve mucosa, especially posteriorly, use mucosal grafts or flaps in Draf III, and avoid opposing raw surfaces", "injury": "Cicatricial restenosis, mucocele"}
    ],
    "variants": [
        "IFAC frontal cells: supra agger frontal cell, suprabullar frontal cell, frontal septal cell",
        "Supraorbital ethmoid cell (pneumatizing over the orbit), with the AEA along its posterior wall",
        "Uncinate attaching to the skull base or middle turbinate (frontal drains into the infundibulum)",
        "Hypoplastic or aplastic frontal sinus, or a narrow anteroposterior diameter (limits a Draf III)",
        "Low-lying skull base / Keros III olfactory fossa"
    ],
    "imaging_check": [
        "Sagittal anteroposterior diameter between the frontal beak and the skull base (determines feasibility of Draf III)",
        "Cell map and drainage pathway in three planes",
        "AEA position relative to the skull base",
        "Keros depth and posterior table integrity or dehiscence",
        "Lamina papyracea and any orbital extension of disease or mucocele"
    ],
    "blood_nerve": [
        ["Arterial", "AEA (ophthalmic); supraorbital and supratrochlear arteries to the frontal sinus mucosa and bone"],
        ["Venous", "Diploic veins and foramina of Breschet in the posterior table drain to the dural sinuses (intracranial spread)"],
        ["Sensory", "Supraorbital and supratrochlear nerves (V1)"],
        ["Olfactory", "First olfactory fibres just posterior to the frontal floor medially"]
    ],
    "pimp": [
        {"q": "Boundaries of the frontal recess?", "a": "Anterior: agger nasi / frontal beak. Posterior: bulla lamella / skull base with the AEA. Lateral: lamina papyracea. Medial: middle turbinate / lateral lamella."},
        {"q": "Define Draf I, IIa, IIb, III.", "a": "I: anterior ethmoidectomy clearing the recess without touching the ostium. IIa: ostium opened between lamina and middle turbinate. IIb: lamina to septum. III: bilateral IIb plus superior septectomy and removal of the intersinus septum (EMLP)."},
        {"q": "What is the posterior limit of a Draf III?", "a": "The first olfactory fibre / anterior olfactory fossa"},
        {"q": "Where does the frontal sinus drain when the uncinate attaches to the lamina?", "a": "Medial to the uncinate, directly into the middle meatus (the uncinate forms the recessus terminalis)"},
        {"q": "Name the anterior IFAC cells.", "a": "Agger nasi, supra agger cell, supra agger frontal cell"},
        {"q": "What are the foramina of Breschet?", "a": "Venous foramina in the frontal sinus mucosa and posterior table; a route for intracranial infection"},
        {"q": "What is Pott puffy tumor?", "a": "Frontal bone osteomyelitis with a subperiosteal abscess of the forehead, a complication of frontal sinusitis"},
        {"q": "When does the frontal sinus appear radiographically?", "a": "It is absent at birth and begins to pneumatize in early childhood; it usually becomes visible on imaging at roughly 5-8 years (sources vary) and keeps enlarging until late adolescence"}
    ],
    "atlas_topics": ["Frontal Recess Anatomy", "Ethmoid Skull Base / Lateral Lamella / AEA", "Orbit — Compartments / Canthi / Lacrimal System"],
    "sources": [
        ["Wormald PJ et al. The International Frontal Sinus Anatomy Classification (IFAC). Int Forum Allergy Rhinol 2016", ""],
        ["Draf W. Endonasal micro-endoscopic frontal sinus surgery: the Fulda concept. Oper Tech Otolaryngol 1991", ""],
        ["Cummings Otolaryngology 7e: Frontal sinus surgery", ""],
        ["Wormald PJ. Endoscopic Sinus Surgery, 4e: Frontal recess and modified Lothrop", ""]
    ]
}

CASES["spa-ligation"] = {
    "title": "Endoscopic Sphenopalatine Artery Ligation",
    "region": "Rhinology / Skull Base",
    "summary": "Most posterior epistaxis comes from the sphenopalatine artery (SPA), the terminal branch of the internal maxillary artery. The SPA enters the nose through the sphenopalatine foramen at the back of the middle meatus, just behind the crista ethmoidalis. Control works only if every branch is found, because the artery often divides into two or more branches before or at the foramen. Dissection stays out of the pterygopalatine fossa and away from the orbit above.",
    "layers": [
        {"step": "Expose the posterior lateral wall", "structures": ["middle turbinate (posterior attachment / tail)", "posterior fontanelle", "maxillary antrostomy (optional)", "posterior wall of maxillary sinus"],
         "note": "Clear clot and decongest, and medialize the middle turbinate. A maxillary antrostomy shows the posterior maxillary wall; the foramen sits just medial and superior to it."},
        {"step": "Mucoperiosteal flap", "structures": ["vertical incision on the lateral wall about 1 cm anterior to the middle turbinate tail / horizontal attachment", "mucoperiosteum", "perpendicular plate of palatine bone"],
         "note": "Elevate a subperiosteal flap posteriorly toward the foramen. Staying on bone keeps the flap intact and the field drier."},
        {"step": "Crista ethmoidalis", "structures": ["crista ethmoidalis (vertical ridge on the palatine bone)", "sphenopalatine foramen (just posterior)"],
         "note": "The crista is the key landmark: the foramen and artery lie immediately behind it. Removing the crista with a Kerrison widens the exposure of the artery and its branches."},
        {"step": "Identify all branches", "structures": ["posterior lateral nasal artery", "posterior septal artery (runs medially across the sphenoid face)", "accessory foramina / additional branches"],
         "note": "Elevate superiorly and inferiorly around the foramen to find every trunk. Clip and/or bipolar each branch. Inspect for an accessory foramen before laying the flap back."},
        {"step": "Reassess persistent bleeding", "structures": ["anterior and posterior ethmoid arteries (superior)", "septal sources", "contralateral supply", "greater palatine contribution"],
         "note": "Bleeding from high in the roof points to the ethmoid (ICA) system; these vessels are controlled surgically, not by embolization. Do not cauterize deeper into the pterygopalatine fossa or toward the orbit."}
    ],
    "landmarks": [
        {"structure": "Sphenopalatine foramen", "how_to_find": "At the posterior end of the middle turbinate horizontal attachment, at the junction of the middle and superior meatus, directly behind the crista ethmoidalis", "why": "Where the SPA and its branches enter the nose"},
        {"structure": "Crista ethmoidalis", "how_to_find": "A small vertical bony ridge on the perpendicular plate of the palatine bone, felt under the elevated flap just anterior to the foramen", "why": "The most reliable landmark; the artery emerges just posterior to it"},
        {"structure": "Posterior maxillary wall", "how_to_find": "Seen through a maxillary antrostomy; the foramen lies superomedial to it", "why": "Helps when the crista is small or absent"},
        {"structure": "Posterior septal artery", "how_to_find": "Leaves the foramen and runs medially across the anterior sphenoid face below the ostium", "why": "An alternative septal source that must be included in control"},
        {"structure": "Ethmoid arteries", "how_to_find": "Along the skull base, the AEA at the back of the frontal recess and the PEA in front of the sphenoid face", "why": "Bleeding from high in the roof points here instead of the SPA"}
    ],
    "danger": [
        {"structure": "Multiple SPA branches / accessory foramina", "where": "At and around the foramen; branching is often proximal to the foramen", "protect": "Wide subperiosteal exposure above and below the crista and check for additional branches before closing", "injury": "Missed branch and early rebleeding"},
        {"structure": "Orbit (lamina papyracea and orbital floor / apex)", "where": "Superolateral to the foramen if dissection drifts up and forward through the ethmoid or maxillary roof", "protect": "Keep dissection at the middle turbinate tail level and do not drill or cauterize superolaterally", "injury": "Orbital injury, hematoma"},
        {"structure": "Pterygopalatine fossa contents (internal maxillary artery, pterygopalatine ganglion, V2, vidian nerve)", "where": "Directly behind the foramen", "protect": "Control the vessel at the foramen and avoid deep cautery or packing into the fossa", "injury": "Uncontrolled bleeding, V2 numbness, dry eye from vidian / ganglion injury"},
        {"structure": "Descending (greater) palatine artery", "where": "In the pterygopalatine canal, inferior to the foramen within the palatine bone", "protect": "Avoid inferior drilling in the perpendicular plate", "injury": "Palatal ischemic symptoms, bleeding"},
        {"structure": "Skull base / sphenoid", "where": "Posterosuperior, above the sphenoid face", "protect": "Stay at the foramen level", "injury": "CSF leak"}
    ],
    "variants": [
        "The SPA divides into two or more branches before entering the nose in many patients",
        "Accessory foramen posterior or inferior to the main foramen",
        "Small or absent crista ethmoidalis",
        "Significant ethmoid (ICA system) contribution to posterior bleeding",
        "Hypervascular lesion (for example juvenile nasopharyngeal angiofibroma in an adolescent male) as the true source"
    ],
    "imaging_check": [
        "Not routinely imaged before urgent SPA ligation. Check clinically: hemodynamics, coagulopathy and anticoagulants, hypertension, HHT, and prior surgery.",
        "CT / CTA if there is trauma (pseudoaneurysm), suspected tumor, or prior sinus surgery",
        "Angiography when embolization is being considered (to map IMAX supply and dangerous ECA-ICA anastomoses)",
        "Adolescent male with unilateral obstruction and bleeding: image for JNA before instrumenting"
    ],
    "blood_nerve": [
        ["Arterial", "ECA, then internal maxillary artery (third / pterygopalatine segment), then SPA, which divides into the posterior lateral nasal and posterior septal arteries"],
        ["Anastomoses", "With the AEA and PEA (ophthalmic, from the ICA), the greater palatine and the superior labial; posterior inferior meatus plexus (Woodruff)"],
        ["Neural (pterygopalatine fossa)", "V2, pterygopalatine ganglion, vidian nerve (parasympathetic to the lacrimal gland and nasal glands)"]
    ],
    "pimp": [
        {"q": "What are the three segments of the internal maxillary artery?", "a": "Mandibular (first), pterygoid (second) and pterygopalatine (third); the SPA is the terminal branch of the third"},
        {"q": "Main landmark for the sphenopalatine foramen?", "a": "Crista ethmoidalis; the foramen is just posterior to it"},
        {"q": "What bones form the sphenopalatine foramen?", "a": "The sphenopalatine notch of the palatine bone (between its orbital and sphenoid processes), closed above by the sphenoid body"},
        {"q": "What are the two main SPA branches in the nose?", "a": "Posterior lateral nasal artery and posterior septal artery"},
        {"q": "Why is AEA bleeding not embolized?", "a": "It is an ophthalmic (ICA) branch; embolization risks blindness and stroke"},
        {"q": "What is Woodruff plexus?", "a": "A vascular plexus on the posterior lateral wall near the inferior meatus, historically described as venous; a source of posterior epistaxis"},
        {"q": "Why does ECA ligation fail more often than SPA ligation?", "a": "It is far from the bleeding point, so collaterals from the opposite ECA and from the ICA refill the nose"}
    ],
    "atlas_topics": ["Pterygopalatine Fossa / Autonomic Pathways", "External Carotid Artery Branches / Major Hemorrhage Anatomy", "Sinonasal Lateral Wall / Ostiomeatal Complex"],
    "sources": [
        ["Cummings Otolaryngology 7e: Epistaxis chapter", ""],
        ["Wormald PJ. Endoscopic Sinus Surgery, 4e: Endoscopic sphenopalatine artery ligation", ""],
        ["Simmen D, et al. The anatomy of the sphenopalatine artery for the endoscopic sinus surgeon. Am J Rhinol 2006", ""],
        ["AAO-HNSF Clinical Practice Guideline: Nosebleed (Epistaxis), 2020", ""]
    ]
}

CASES["orbital-abscess"] = {
    "title": "Endoscopic Orbital / Subperiosteal Abscess Drainage",
    "region": "Rhinology / Skull Base",
    "summary": "A subperiosteal orbital abscess forms when ethmoid infection crosses the thin lamina papyracea, or travels along valveless veins and neurovascular foramina, and collects between the bone and the periorbita. Endoscopic drainage removes the lamina over a medial collection and opens the diseased sinuses. The periorbita is the barrier that protects the medial rectus and orbital fat. The anterior and posterior ethmoid arteries and the optic canal mark the superior and posterior limits.",
    "layers": [
        {"step": "Nasal access", "structures": ["inflamed nasal mucosa", "middle turbinate", "uncinate", "maxillary ostium"],
         "note": "Decongest well. Uncinectomy and maxillary antrostomy show the orbital floor and give a reliable lateral reference at a known height in an inflamed, bloody field."},
        {"step": "Ethmoidectomy", "structures": ["ethmoid bulla", "anterior ethmoid cells", "basal lamella", "skull base"],
         "note": "Clear the ethmoid cells adjacent to the collection, which lies at the level shown on axial and coronal CT. Identify the skull base so the superior limit is known."},
        {"step": "Skeletonize and remove lamina papyracea", "structures": ["lamina papyracea", "frontoethmoidal suture line with the AEA and PEA (superior limit)", "lacrimal bone / posterior lacrimal crest (anterior)"],
         "note": "Thin bone may already be eroded and pus may appear. Remove the lamina over the collection with a Cottle or curette, keeping below the ethmoid arteries."},
        {"step": "Subperiosteal space", "structures": ["subperiosteal abscess", "periorbita"],
         "note": "Drain and culture. The space between the bone and the periorbita is open and the periorbita is usually intact; incise it only if an intraorbital (intraconal or extraconal) collection needs drainage."},
        {"step": "Periorbita and orbital contents (if opened)", "structures": ["extraconal fat", "medial rectus (deep to the periorbita, mid-height of the medial wall)", "superior oblique (superomedial)"],
         "note": "Make shallow incisions and use no powered instruments in the fat. Ask anesthesia for forced duction or globe movement if anatomy is unclear."},
        {"step": "Source sinuses and closure", "structures": ["maxillary, ethmoid, frontal and sphenoid drainage pathways"],
         "note": "Open the involved sinuses. Avoid tight nasal packing against the opened lamina, because it transmits pressure to the orbit."}
    ],
    "landmarks": [
        {"structure": "Lamina papyracea", "how_to_find": "Trace the medial orbital wall up from the orbital floor (seen through the maxillary antrostomy); it lies in the plane of the medial maxillary wall", "why": "The bone to remove over the abscess"},
        {"structure": "Abscess location", "how_to_find": "Match the craniocaudal and anteroposterior position on CT to ethmoid landmarks (bulla, basal lamella); pus often appears through eroded bone", "why": "Directs the bone window"},
        {"structure": "Anterior and posterior ethmoid arteries", "how_to_find": "Along the frontoethmoidal suture at the top of the lamina where it meets the skull base", "why": "Superior limit of bone removal"},
        {"structure": "Optic canal", "how_to_find": "Posterior limit, in the posterolateral sphenoid / Onodi cell; classically about 6 mm behind the PEA, but reported distances are about 4-7 mm and can be shorter, so confirm on CT", "why": "Do not extend posterior decompression without intent"},
        {"structure": "Medial rectus", "how_to_find": "Deep to the periorbita and a thin fat layer at about mid-height of the medial wall; ballotting the globe moves it", "why": "Most commonly injured muscle in endoscopic orbital work"}
    ],
    "danger": [
        {"structure": "Optic nerve", "where": "Orbital apex and optic canal, posterior to the PEA", "protect": "Limit posterior bone removal, use CT orientation, and avoid packing or pressure", "injury": "Vision loss"},
        {"structure": "Medial rectus", "where": "Deep to the periorbita over the mid medial wall", "protect": "Keep the periorbita intact unless necessary, make shallow incisions, and use no microdebrider in orbital fat", "injury": "Diplopia, restrictive or paretic strabismus"},
        {"structure": "Anterior and posterior ethmoid arteries", "where": "Top of the lamina at the frontoethmoidal suture", "protect": "Stay below them and use bipolar if cut", "injury": "Orbital hematoma and orbital compartment syndrome"},
        {"structure": "Skull base", "where": "Above the ethmoid cells; inflamed bone may be soft", "protect": "Identify the skull base early", "injury": "CSF leak, intracranial spread"},
        {"structure": "Nasolacrimal sac", "where": "Anterior to the lamina at the lacrimal fossa", "protect": "Stay posterior to the lacrimal bone", "injury": "Epiphora"}
    ],
    "variants": [
        "Dehiscent or eroded lamina papyracea",
        "Superior or lateral subperiosteal abscess (often of frontal origin), which usually needs an external approach",
        "Small, incompletely pneumatized sinuses in young children",
        "Onodi cell bringing the optic nerve forward",
        "Low or asymmetric skull base"
    ],
    "imaging_check": [
        "Contrast CT: subperiosteal versus intraorbital abscess, size, and medial versus superior or lateral location",
        "Source sinus and its relation to the lamina, skull base and ethmoid arteries",
        "Intracranial complications (epidural or subdural abscess, cavernous sinus thrombosis); obtain MRI if suspected",
        "Clinically, document vision, color vision, pupils (RAPD), extraocular movements, proptosis and intraocular pressure"
    ],
    "blood_nerve": [
        ["Arterial", "Ophthalmic artery (ICA) giving the AEA and PEA"],
        ["Venous", "Valveless superior and inferior ophthalmic veins to the cavernous sinus and pterygoid plexus (spread of infection)"],
        ["Nerves", "CN III inferior division to the medial rectus; V1 (nasociliary to the ethmoidal nerves); optic nerve via the optic canal"]
    ],
    "pimp": [
        {"q": "Give the Chandler classification.", "a": "I preseptal cellulitis, II orbital cellulitis, III subperiosteal abscess, IV orbital abscess, V cavernous sinus thrombosis"},
        {"q": "What separates preseptal from postseptal infection?", "a": "The orbital septum (from the orbital rim periosteum to the tarsal plates)"},
        {"q": "Why does ethmoid infection reach the orbit easily?", "a": "Thin and sometimes dehiscent lamina, neurovascular foramina, and valveless ophthalmic veins"},
        {"q": "What passes through the annulus of Zinn?", "a": "CN III (superior and inferior divisions), nasociliary nerve and CN VI; the optic nerve and ophthalmic artery enter through the optic canal within the ring"},
        {"q": "What passes through the superior orbital fissure outside the annulus?", "a": "Frontal, lacrimal and trochlear nerves and the superior ophthalmic vein"},
        {"q": "Innervation of the medial rectus?", "a": "Inferior division of the oculomotor nerve"},
        {"q": "Contents of the optic canal?", "a": "Optic nerve and ophthalmic artery"}
    ],
    "atlas_topics": ["Orbit — Compartments / Canthi / Lacrimal System", "Ethmoid Skull Base / Lateral Lamella / AEA", "Sinonasal Lateral Wall / Ostiomeatal Complex"],
    "sources": [
        ["Chandler JR, Langenbrunner DJ, Stevens ER. The pathogenesis of orbital complications in acute sinusitis. Laryngoscope 1970", ""],
        ["Cummings Otolaryngology 7e: Complications of rhinosinusitis", ""],
        ["Bailey's Head and Neck Surgery-Otolaryngology 5e: Orbital complications of sinusitis", ""]
    ]
}

CASES["parathyroidectomy"] = {
    "title": "Parathyroidectomy",
    "region": "Thyroid / Parathyroid / Salivary",
    "summary": "Parathyroidectomy finds and removes abnormal parathyroid tissue. The glands have predictable embryologic positions relative to the recurrent laryngeal nerve (RLN) and the inferior thyroid artery (ITA). Superior glands (fourth pouch) lie posterior and dorsal to the coronal plane of the RLN at the upper-mid lobe. Inferior glands (third pouch, with the thymus) lie anterior and ventral to the nerve near the lower pole, and are the more variable and more often ectopic. Safety depends on seeing the RLN before dividing tissue in the tracheoesophageal groove and on preserving the blood supply of the normal glands.",
    "layers": [
        {"step": "Incision and flaps", "structures": ["skin", "platysma", "anterior jugular veins", "investing layer of deep cervical fascia"],
         "note": "Use a short low transverse incision placed according to localization, and plan it so it can be extended. Raise limited subplatysmal flaps."},
        {"step": "Strap muscles", "structures": ["midline raphe (linea alba)", "sternohyoid (superficial)", "sternothyroid (deep, attached to the thyroid capsule)"],
         "note": "Open the midline and retract the straps laterally. A lateral approach between the SCM and the straps gives direct access to a posterior adenoma."},
        {"step": "Thyroid rotation", "structures": ["thyroid lobe", "middle thyroid vein", "carotid sheath (lateral)"],
         "note": "Divide the middle thyroid vein if needed and rotate the lobe medially to enter the plane behind the thyroid, between it and the carotid sheath."},
        {"step": "Tracheoesophageal groove and nerve", "structures": ["RLN", "ITA", "tubercle of Zuckerkandl", "tracheoesophageal groove"],
         "note": "Identify the RLN, or a nerve-safe zone, before dividing anything near the ITA. The right RLN runs more obliquely from lateral to medial; the left runs more vertically in the groove."},
        {"step": "Search by embryologic location", "structures": ["superior parathyroid (posterior upper-mid lobe, near the cricothyroid junction, about 1 cm above the ITA-RLN crossing)", "inferior parathyroid (lower pole, anterior / lateral, thyrothymic ligament)", "thymic tongue"],
         "note": "A normal gland is yellow-tan to mahogany, flat and oval, may move in fat, and has a hilar vessel. An adenoma is larger and darker. Fat is yellower and lighter; lymph nodes are gray and firm; thyroid nodules are redder and continuous with the gland."},
        {"step": "Gland mobilization", "structures": ["adenoma capsule", "vascular pedicle (usually from the ITA)", "RLN (deep and medial for superior glands)"],
         "note": "Dissect around the capsule without rupturing it (rupture risks parathyromatosis). Control the pedicle last. Superior adenomas often descend posteriorly along the esophagus, deep to the RLN."},
        {"step": "Ectopic search if IOPTH does not fall", "structures": ["thymus / anterior mediastinum (inferior)", "retroesophageal / paraesophageal space (superior)", "carotid sheath up to the angle of the mandible (undescended inferior)", "intrathyroidal", "contralateral glands"],
         "note": "Follow the embryology: inferior glands lie anywhere along the thymic descent; superior glands lie posteriorly in the tracheoesophageal groove or retroesophageal space, extending into the posterior mediastinum."}
    ],
    "landmarks": [
        {"structure": "Superior parathyroid", "how_to_find": "Posterior surface of the upper-mid lobe at about the cricoid level, about 1 cm cranial to where the RLN crosses the ITA, dorsal to the RLN plane, often under the tubercle of Zuckerkandl", "why": "More constant position; a superior adenoma may sink posteriorly and inferiorly"},
        {"structure": "Inferior parathyroid", "how_to_find": "Ventral to the RLN plane, on the anterior, lateral or posterior surface of the lower pole, or in the thyrothymic ligament / thymic tongue", "why": "More variable location because of the longer descent with the thymus"},
        {"structure": "RLN", "how_to_find": "In the tracheoesophageal groove below the ITA, within the triangle bordered by the trachea / esophagus medially, the common carotid laterally and the ITA superiorly. Then follow it to its entry under the inferior constrictor behind the cricothyroid joint.", "why": "Must be seen before dividing tissue in the groove"},
        {"structure": "ITA", "how_to_find": "From the thyrocervical trunk, it rises behind the carotid and loops medially at the mid-lobe to reach the thyroid; its branches supply both parathyroids", "why": "Orientation for both glands and for the nerve"},
        {"structure": "Tubercle of Zuckerkandl", "how_to_find": "Posterolateral projection of the lobe at about the cricoid level; lift it medially", "why": "The RLN usually lies deep and medial to it, and the superior gland lies nearby"},
        {"structure": "Thyrothymic ligament", "how_to_find": "Band of tissue from the lower pole into the superior mediastinum; deliver it with gentle traction", "why": "Common site of an inferior gland or inferior adenoma"}
    ],
    "danger": [
        {"structure": "Recurrent laryngeal nerve", "where": "Tracheoesophageal groove; superior adenomas often lie posterior to it, inferior adenomas anterior", "protect": "Identify before dividing tissue in the groove, use no energy device near it, and trace a nonrecurrent nerve on the right if no nerve is found low", "injury": "Vocal fold paralysis, hoarseness, aspiration"},
        {"structure": "Inferior thyroid artery branches", "where": "Terminal branches to the parathyroids and the thyroid capsule", "protect": "Ligate adenoma pedicles close to the gland and preserve branches to normal glands", "injury": "Devascularization of normal glands, causing hypoparathyroidism"},
        {"structure": "Normal parathyroid glands", "where": "Superior and inferior positions bilaterally", "protect": "Minimal handling and do not biopsy unnecessarily; autotransplant a devascularized gland", "injury": "Permanent hypoparathyroidism"},
        {"structure": "Esophagus and trachea", "where": "Deep and medial during retroesophageal or paraesophageal exploration", "protect": "Blunt dissection along the prevertebral fascia and a bougie or nasogastric tube if needed", "injury": "Perforation, mediastinitis"},
        {"structure": "Neck hematoma", "where": "Central compartment beneath the strap muscles", "protect": "Valsalva check and meticulous hemostasis", "injury": "Airway compromise; open the wound at the bedside"}
    ],
    "variants": [
        "Nonrecurrent right inferior laryngeal nerve (about 0.3-0.8% of right sides in large series), almost always with a retroesophageal right subclavian artery (arteria lusoria); a left nonrecurrent nerve is exceptionally rare (about 0.004%) and needs situs inversus / a right-sided arch",
        "Supernumerary glands (most often in the thymus)",
        "Ectopic inferior gland: thymus or anterior mediastinum, undescended in the carotid sheath, intrathyroidal",
        "Ectopic superior gland: retroesophageal or retropharyngeal, posterior mediastinum along the tracheoesophageal groove",
        "Extralaryngeal branching of the RLN (motor fibres usually in the anterior branch)"
    ],
    "imaging_check": [
        "Concordance of sestamibi / SPECT-CT, ultrasound and 4D-CT: side, level and depth (anterior versus posterior to the RLN plane)",
        "Ectopic location (mediastinum, carotid sheath, retroesophageal)",
        "Concurrent thyroid nodules that need treatment or could be mistaken for adenoma",
        "Retroesophageal right subclavian artery on CT (predicts a nonrecurrent RLN)",
        "Preoperative laryngeal exam; check for multigland disease risk (MEN, familial) clinically"
    ],
    "blood_nerve": [
        ["Arterial", "ITA (thyrocervical trunk) supplies most superior and inferior glands; superior glands may receive STA branches or an anastomotic loop"],
        ["Venous", "Thyroid veins: superior and middle to the IJV, inferior to the brachiocephalic vein"],
        ["Nerves", "RLN in the tracheoesophageal groove; EBSLN at the superior pole (rarely exposed); cervical sympathetic chain posterolateral"],
        ["Embryology", "Superior: fourth pharyngeal pouch (with the ultimobranchial body). Inferior: third pouch (with the thymus)."]
    ],
    "pimp": [
        {"q": "Embryologic origin of the superior and inferior parathyroids?", "a": "Superior from the fourth pouch; inferior from the third pouch with the thymus"},
        {"q": "Why are inferior glands more often ectopic?", "a": "They travel further, descending with the thymus, so they can stop high or end up in the mediastinum"},
        {"q": "Relationship of each gland to the RLN?", "a": "Superior glands are dorsal (posterior) to the coronal plane of the RLN; inferior glands are ventral (anterior)"},
        {"q": "Most common ectopic site for an inferior gland? For a superior gland?", "a": "Inferior: thymus / anterior mediastinum. Superior: tracheoesophageal groove / retroesophageal space."},
        {"q": "State the Miami criterion.", "a": "IOPTH falls more than 50% from the highest pre-excision value at 10 minutes after excision"},
        {"q": "What anomaly predicts a nonrecurrent laryngeal nerve?", "a": "Retroesophageal (aberrant) right subclavian artery, on the right side"},
        {"q": "Main blood supply of the parathyroids?", "a": "Inferior thyroid artery"},
        {"q": "Where is a parathyroid autograft usually placed?", "a": "Minced into the SCM (or the brachioradialis forearm muscle for hyperplasia)"}
    ],
    "atlas_topics": ["Parathyroid Embryology / Ectopic Map", "Thyroid / RLN / EBSLN Anatomy"],
    "sources": [
        ["Cummings Otolaryngology 7e: Management of parathyroid disorders", ""],
        ["Randolph GW. Surgery of the Thyroid and Parathyroid Glands, 3e", ""],
        ["Akerstrom G, et al. Surgical anatomy of human parathyroid glands. Surgery 1984", ""],
        ["AAES Guidelines for definitive management of primary hyperparathyroidism. JAMA Surg 2016", ""]
    ]
}

CASES["thyroid-lobectomy"] = {
    "title": "Thyroid Lobectomy",
    "region": "Thyroid / Parathyroid / Salivary",
    "summary": "Thyroid lobectomy is a dissection on the thyroid capsule that removes the lobe while keeping two nerves and two glands safe. The external branch of the superior laryngeal nerve (EBSLN) runs near the superior pole vessels. The RLN runs up the tracheoesophageal groove to enter the larynx at Berry ligament. The superior and inferior parathyroids keep their blood supply only if inferior thyroid artery branches are divided on the capsule. The highest-risk point is Berry ligament, where the RLN is closest to the gland.",
    "layers": [
        {"step": "Incision and subplatysmal flaps", "structures": ["skin crease incision about 1-2 fingerbreadths above the sternal notch", "platysma", "anterior jugular veins (superficial to the strap fascia)"],
         "note": "Raise flaps superiorly to the thyroid notch and inferiorly to the sternal notch in the subplatysmal plane, leaving the anterior jugular veins down on the straps."},
        {"step": "Strap muscles", "structures": ["linea alba", "sternohyoid", "sternothyroid (inserts on the oblique line of the thyroid cartilage)", "ansa cervicalis (enters the straps from below and laterally)"],
         "note": "Separate the straps in the midline. If they must be divided for a large gland, divide them high so the ansa innervation from below is preserved."},
        {"step": "Lateral mobilization", "structures": ["false (pretracheal) fascia and true capsule", "middle thyroid vein", "carotid sheath"],
         "note": "Peel the sternothyroid off the lobe. Divide the middle thyroid vein so the lobe can be rotated medially."},
        {"step": "Superior pole", "structures": ["superior thyroid artery and vein", "sternothyroid-laryngeal (Joll) triangle", "EBSLN on the inferior constrictor", "cricothyroid muscle"],
         "note": "Pull the pole down and laterally to open the avascular plane between the pole and the cricothyroid. Ligate branches individually on the capsule, below where the EBSLN may cross."},
        {"step": "Inferior pole", "structures": ["inferior thyroid veins", "thyrothymic ligament", "inferior parathyroid"],
         "note": "Divide the inferior veins on the capsule. Sweep the inferior parathyroid and thymic tissue away with their blood supply intact."},
        {"step": "RLN identification", "structures": ["RLN", "ITA", "tubercle of Zuckerkandl", "inferior cornu of thyroid cartilage"],
         "note": "Find the nerve where the anatomy is undisturbed: inferiorly in the groove, laterally at the ITA, or superiorly at the laryngeal entry. Then follow it upward as the lobe is rotated."},
        {"step": "Superior parathyroid and terminal vessels", "structures": ["superior parathyroid", "ITA terminal branches on the capsule"],
         "note": "Mobilize the superior gland off the posterior capsule on its pedicle. Divide ITA branches on the capsule, not at the trunk."},
        {"step": "Berry ligament and isthmus", "structures": ["posterior suspensory (Berry) ligament", "RLN at laryngeal entry", "cricoid and first tracheal rings", "isthmus / pyramidal lobe", "Delphian (prelaryngeal) node"],
         "note": "Divide Berry ligament sharply under direct vision of the nerve, with no energy device close to it. Divide the isthmus and remove any pyramidal lobe up toward the hyoid."}
    ],
    "landmarks": [
        {"structure": "EBSLN", "how_to_find": "Retract the superior pole inferolaterally and open Joll triangle (medially the cricothyroid / inferior constrictor, laterally the pole vessels, superiorly the sternothyroid insertion). Look for the nerve on the inferior constrictor running down to the cricothyroid, or confirm by monitor (cricothyroid twitch).", "why": "Avoid the ligature and energy zone when it runs low (Cernea 2b)"},
        {"structure": "RLN, inferior approach", "how_to_find": "Low in the tracheoesophageal groove near the thoracic inlet. The right nerve runs more obliquely from lateral to medial; the left is more vertical and closer to the groove.", "why": "Virgin territory, useful for large or revision cases"},
        {"structure": "RLN, lateral approach", "how_to_find": "At the ITA crossing at mid-lobe; the nerve may pass anterior, posterior or between ITA branches", "why": "Most commonly used point of identification"},
        {"structure": "RLN, superior approach", "how_to_find": "At its entry under the inferior constrictor just posterior and inferior to the inferior cornu of the thyroid cartilage / cricothyroid joint", "why": "Constant position; useful for large substernal goiters"},
        {"structure": "Tubercle of Zuckerkandl", "how_to_find": "Posterolateral projection at the cricoid level; lift it medially", "why": "The RLN usually lies medial and deep to it; the superior parathyroid sits nearby"},
        {"structure": "Berry ligament", "how_to_find": "Dense attachment of the posteromedial lobe to the cricoid and first tracheal rings, just medial to the nerve's entry point", "why": "Point of closest nerve-to-gland contact"}
    ],
    "danger": [
        {"structure": "Recurrent laryngeal nerve", "where": "Tracheoesophageal groove to Berry ligament; may branch extralaryngeally", "protect": "Visual identification along its course, no energy device within a few mm, minimal traction on the lobe at Berry ligament, and neuromonitoring as an adjunct", "injury": "Vocal fold paralysis, dysphonia, aspiration"},
        {"structure": "EBSLN", "where": "Close to the superior thyroid artery near the upper pole, especially when it crosses below the top of the pole", "protect": "Individual capsular ligation of branches and no mass ligation high on the pedicle", "injury": "Cricothyroid paralysis, causing loss of pitch range and projection and voice fatigue"},
        {"structure": "Parathyroid glands and pedicles", "where": "Superior gland on the posterior upper lobe; inferior gland at the lower pole", "protect": "Capsular dissection, divide ITA branches distal to the parathyroid branches, and autotransplant if devascularized", "injury": "Hypocalcemia (relevant if the contralateral glands are later removed)"},
        {"structure": "Trachea and esophagus", "where": "Medial and posterior to the lobe at Berry ligament", "protect": "Sharp dissection and care with energy devices", "injury": "Tracheal or esophageal injury"},
        {"structure": "Hematoma", "where": "Under the straps in the central neck", "protect": "Valsalva check and ligation of the superior pole vessels individually", "injury": "Airway compromise; open the wound urgently"}
    ],
    "variants": [
        "Nonrecurrent right inferior laryngeal nerve (aberrant right subclavian)",
        "Extralaryngeal RLN branching before laryngeal entry",
        "Cernea type 2b EBSLN, crossing the pedicle below the upper border of the pole",
        "Pyramidal lobe (thyroglossal remnant) extending toward the hyoid",
        "Thyroid ima artery from the brachiocephalic trunk or aortic arch (small minority)"
    ],
    "imaging_check": [
        "Ultrasound: nodule location, extrathyroidal extension, central and lateral neck nodes",
        "CT if substernal extension, tracheal compression or deviation, or a fixed mass",
        "Retroesophageal subclavian artery on any CT obtained",
        "Preoperative laryngoscopy to document vocal fold mobility"
    ],
    "blood_nerve": [
        ["Arterial", "Superior thyroid artery (first anterior ECA branch); ITA (thyrocervical trunk); thyroid ima (variable)"],
        ["Venous", "Superior and middle thyroid veins to the IJV; inferior thyroid veins to the brachiocephalic veins"],
        ["Motor", "RLN to all intrinsic laryngeal muscles except the cricothyroid; EBSLN to the cricothyroid; ansa cervicalis to the straps"],
        ["Embryology", "Median anlage from the foramen cecum, descending as the thyroglossal duct; lateral anlage (ultimobranchial body, fourth pouch) gives parafollicular C cells"]
    ],
    "pimp": [
        {"q": "Around which vessels does each RLN loop?", "a": "Right: the subclavian artery. Left: the aortic arch at the ligamentum arteriosum."},
        {"q": "Boundaries of Joll (sternothyroid-laryngeal) triangle?", "a": "Medially the cricothyroid / inferior constrictor, laterally the superior pole vessels, superiorly the sternothyroid insertion on the oblique line"},
        {"q": "Describe the Cernea classification.", "a": "EBSLN crosses the STA: type 1 more than 1 cm above the upper pole, type 2a within 1 cm above it, type 2b below the upper border of the pole"},
        {"q": "What does the EBSLN innervate, and what is the deficit?", "a": "Cricothyroid; loss of pitch elevation and projection, voice fatigue"},
        {"q": "Where does the RLN enter the larynx?", "a": "Under the inferior constrictor, posterior to the cricothyroid joint (inferior cornu of the thyroid cartilage)"},
        {"q": "Where does the thyroid arise embryologically?", "a": "Foramen cecum of the tongue; descends anterior to the hyoid as the thyroglossal duct"},
        {"q": "Why divide the straps high?", "a": "The ansa cervicalis enters them inferiorly, so high division preserves innervation"},
        {"q": "What is the Delphian node?", "a": "The prelaryngeal node on the cricothyroid membrane"}
    ],
    "atlas_topics": ["Thyroid / RLN / EBSLN Anatomy", "Superior Laryngeal Nerve / Cricothyroid Space", "Parathyroid Embryology / Ectopic Map"],
    "sources": [
        ["Cummings Otolaryngology 7e: Management of thyroid neoplasms; thyroid surgery", ""],
        ["Randolph GW. Surgery of the Thyroid and Parathyroid Glands, 3e", ""],
        ["Cernea CR, et al. Surgical anatomy of the external branch of the superior laryngeal nerve. Head Neck 1992", ""],
        ["Myers EN. Operative Otolaryngology, 2e: Thyroidectomy", ""]
    ]
}

CASES["total-thyroidectomy"] = {
    "title": "Total Thyroidectomy",
    "region": "Thyroid / Parathyroid / Salivary",
    "summary": "Total thyroidectomy repeats the capsular lobectomy on both sides. What changes is the stakes: both RLNs and all four parathyroids are at risk at once. Bilateral RLN injury leaves both vocal folds paramedian and threatens the airway. Losing the blood supply of all parathyroids causes permanent hypocalcemia. The anatomy differs by side (left RLN vertical in the groove, right RLN oblique, and a possible right nonrecurrent nerve), and confirming nerve function after the first side decides whether to proceed.",
    "layers": [
        {"step": "Exposure", "structures": ["skin", "platysma", "anterior jugular veins", "linea alba", "sternohyoid and sternothyroid", "pyramidal lobe / Delphian node"],
         "note": "Use a low transverse incision and subplatysmal flaps to the thyroid notch and sternal notch. Open the midline raphe fully. Look for a pyramidal lobe along the midline toward the hyoid; it must be removed in a total thyroidectomy."},
        {"step": "First lobe: lateral and superior pole", "structures": ["middle thyroid vein", "superior thyroid vessels", "EBSLN", "Joll triangle"],
         "note": "As for lobectomy: divide the middle vein, open the avascular space medial to the superior pole, and ligate branches individually on the capsule."},
        {"step": "First lobe: parathyroids and RLN", "structures": ["inferior parathyroid / thyrothymic ligament", "RLN", "ITA", "superior parathyroid", "tubercle of Zuckerkandl"],
         "note": "Preserve each gland on its pedicle as found. Identify the RLN and follow it up to Berry ligament, dividing terminal ITA branches on the capsule."},
        {"step": "Berry ligament and isthmus", "structures": ["Berry ligament", "RLN entry", "isthmus", "trachea"],
         "note": "Release sharply under vision and carry the specimen across the trachea."},
        {"step": "Decision point", "structures": ["ipsilateral vagus / RLN signal (if monitored)", "visual nerve integrity"],
         "note": "If there is unexplained loss of signal on the first side, consider staging the contralateral lobectomy to avoid bilateral paralysis."},
        {"step": "Contralateral lobe", "structures": ["contralateral superior pole and EBSLN", "contralateral parathyroids", "contralateral RLN (opposite course)", "Berry ligament"],
         "note": "Repeat every step in full. Expect a different nerve course: the left RLN is more vertical, deeper and in the groove; the right is more oblique and lateral, and a right nonrecurrent nerve runs directly from the vagus at about the laryngeal level."},
        {"step": "Final survey", "structures": ["both parathyroid beds", "both RLNs", "hemostasis (Valsalva)"],
         "note": "Inspect parathyroid color. Autotransplant any devascularized gland into the SCM after a frozen-section confirmation sliver if there is doubt."}
    ],
    "landmarks": [
        {"structure": "Left RLN", "how_to_find": "Rises more vertically and medially in the tracheoesophageal groove from the aortic arch; find it low in the groove or at the ITA", "why": "More predictable course but closely applied to the trachea"},
        {"structure": "Right RLN", "how_to_find": "Runs obliquely from lateral (from the subclavian) to medial. It is more exposed and lateral in the lower neck and enters the groove higher up. If none is found low, look for a nonrecurrent nerve running horizontally from the vagus near the cricoid / ITA level.", "why": "Higher risk of a variant course"},
        {"structure": "EBSLN (both sides)", "how_to_find": "Joll triangle with the pole retracted inferolaterally; nerve on the inferior constrictor heading to the cricothyroid", "why": "Bilateral injury causes significant pitch and voice-fatigue loss"},
        {"structure": "Four parathyroids", "how_to_find": "Superior: posterior upper-mid lobe, dorsal to the RLN, about 1 cm above the ITA crossing. Inferior: near the lower pole, ventral to the RLN, or in the thyrothymic ligament.", "why": "Keeping each on its pedicle prevents permanent hypoparathyroidism"},
        {"structure": "Berry ligament", "how_to_find": "Posteromedial attachment to the cricoid and upper trachea at the nerve entry point", "why": "Point of greatest nerve risk on each side"},
        {"structure": "Pyramidal lobe", "how_to_find": "Superior extension from the isthmus, usually left of midline, toward the hyoid along the thyroglossal tract", "why": "Residual tissue affects radioiodine uptake and Tg surveillance"}
    ],
    "danger": [
        {"structure": "Bilateral RLNs", "where": "Both tracheoesophageal grooves and Berry ligaments", "protect": "Identify both nerves, monitor and confirm the signal after the first side, and stage if loss of signal occurs", "injury": "Bilateral vocal fold paralysis with stridor and airway obstruction; possible tracheostomy"},
        {"structure": "All parathyroids and ITA branches", "where": "Posterior capsule bilaterally", "protect": "Capsular dissection, branch ligation distal to the parathyroid branches, and autotransplant of devascularized glands", "injury": "Transient or permanent hypoparathyroidism and hypocalcemia"},
        {"structure": "EBSLN (bilateral)", "where": "Superior poles", "protect": "Individual capsular ligation", "injury": "Loss of pitch range and projection"},
        {"structure": "Trachea and esophagus", "where": "Under the isthmus and at Berry ligament; at risk in large goiters and with tracheomalacia", "protect": "Sharp dissection and limited energy use", "injury": "Tracheal perforation or injury, esophageal injury"},
        {"structure": "Neck hematoma", "where": "Central compartment, often from the superior pole or strap vessels", "protect": "Valsalva, meticulous hemostasis and good closure", "injury": "Airway compromise needing bedside wound opening"},
        {"structure": "Thermal spread", "where": "Energy devices near the nerve or parathyroid pedicles", "protect": "Keep active blades a few mm from the nerve and turn the blade away", "injury": "Neurapraxia or delayed paralysis"}
    ],
    "variants": [
        "Right nonrecurrent laryngeal nerve (aberrant right subclavian artery); a left nonrecurrent nerve needs situs inversus and is exceptionally rare",
        "Extralaryngeal RLN branching (motor fibres usually in the anterior branch)",
        "Pyramidal lobe, thyroglossal tract remnants",
        "Substernal extension, usually supplied from the neck by the ITA",
        "Intrathyroidal or ectopic parathyroid"
    ],
    "imaging_check": [
        "Ultrasound of both lobes and the central and lateral necks",
        "CT for substernal extent, tracheal compression and an aberrant subclavian artery",
        "Preoperative laryngoscopy (mandatory baseline before bilateral surgery)",
        "Baseline calcium, PTH and vitamin D clinically"
    ],
    "blood_nerve": [
        ["Arterial", "Bilateral STA and ITA; occasional thyroid ima"],
        ["Venous", "Superior and middle thyroid veins to the IJV; inferior thyroid veins to the brachiocephalic veins"],
        ["Nerves", "Bilateral RLNs, bilateral EBSLNs, ansa cervicalis to the straps"],
        ["Parathyroid supply", "ITA branches primarily"]
    ],
    "pimp": [
        {"q": "Position of the vocal folds after bilateral RLN injury?", "a": "Paramedian. The voice is often fairly good, but the glottic airway is narrow, causing stridor and airway compromise"},
        {"q": "Why is the right RLN at greater risk of variant anatomy?", "a": "A nonrecurrent course occurs on the right with an aberrant retroesophageal subclavian; the right also runs more obliquely and laterally"},
        {"q": "What is loss of signal on neuromonitoring?", "a": "Usually defined as an evoked EMG amplitude below 100 microvolts with a previously good signal (after excluding equipment problems)"},
        {"q": "How do you confirm devascularized tissue is parathyroid before autotransplantation?", "a": "Frozen section of a small sliver; then mince it into SCM pockets"},
        {"q": "Clinical signs of hypocalcemia?", "a": "Chvostek (facial nerve tap) and Trousseau (carpal spasm with cuff); perioral and digital paresthesia"},
        {"q": "Which branch of the RLN usually carries the motor fibres when it branches extralaryngeally?", "a": "The anterior branch"},
        {"q": "What remnant can lie between the isthmus and the hyoid?", "a": "Pyramidal lobe / thyroglossal duct remnant"},
        {"q": "Blood supply of a substernal goiter?", "a": "Usually cervical (ITA); it can usually be delivered through the neck"}
    ],
    "atlas_topics": ["Thyroid / RLN / EBSLN Anatomy", "Parathyroid Embryology / Ectopic Map", "Superior Laryngeal Nerve / Cricothyroid Space"],
    "sources": [
        ["Cummings Otolaryngology 7e: Management of thyroid neoplasms", ""],
        ["Randolph GW. Surgery of the Thyroid and Parathyroid Glands, 3e", ""],
        ["International Neural Monitoring Study Group guidelines (Randolph et al., Laryngoscope 2011; Schneider et al. 2018)", ""],
        ["ATA 2015 Guidelines for differentiated thyroid cancer", ""]
    ]
}

CASES["parotidectomy"] = {
    "title": "Parotidectomy",
    "region": "Thyroid / Parathyroid / Salivary",
    "summary": "The facial nerve divides the parotid into a superficial and a deep lobe; this is a surgical plane, not a true anatomic lobe. Parotidectomy removes the tumor and a cuff of gland by finding the main nerve trunk at the stylomastoid foramen and lifting gland off the branches, so the safety of the whole case depends on finding the trunk. The retromandibular vein and external carotid artery lie deep to the nerve plane. The great auricular and auriculotemporal nerves account for most sensory and gustatory-sweating (Frey) problems after surgery.",
    "layers": [
        {"step": "Incision and flap", "structures": ["skin", "subcutaneous fat", "SMAS / parotidomasseteric fascia", "great auricular nerve on the SCM (posterior branch)"],
         "note": "Use a modified Blair (preauricular, around the lobule, into a neck crease) or facelift incision. Raise the flap superficial to the parotid fascia, anteriorly to the anterior gland border. The great auricular nerve ascends on the SCM about halfway between the mastoid and the angle of the mandible, and its posterior (lobular) branch can often be kept."},
        {"step": "Posterior gland release", "structures": ["anterior border of SCM", "tragal cartilage", "posterior belly of digastric", "mastoid tip"],
         "note": "Separate the gland from the cartilaginous EAC and the SCM. Expose the posterior belly of digastric toward its mastoid attachment. This opens a triangle in which the trunk is found."},
        {"step": "Facial nerve trunk", "structures": ["tympanomastoid suture", "tragal pointer", "stylomastoid foramen", "styloid process (deep)", "postauricular artery / stylomastoid artery branch (bleeds just superficial to the trunk)"],
         "note": "Spread parallel to the expected nerve direction. The trunk runs anteriorly, inferiorly and laterally from the stylomastoid foramen, crossing lateral to the styloid. A small artery bleeding just above it is a useful warning sign."},
        {"step": "Pes anserinus and divisions", "structures": ["temporofacial (upper) division", "cervicofacial (lower) division", "pes anserinus"],
         "note": "The trunk divides about 1-2 cm after leaving the foramen, usually within the gland behind the posterior mandibular ramus. Tunnel and divide gland tissue superficial to the branch being followed."},
        {"step": "Peripheral branches", "structures": ["frontal (temporal) branch", "zygomatic branch", "buccal branch (parallel to Stensen duct)", "marginal mandibular branch", "cervical branch"],
         "note": "Dissect the branches nearest the tumor first, following them anteriorly and lifting the superficial lobe off the nerve, rather than pulling the nerve out of the gland."},
        {"step": "Deep structures", "structures": ["retromandibular vein (usually deep to the nerve)", "external carotid artery and its terminal branches (superficial temporal, maxillary)", "transverse facial artery", "Stensen duct (anterior border, over the masseter)", "deep lobe and stylomandibular tunnel"],
         "note": "Ligate the RMV branches or Stensen duct only as the resection needs. Deep-lobe tumors pass through the stylomandibular tunnel into the prestyloid parapharyngeal space, giving a dumbbell shape."},
        {"step": "Closure", "structures": ["SMAS / fascia flap", "drain", "sternocleidomastoid flap or graft (optional, for contour or Frey prevention)"],
         "note": "Stimulate the trunk before closing. An SMAS or SCM flap or an acellular dermal barrier reduces Frey syndrome and contour defect."}
    ],
    "landmarks": [
        {"structure": "Facial nerve main trunk", "how_to_find": "Tragal pointer: about 1 cm deep, anterior and inferior to its tip. Tympanomastoid suture: the trunk is about 6-8 mm deep to its outer end. Posterior belly of digastric: the trunk lies at the same depth, just superior to the digastric attachment at the mastoid. Use these together; none is enough alone.", "why": "Antegrade dissection begins at the trunk"},
        {"structure": "Marginal mandibular branch (retrograde)", "how_to_find": "Crosses superficial to the facial artery and vein at the anterior masseter border, where the vessels cross the inferior mandibular border at the antegonial (facial) notch, deep to the platysma", "why": "Retrograde identification when the trunk cannot be reached safely"},
        {"structure": "Buccal branch (retrograde)", "how_to_find": "Runs parallel to Stensen duct, which lies about a fingerbreadth below the zygomatic arch over the masseter", "why": "A reliable anterior retrograde landmark"},
        {"structure": "Frontal branch", "how_to_find": "Crosses the zygomatic arch along Pitanguy line (about 0.5 cm below the tragus to about 1.5 cm above the lateral brow) in the temporoparietal fascia", "why": "Superior limit of flap elevation"},
        {"structure": "Retromandibular vein", "how_to_find": "Runs vertically behind the ramus; the nerve divisions usually cross superficial (lateral) to it", "why": "Guides finding the nerve and marks the superficial-deep lobe division on imaging"},
        {"structure": "Great auricular nerve", "how_to_find": "On the SCM surface about halfway between the mastoid tip and the mandibular angle, heading toward the lobule", "why": "Preserve the posterior branch; it is also a convenient cable graft donor"}
    ],
    "danger": [
        {"structure": "Facial nerve trunk and branches", "where": "Within the parotid at the superficial-deep lobe interface; the trunk lies deep in the posterior gland at the level of the tympanomastoid suture and posterior belly of digastric (its depth from skin varies with gland and soft-tissue thickness)", "protect": "Identify the trunk by multiple landmarks, dissect superficial to the nerve, use a stimulator or monitor, avoid traction and heat, and repair any transection immediately", "injury": "Facial paralysis of the branch territory, eye exposure, oral incompetence"},
        {"structure": "Marginal mandibular branch", "where": "Crossing the facial vessels superficially, deep to the platysma. Anterior to the facial artery it is almost always above the mandibular border. Posterior to the artery it runs below the border in a minority to about half of patients, depending on the series (Dingman and Grabb: about 1 in 5, within about 1 cm); it lies lower with the neck extended and the head turned", "protect": "Hayes Martin maneuver (ligate the facial vein low and reflect it up) or dissect deep to the investing fascia", "injury": "Lower lip depressor weakness"},
        {"structure": "Great auricular nerve", "where": "On the SCM, entering the gland and lobule", "protect": "Keep the posterior branch when oncologically safe", "injury": "Numbness of the lobule and preauricular skin, neuroma"},
        {"structure": "Retromandibular vein and ECA branches", "where": "Deep to the nerve plane", "protect": "Ligate under vision after the nerve is identified; avoid blind clamping", "injury": "Hemorrhage, nerve injury from blind clamping"},
        {"structure": "Tumor capsule (pleomorphic adenoma)", "where": "Thin capsule with pseudopodia, often lying against nerve branches", "protect": "Remove with a cuff of normal parotid, use no enucleation, and avoid rupture", "injury": "Tumor spillage and multinodular recurrence"},
        {"structure": "Auriculotemporal nerve", "where": "Behind the TMJ, running up with the superficial temporal vessels", "protect": "A barrier flap between the gland bed and skin", "injury": "Frey syndrome (gustatory sweating)"}
    ],
    "variants": [
        "Retromandibular vein lateral (superficial) to the facial nerve in a minority",
        "High or early bifurcation of the trunk, or multiple trunks, and many branching patterns with buccal-zygomatic interconnections",
        "Accessory parotid tissue along Stensen duct over the masseter",
        "Deep-lobe tumor extending through the stylomandibular tunnel into the prestyloid parapharyngeal space",
        "Intraparotid lymph nodes (unique among the salivary glands)"
    ],
    "imaging_check": [
        "Superficial versus deep lobe: tumor position relative to the retromandibular vein / facial nerve line",
        "Parapharyngeal (prestyloid) extension and stylomandibular tunnel widening",
        "Malignant features: ill-defined margins, perineural spread along VII to the stylomastoid foramen or along V3",
        "Cervical and intraparotid nodes",
        "Clinically: preoperative facial nerve function, and FNA cytology"
    ],
    "blood_nerve": [
        ["Arterial", "ECA within the gland, dividing into the superficial temporal and maxillary arteries; transverse facial and posterior auricular branches"],
        ["Venous", "Retromandibular vein (superficial temporal plus maxillary veins), dividing into an anterior division to the facial vein and a posterior division to the EJV"],
        ["Sensory", "Great auricular nerve (C2-C3); auriculotemporal nerve (V3)"],
        ["Parasympathetic", "Inferior salivatory nucleus, then IX, Jacobson's nerve, lesser petrosal nerve, otic ganglion, auriculotemporal nerve to the gland"]
    ],
    "pimp": [
        {"q": "What is the first extracranial branch of the facial nerve?", "a": "Posterior auricular nerve, followed by branches to the posterior belly of digastric and the stylohyoid"},
        {"q": "Trace the parotid secretomotor pathway.", "a": "Inferior salivatory nucleus, then IX, Jacobson's (tympanic) nerve, lesser petrosal nerve, otic ganglion, then postganglionic fibres via the auriculotemporal nerve"},
        {"q": "What causes Frey syndrome, and how is it tested?", "a": "Severed parasympathetic fibres regrow into sweat glands of the skin; Minor starch-iodine test"},
        {"q": "Where does Stensen duct open?", "a": "Buccal mucosa opposite the upper second molar, after crossing the masseter and piercing the buccinator"},
        {"q": "Why does the parotid contain lymph nodes?", "a": "It encapsulates late in development, after the lymphatics form, so nodes become trapped within it"},
        {"q": "What is the stylomandibular tunnel?", "a": "The gap between the posterior ramus, the styloid / stylomandibular ligament and the skull base. Deep-lobe tumors pass through it to the parapharyngeal space, forming a dumbbell."},
        {"q": "Name the five main facial nerve branches.", "a": "Temporal (frontal), zygomatic, buccal, marginal mandibular, cervical"},
        {"q": "Which branches have the least redundancy and are most often weak after surgery?", "a": "Frontal and marginal mandibular (few interconnections)"}
    ],
    "atlas_topics": ["Parotid / Facial Nerve Anatomy", "Superficial Face — Vessels / Facial Nerve / SMAS"],
    "sources": [
        ["Cummings Otolaryngology 7e: Benign and malignant neoplasms of the salivary glands; parotidectomy", ""],
        ["Myers EN. Operative Otolaryngology, 2e: Parotidectomy", ""],
        ["Bailey's Head and Neck Surgery-Otolaryngology 5e: Salivary gland surgery", ""],
        ["Pasha & Golub, Clinical Reference Guide 6e: Salivary glands", ""]
    ]
}

CASES["submandibular-gland"] = {
    "title": "Submandibular Gland Excision",
    "region": "Thyroid / Parathyroid / Salivary",
    "summary": "The submandibular gland lies in the digastric (submandibular) triangle and wraps around the free posterior border of the mylohyoid. Its superficial lobe is below the muscle and its deep lobe and duct run above it into the floor of mouth. Three nerves define the operation. The marginal mandibular nerve lies superficial, in the flap. The lingual nerve lies deep and superior, attached to the gland by the submandibular ganglion. The hypoglossal nerve lies deep and inferior on the hyoglossus. The facial artery hooks over the gland and is controlled at two points.",
    "layers": [
        {"step": "Incision and flap", "structures": ["skin crease about 2 fingerbreadths (3-4 cm) below the mandibular border", "platysma", "marginal mandibular branch (deep to platysma, superficial to the investing fascia)"],
         "note": "Incise through the platysma. Raise the flap in the subplatysmal plane, or incise the investing fascia low on the gland and raise it with the flap (subcapsular approach), so the marginal nerve stays protected in the superior flap."},
        {"step": "Superficial gland and facial vein", "structures": ["superficial layer of deep cervical fascia over the gland", "anterior facial vein", "facial artery at the mandibular border", "level IB nodes (perifacial)"],
         "note": "Ligate the facial vein low on the gland and reflect it superiorly with the fascia (Hayes Martin maneuver). This lifts the marginal nerve out of the field. Ligate the distal facial artery as it crosses the mandible if it is not being preserved."},
        {"step": "Inferior and posterior gland", "structures": ["anterior and posterior bellies of digastric", "intermediate tendon", "stylohyoid", "proximal facial artery (posterior gland, deep to the posterior belly)"],
         "note": "Free the gland from the digastric tendon. The proximal facial artery comes from beneath the posterior belly and stylohyoid, grooving the deep gland. Ligate it here as the second pedicle."},
        {"step": "Anterior gland and mylohyoid", "structures": ["mylohyoid (free posterior border)", "nerve to mylohyoid and submental vessels (superficial to the mylohyoid)"],
         "note": "Retract the mylohyoid anteriorly with a right-angle retractor while pulling the gland inferiorly. This exposes the deep lobe, lingual nerve and duct in the space above the mylohyoid."},
        {"step": "Lingual nerve and ganglion", "structures": ["lingual nerve (superior)", "submandibular ganglion", "ganglion branches to the gland"],
         "note": "Inferior traction on the gland pulls the lingual nerve down into a V. Divide the ganglion branches close to the gland, and the nerve springs back up."},
        {"step": "Wharton duct and hypoglossal nerve", "structures": ["Wharton duct", "hypoglossal nerve (inferior, on the hyoglossus)", "ranine veins", "hyoglossus"],
         "note": "The hypoglossal nerve lies deep and inferior to the duct on the hyoglossus, with its accompanying veins, just above and deep to the intermediate digastric tendon (the tendon is the lower border of Pirogoff triangle and XII the upper). Divide the duct as far anteriorly as needed (fully for stone disease) only after the lingual and hypoglossal nerves are identified."},
        {"step": "Removal and closure", "structures": ["gland bed", "lingual nerve", "XII", "facial artery stumps"],
         "note": "Check the nerves and ligatures, use a drain if needed, and close the platysma and skin."}
    ],
    "landmarks": [
        {"structure": "Marginal mandibular branch", "how_to_find": "Deep to the platysma over the gland's fascia, crossing the facial vessels superficially near the mandibular border. Incise low and use the Hayes Martin maneuver.", "why": "The nerve at greatest risk in this exposure"},
        {"structure": "Facial artery", "how_to_find": "Distal: hooks over the mandible at the anterior masseter border. Proximal: emerges deep to the posterior belly of digastric and stylohyoid, grooving the posterior gland.", "why": "Two separate ligation points"},
        {"structure": "Lingual nerve", "how_to_find": "Retract the mylohyoid anteriorly and pull the gland down. The nerve is the flat band dragged into a V above the gland by the submandibular ganglion.", "why": "Divide the ganglion, not the nerve"},
        {"structure": "Hypoglossal nerve", "how_to_find": "On the hyoglossus below the duct, just above and deep to the intermediate digastric tendon, with the ranine veins; keep the plane superficial to the fascia over the hyoglossus", "why": "Must be seen before dividing the duct or deep tissue"},
        {"structure": "Wharton duct", "how_to_find": "Leaves the deep lobe and runs anteriorly above the mylohyoid between the hyoglossus and mylohyoid; the lingual nerve crosses it", "why": "Ligate after identifying both nerves"},
        {"structure": "Pirogoff (lingual) triangle", "how_to_find": "Bounded by the intermediate digastric tendon, the posterior border of the mylohyoid and the hypoglossal nerve; the lingual artery is deep to the hyoglossus here", "why": "Locates the lingual artery if there is bleeding"}
    ],
    "danger": [
        {"structure": "Marginal mandibular branch", "where": "Deep to the platysma, superficial to the gland fascia, usually above the mandibular border but can lie below it, especially posterior to the facial artery", "protect": "Low incision, subfascial or Hayes Martin elevation, and no cautery in the superior flap", "injury": "Lower lip depressor weakness and asymmetric smile"},
        {"structure": "Lingual nerve", "where": "Above the deep lobe, joined to the gland by the submandibular ganglion; crosses the duct", "protect": "Divide ganglion branches next to the gland and identify the nerve before cutting the duct", "injury": "Ipsilateral tongue numbness and loss of taste (anterior two-thirds), tongue biting"},
        {"structure": "Hypoglossal nerve", "where": "Deep and inferior on the hyoglossus, below the duct and just above / deep to the intermediate digastric tendon", "protect": "Stay superficial to the hyoglossus fascia and use bipolar only near the ranine veins", "injury": "Ipsilateral tongue weakness, deviation toward the injured side"},
        {"structure": "Facial artery and vein", "where": "Distal at the mandible; proximal deep to the posterior digastric", "protect": "Ligate securely at both points", "injury": "Hematoma, airway compromise"}
    ],
    "variants": [
        "Marginal mandibular branch running below the mandible (more common posteriorly and in older patients), or present as multiple branches",
        "Facial artery passing through the gland rather than in a groove",
        "Large deep lobe extending far into the floor of mouth",
        "Accessory or duplicated duct; communication with the sublingual gland (Bartholin duct)",
        "Mylohyoid dehiscence (route for a plunging ranula)"
    ],
    "imaging_check": [
        "Stone location (hilar or proximal versus distal duct); distal stones may be removed transorally and spare the gland",
        "Mass versus inflammatory gland, and malignancy features",
        "Level IB node involvement and relation to the mandible and floor of mouth",
        "Clinically: bimanual palpation, and baseline marginal, lingual and XII function"
    ],
    "blood_nerve": [
        ["Arterial", "Facial artery (main) with its submental branch; sublingual branch of the lingual artery"],
        ["Venous", "Anterior facial vein to the common facial vein to the IJV"],
        ["Parasympathetic", "Superior salivatory nucleus, then nervus intermedius, chorda tympani, lingual nerve, submandibular ganglion to the gland"],
        ["Neighbouring nerves", "Marginal mandibular (VII) superficial; lingual (V3) deep and superior; hypoglossal (XII) deep and inferior; nerve to mylohyoid superficial to the mylohyoid"]
    ],
    "pimp": [
        {"q": "Boundaries of the submandibular triangle?", "a": "Anterior and posterior bellies of digastric and the inferior border of the mandible"},
        {"q": "Describe the lingual nerve and duct relationship.", "a": "The lingual nerve starts lateral to the duct, loops under it, and ends medial to it (the double crossing)"},
        {"q": "What lies superficial and deep to the hyoglossus?", "a": "Superficial: XII, the duct and the lingual nerve. Deep: the lingual artery."},
        {"q": "Boundaries of Pirogoff triangle?", "a": "Intermediate digastric tendon, posterior border of the mylohyoid and the hypoglossal nerve; the floor is the hyoglossus, with the lingual artery deep"},
        {"q": "Why are stones more common in the submandibular gland?", "a": "More alkaline, mucin-rich, calcium-rich saliva, and a long duct that runs upward against gravity"},
        {"q": "Trace the submandibular secretomotor pathway.", "a": "Superior salivatory nucleus, nervus intermedius, chorda tympani, lingual nerve, submandibular ganglion"},
        {"q": "What does the marginal mandibular nerve innervate?", "a": "Depressor anguli oris, depressor labii inferioris and mentalis"},
        {"q": "Where does Wharton duct open?", "a": "Sublingual caruncle beside the lingual frenulum"}
    ],
    "atlas_topics": ["Submandibular Triangle / Floor of Mouth", "Superficial Face — Vessels / Facial Nerve / SMAS", "Oral Tongue / Floor of Mouth"],
    "sources": [
        ["Cummings Otolaryngology 7e: Inflammatory disorders and neoplasms of the salivary glands", ""],
        ["Myers EN. Operative Otolaryngology, 2e: Submandibular gland excision", ""],
        ["Bailey's Head and Neck Surgery-Otolaryngology 5e: Salivary gland surgery", ""]
    ]
}

CASES["sialendoscopy"] = {
    "title": "Sialendoscopy",
    "region": "Thyroid / Parathyroid / Salivary",
    "summary": "Sialendoscopy treats obstruction (stones, stenosis, mucus plugs) from inside the duct. The papilla is the narrowest point. The Wharton duct runs upward and back around the mylohyoid to the hilum, with the lingual nerve crossing beneath it in the floor of mouth. The Stensen duct turns sharply at the anterior masseter border where it pierces the buccinator. Knowing these bends and the lingual nerve relationship prevents false passage, perforation, and nerve injury during combined transoral removal.",
    "layers": [
        {"step": "Papilla", "structures": ["Wharton papilla on the sublingual caruncle beside the frenulum", "Stensen papilla on the buccal mucosa opposite the upper second molar"],
         "note": "The papilla is the tightest point. Dilate gradually with lacrimal probes and dilators, or do a limited papillotomy. Massaging the gland to express saliva helps find the opening."},
        {"step": "Distal duct", "structures": ["distal Wharton duct beneath the sublingual fold", "sublingual gland and its ducts (superficial / lateral)", "buccinator and masseter for Stensen"],
         "note": "Advance with continuous irrigation, keeping the lumen centered. Stensen has a sharp bend at the anterior masseter border; pulling the cheek forward and outward straightens it."},
        {"step": "Mid duct and nerve crossing", "structures": ["Wharton duct over the hyoglossus", "lingual nerve looping beneath the duct (lateral to medial), around the second and third molar region"],
         "note": "This is the zone where a transoral duct incision for stone removal is made. Open the duct directly over the stone, which is easiest anterior to where the lingual nerve crosses."},
        {"step": "Hilum / genu", "structures": ["Wharton duct bend around the posterior free border of the mylohyoid", "hilum of the submandibular gland", "parotid hilum and intraglandular branches"],
         "note": "The genu at the hilum is a common place for stones to lodge and is hard to pass. Hilar stones may need a combined transoral approach with lingual nerve identification."},
        {"step": "Intraglandular branches", "structures": ["primary and secondary ductal branches"],
         "note": "Survey the branch points for stones, plugs and stenosis. Current scopes usually reach first-order and second-order branches, and sometimes third-order branches, depending on scope size and duct caliber."},
        {"step": "Treatment and stenting", "structures": ["stone basket", "laser or pneumatic fragmentation", "duct stent at the papilla"],
         "note": "Pass the basket beyond the stone, close it, and withdraw under vision. Fragment stones too large to pass the papilla or duct. Place a stent after ductotomy or for stenosis."}
    ],
    "landmarks": [
        {"structure": "Wharton papilla", "how_to_find": "On the sublingual caruncle just lateral to the lingual frenulum; dry the area and massage the gland to see saliva", "why": "Entry point; easily torn by forced entry"},
        {"structure": "Stensen papilla", "how_to_find": "Buccal mucosa opposite the upper second molar, sometimes on a small fold; express by pressing the parotid", "why": "Entry point"},
        {"structure": "Stensen bend", "how_to_find": "At the anterior masseter border where the duct turns medially through the buccinator; pull the cheek forward to straighten the path", "why": "Common site of false passage"},
        {"structure": "Lingual nerve in the floor of mouth", "how_to_find": "Runs under the Wharton duct from lateral to medial around the second and third molar region, just above the mylohyoid. In a combined approach, see it posterior in the incision before deep dissection.", "why": "Protect during transoral stone removal"},
        {"structure": "Submandibular hilum", "how_to_find": "Where the duct bends around the posterior free border of the mylohyoid; palpate bimanually", "why": "Common stone site and where the duct is hardest to pass"}
    ],
    "danger": [
        {"structure": "Duct wall", "where": "Papilla, Stensen bend, Wharton genu", "protect": "Gradual dilation, irrigation, keeping the lumen centered, and no forcing", "injury": "Perforation, false passage, extravasation, later stenosis"},
        {"structure": "Lingual nerve", "where": "Under the Wharton duct in the floor of mouth during a transoral incision", "protect": "Incise the mucosa directly over the duct and stone, and identify the nerve posteriorly before deep dissection", "injury": "Tongue numbness and loss of taste"},
        {"structure": "Basket entrapment", "where": "Stone captured in a narrow segment, often at the papilla or bend", "protect": "Capture only stones that can pass the narrowest point; fragment first", "injury": "Impaction needing open removal"},
        {"structure": "Sublingual gland", "where": "Lateral to the distal Wharton duct", "protect": "Gentle dissection in transoral approaches", "injury": "Ranula"},
        {"structure": "Facial nerve buccal branch / Stensen duct (combined parotid approach)", "where": "Running together over the masseter", "protect": "Identify the buccal branch when external access is used", "injury": "Buccal branch weakness, salivary fistula"}
    ],
    "variants": [
        "Papillary or ductal stenosis (in parotid disease, often radioiodine-related or inflammatory)",
        "Wharton duct opening in common with the sublingual (Bartholin) duct",
        "Accessory parotid gland duct joining Stensen over the masseter",
        "Megaduct or dilated duct proximal to a stricture",
        "Juvenile recurrent parotitis with a sialectatic duct system"
    ],
    "imaging_check": [
        "Ultrasound: stone size, number, location (distal, hilar, intraparenchymal), mobility and proximal dilation",
        "Non-contrast CT for stone size and location when ultrasound is equivocal",
        "MR sialography or ultrasound for stenosis length and site",
        "Size thresholds for basket retrieval versus fragmentation versus combined approach vary by gland and center (smaller for the parotid than the submandibular)",
        "Clinically: bimanual palpation, papilla appearance and saliva quality"
    ],
    "blood_nerve": [
        ["Sensory", "Lingual nerve (V3) to the floor of mouth; buccal nerve (V3) to the buccal mucosa"],
        ["Parasympathetic", "Submandibular: chorda tympani through the lingual nerve to the submandibular ganglion. Parotid: lesser petrosal nerve through the otic ganglion and auriculotemporal nerve."],
        ["Arterial", "Sublingual (lingual artery) and submental (facial artery) in the floor of mouth; transverse facial artery along Stensen"]
    ],
    "pimp": [
        {"q": "Where does Stensen duct open, and what does it pierce?", "a": "Opposite the upper second molar, after crossing the masseter and piercing the buccinator"},
        {"q": "Which gland forms most salivary stones?", "a": "Submandibular, in the large majority (roughly 80-90%)"},
        {"q": "Relationship of the lingual nerve to Wharton duct?", "a": "Starts lateral, passes under the duct, and ends medial to it"},
        {"q": "Where do submandibular stones most commonly lodge?", "a": "At the hilum / genu where the duct bends around the posterior border of the mylohyoid, and in the distal duct"},
        {"q": "What is the narrowest point of the salivary ducts?", "a": "The papilla"},
        {"q": "What is a plunging ranula?", "a": "A sublingual gland mucus extravasation cyst extending into the neck through or around the mylohyoid"},
        {"q": "Which ducts drain the sublingual gland?", "a": "Multiple small ducts of Rivinus on the plica sublingualis, and sometimes a larger Bartholin duct joining Wharton"}
    ],
    "atlas_topics": ["Submandibular Triangle / Floor of Mouth", "Parotid / Facial Nerve Anatomy", "Oral Tongue / Floor of Mouth"],
    "sources": [
        ["Cummings Otolaryngology 7e: Sialendoscopy / salivary gland obstructive disease", ""],
        ["Marchal F, et al. Sialendoscopy (atlas / technique literature)", ""],
        ["Bailey's Head and Neck Surgery-Otolaryngology 5e: Salivary gland disorders", ""]
    ]
}
