"""ENT Mastery v44.6 -- resident-requested safety-content gaps + a Deep Curriculum
readability pilot.

Four things, all grounded in the resident's own attached screenshots and requests
(no new clinical claims beyond what standard ENT/allergy teaching already supports):

1. DEEP CURRICULUM READABILITY PILOT -- "Laryngeal Fracture / External Laryngeal
   Trauma" (Facial Plastics / Trauma) was the resident's own example of a dense,
   wall-of-text topic. Rewritten into short bolded-label sentences (every clinical
   fact preserved, none added) so the existing per-sentence bullet renderer in
   templates/curriculum_depth.html actually produces short, scannable bullets
   instead of a few giant ones. This is a pilot for the same treatment across the
   rest of the 356-topic curriculum, not a claim that the whole curriculum has
   been redone.

2. ALLERGY TESTING -- adds intradermal (dilutional) skin testing technique and
   positive-test criteria, and explicit SPT positive-test criteria, to "Allergy
   Testing & Interpretation" (Rhinology / Allergy / Skull Base), which previously
   only discussed skin-prick testing and serum specific-IgE at a policy level
   without technique/positive-criteria detail for either modality.

3. RETROBULBAR HEMATOMA / AEA -- adds explicit "retrobulbar hematoma" terminology
   and the specific point that embolization is NOT indicated for an injured
   anterior ethmoidal artery (branch of the ophthalmic artery off the internal
   carotid -> blindness/stroke risk; treat with immediate lateral canthotomy and
   cantholysis instead) to the "Ethmoidectomy" Deep Curriculum topic and to the
   endoscopic-sinus-surgery and frontal-sinus-trauma OR-prep cards. Both cards
   already discussed the AEA and orbital emergency response; neither used the term
   "retrobulbar hematoma" or the embolization-contraindication point explicitly.

4. OR-PREP ANTIBIOTIC PROPHYLAXIS -- OR_PREP_REGISTRY had no antibiotics field at
   all across any of its 95 cards. Adds one, grounded in general surgical
   antibiotic-prophylaxis principles (ASHP/IDSA/SHEA/SIS surgical prophylaxis
   guidance; the AAO-HNS Clinical Practice Guideline: Tonsillectomy in Children for
   the explicit "not routinely indicated" pediatric-tonsil recommendation) and
   standard facial-trauma/mucosal-entry teaching. This is categorical, board-level
   teaching -- not a substitute for institutional protocol or attending preference,
   which the rendered text says explicitly.
"""

from copy import deepcopy


# ---------------------------------------------------------------------------
# 1. Deep Curriculum readability pilot: Laryngeal Fracture / External Laryngeal
#    Trauma (Facial Plastics / Trauma). Every clinical fact below already existed
#    in the topic; only the structure (short sentences, bolded labels) changed.
# ---------------------------------------------------------------------------

LARYNGEAL_TRAUMA_DOMAIN = "Facial Plastics / Trauma"
LARYNGEAL_TRAUMA_TOPIC = "Laryngeal Fracture / External Laryngeal Trauma"

LARYNGEAL_TRAUMA_FIELDS = {
    "recognize": (
        "**Mechanism**: anterior-neck impact (dashboard, sports collision, clothesline, "
        "assault/strangulation) or penetrating trauma. "
        "**Red flags**: new dysphonia, odynophagia/dysphagia, hemoptysis, dyspnea, neck "
        "tenderness/crepitus, subcutaneous emphysema, a flattened thyroid prominence, or a "
        "palpable step-off. "
        "**Key trap**: symptom severity does NOT reliably grade structural injury -- a patient "
        "speaking calmly can still develop airway-threatening edema over hours. "
        "**Act now if**: stridor, progressive dyspnea, expanding hematoma, inability to handle "
        "secretions, major emphysema, or gross distortion -- this mandates an immediately "
        "coordinated airway plan, not a trip to CT first. "
        "Assess for cervical spine injury, carotid/jugular trauma, and pharyngoesophageal "
        "perforation as part of multidisciplinary trauma care. "
        "**Pediatric note**: children have a higher, more flexible, less ossified larynx -- this "
        "lowers obvious fracture frequency but does NOT exclude serious mucosal injury. "
        "A normal-appearing external neck is not a rule-out test."
    ),
    "localize": (
        "Map the injury by level: **supraglottic** (epiglottis, aryepiglottic structures), "
        "**glottic** (thyroid laminae, true folds, anterior commissure, arytenoids, "
        "cricoarytenoid joints), and **subglottic/cricoid-tracheal**. "
        "**Key anatomy**: the cricoid is a complete ring, so a fracture or hematoma there can "
        "critically narrow the only airway. "
        "**Schaefer-Fuhrman grading**: "
        "**I** = minor mucosal edema/hematoma/laceration without significant structural "
        "disruption. "
        "**II** = greater edema/hematoma or minor mucosal injury, possibly a stable "
        "nondisplaced fracture, no exposed cartilage. "
        "**III** = massive edema, exposed cartilage, substantial laceration, displaced "
        "fracture, or fold immobility. "
        "**IV** = severe unstable framework, multiple displaced fractures, major mucosal "
        "disruption, or anterior-commissure avulsion. "
        "**V** = complete laryngotracheal separation. "
        "Grade using BOTH endoscopy and CT findings -- not radiology alone. "
        "Differentiate vocal fold immobility from arytenoid dislocation/cricoarytenoid "
        "fixation versus RLN injury. "
        "Document the anterior commissure and mucosal coverage -- malrepair here causes "
        "web/stenosis or dysphonia."
    ),
    "workup": (
        "**Airway first**: assess airway, breathing, and circulation with cervical-spine "
        "precautions and senior ENT/anesthesia/trauma support. "
        "An unstable or rapidly deteriorating airway should be secured by the team using the "
        "safest method BEFORE imaging -- a controlled awake tracheostomy below the injury is "
        "often favored for clear major framework disruption. "
        "**If stable and cooperative**: flexible nasolaryngoscopy assesses edema, blood, "
        "airway caliber, exposed cartilage, mucosal tears, and bilateral vocal fold motion; a "
        "seemingly mild scope exam can still miss a framework fracture. "
        "**Imaging**: CT neck with thin cuts and multiplanar laryngeal reconstruction defines "
        "displaced/nondisplaced thyroid/cricoid fractures once safe to image -- do not impose "
        "a 24-hour wait or image a threatened airway. "
        "Add **CTA neck** when mechanism or findings suggest vascular injury, and evaluate the "
        "cervical spine. "
        "**Suspect esophageal injury** if there is a deep laceration, air near the esophagus, "
        "swallowing symptoms, or a penetrating trajectory -- arrange esophagoscopy and/or "
        "contrast swallow. "
        "After airway control, direct laryngoscopy/bronchoscopy with arytenoid palpation (and "
        "esophagoscopy as appropriate) delineates the full extent for repair. "
        "**Monitor**: serial bedside airway and flexible-endoscopic checks in monitored care "
        "are essential even in conservatively treated injury -- typically at least 24 hours."
    ),
    "manage": (
        "**Airway first.** Do not attempt routine blind rapid-sequence intubation across a "
        "suspected severe disruption -- it can create a false passage or complete separation. "
        "Choice among controlled fiberoptic intubation with immediate surgical backup, versus "
        "awake/local tracheostomy, depends on anatomy, stability, expertise, and associated "
        "injuries. With a clearly unstable framework or major separation, secure a surgical "
        "airway below the injury when feasible. "
        "**Group I and selected stable II** (intact mucosa, no significant displacement or "
        "airway compromise) generally receive monitored admission, head elevation, "
        "humidification, voice rest, analgesia, a swallowing assessment, and serial endoscopy. "
        "Steroids/antireflux therapy are adjuncts with variable evidence -- not substitutes for "
        "airway vigilance. A group II patient with concerning mucosal/fracture findings can "
        "still require direct endoscopy or exploration. "
        "**Operate on**: displaced fractures, exposed cartilage, large mucosal lacerations, "
        "anterior-commissure disruption, cricoarytenoid injury, persistent immobility, unstable "
        "airway, or progressive emphysema -- all require prompt operative assessment/repair. "
        "**Timing correction (common teaching error)**: expeditious repair is preferred when "
        "clinically feasible. Operative Otolaryngology recommends exploration within "
        "**24-48 hours**, and Pasha describes repair ideally within **2-3 days** after "
        "stabilization. A published mean of **5.6 days (range 3-10)** must NOT be misread as a "
        "required delay. Address immediately life-threatening injuries first, and individualize "
        "timing."
    ),
    "operate": (
        "After a secure airway below any major disruption and associated trauma/cervical-spine "
        "planning, perform direct laryngoscopy plus bronchoscopy (and esophagoscopy if "
        "indicated) to map mucosal breaks, exposed cartilage, fold mobility, arytenoid joint "
        "integrity, anterior commissure, and cricotracheal continuity. "
        "**For displaced thyroid/cricoid fracture or major soft-tissue disruption**: expose "
        "through a suitable cervical incision; preserve perichondrium and blood supply; gently "
        "reduce cartilage to anatomic contour; fix with miniplates/sutures or tailored mesh "
        "where necessary; repair mucosal lacerations to cover cartilage; restore "
        "anterior-commissure attachment; address arytenoid dislocation or vocal-fold avulsion. "
        "**Stenting/keel is SELECTIVE** -- for unstable comminution, extensive mucosal loss, or "
        "commissure disruption -- not automatic for every fracture; weigh the risk of "
        "granulation and later removal. "
        "**Complete laryngotracheal separation is an airway catastrophe**: identify the distal "
        "trachea for secure ventilation first, then reconstruct continuity once stabilized; "
        "coordinate with trauma/thoracic teams and assess for RLN and esophageal injury. "
        "**Exit checklist**: patent secure airway/trach, intact mucosal cover, restored "
        "framework and commissure, no unrecognized esophageal or vascular injury, a "
        "feeding/aspiration plan, and staged repeat-endoscopy/stent follow-up. "
        "**Early complications**: airway edema, infection, hematoma, mucosal breakdown. "
        "**Late complications**: glottic/subglottic stenosis, web, dysphonia, "
        "dysphagia/aspiration, vocal fold immobility, decannulation failure."
    ),
    "teach": (
        "**Board algorithm**: suspect after anterior neck trauma plus a voice, breathing, or "
        "swallowing change. Do airway/C-spine evaluation BEFORE CT. If stable: flexible scope "
        "and CT framework mapping. If the airway is threatened or separation is suspected: "
        "expert controlled airway, usually surgical, below the disruption. Then classify with "
        "**Schaefer-Fuhrman I-V**. "
        "**Minor stable I / selected II**: observe with serial scope for at least 24 hours. "
        "**Major mucosal/cartilage instability or group III-V**: early operative evaluation -- "
        "reconstruct cartilage, restore mucosa and anterior commissure, consider a stent only "
        "when needed. "
        "**Common teaching error to correct**: early reconstruction when safe (often within "
        "24-48 hours) is favored -- never teach waiting 3-10 days as the optimal standard. "
        "**The most important discriminator** is exposed cartilage, displacement, commissure "
        "injury, or airway instability -- not isolated hoarseness. "
        "**Attendings may ask**: why a normal CT does not rule out mucosal injury; how to "
        "recognize arytenoid dislocation versus nerve paralysis; why cricoid injury threatens "
        "circumferential airway caliber; what short- and long-term evaluations are needed to "
        "preserve breathing, swallowing, and voice."
    ),
}


# ---------------------------------------------------------------------------
# 2. Allergy Testing & Interpretation -- intradermal + SPT positive-criteria detail.
# ---------------------------------------------------------------------------

ALLERGY_DOMAIN = "Rhinology / Allergy / Skull Base"
ALLERGY_TOPIC = "Allergy Testing & Interpretation"

ALLERGY_WORKUP = (
    "Choose **skin-prick testing (SPT)** or **serum allergen-specific IgE** selectively. "
    "Skin testing provides rapid in-vivo assessment but requires interpretable controls and "
    "consideration of medications/skin disease that can blunt results. Serum specific-IgE is "
    "useful when skin testing is unsafe, impractical, or uninterpretable. Interpret either test "
    "against the clinical exposure history. Avoid indiscriminate inhalant or food panels, and "
    "do not use total IgE or eosinophil counts as substitute culprit-allergen tests. When "
    "systemic tests are negative despite a compelling localized allergen history, consider "
    "specialist evaluation for local allergic rhinitis rather than simply labeling the patient "
    "nonallergic.\n\n"
    "**SPT technique and positive criteria**: apply a drop of allergen extract and prick "
    "through it into the epidermis, always alongside a **histamine positive control** and a "
    "**saline/diluent negative control**. Read at **15-20 minutes**. A **positive SPT** is a "
    "wheal **at least 3 mm larger than the negative control**, typically with surrounding "
    "erythema/flare; a negative histamine control invalidates the test (antihistamine effect "
    "or technique failure).\n\n"
    "**Intradermal (dilutional) testing**: more sensitive than SPT but less specific, with a "
    "higher false-positive and systemic-reaction rate -- reserve it for inhalant allergens "
    "with a negative or equivocal SPT plus a compelling history, and avoid it for food "
    "allergens given the anaphylaxis risk. **Technique**: inject a small volume (about "
    "0.01-0.02 mL) intradermally at a validated, nonirritating allergen-specific dilution "
    "under a specialist protocol, producing a small bleb; step up in concentration only "
    "according to that protocol. **Interpretation**: read the wheal and flare at about "
    "15 minutes against a diluent control; dilutional end-point protocols often use "
    "approximately 2 mm wheal growth over the initial bleb with erythema, but a response "
    "at an irritant concentration or without matching exposure symptoms does not establish "
    "clinical allergy. **Skin end-point titration (SET)** estimates a response threshold "
    "across dilutions; it is not a universal immunotherapy starting dose. **Safety**: because of "
    "the higher systemic-reaction risk, perform intradermal testing only where epinephrine and "
    "resuscitation equipment are immediately available, and observe the patient afterward."
)


# ---------------------------------------------------------------------------
# 3. Retrobulbar hematoma / AEA -- Ethmoidectomy topic + two OR-prep cards.
# ---------------------------------------------------------------------------

ETHMOIDECTOMY_DOMAIN = "Rhinology / Allergy / Skull Base"
ETHMOIDECTOMY_TOPIC = "Ethmoidectomy"

ETHMOIDECTOMY_OPERATE = (
    "**Indication**: ethmoid sinus disease (chronic rhinosinusitis with or without polyps, "
    "access for further posterior procedures) requiring surgical clearance. "
    "**Setup**: proceed systematically from anterior to posterior ethmoid, keeping the lamina "
    "papyracea and skull base continuously in view. "
    "**Key steps**: open cells working medially away from the lamina papyracea; identify the "
    "basal lamella and cross it deliberately (not by blunt instrumentation) to enter the "
    "posterior ethmoid; follow the skull base posteriorly toward the sphenoid face. "
    "**Danger structures**: lamina papyracea (orbit) laterally; fovea ethmoidalis/cribriform "
    "plate (skull base and CSF) superiorly and medially; the anterior ethmoidal artery (AEA), "
    "which can retract into the orbit if transected. "
    "**Retrobulbar hematoma**: this is the feared consequence of a transected/retracted AEA -- "
    "rapidly rising orbital pressure threatens the optic nerve and can cause permanent vision "
    "loss within minutes to hours if untreated. "
    "**Do NOT embolize the AEA**: it is a branch of the ophthalmic artery off the internal "
    "carotid, so endovascular embolization there risks blindness and/or stroke. A retrobulbar "
    "hematoma is a surgical emergency managed with immediate **lateral canthotomy and "
    "cantholysis** (+/- orbital decompression) -- not interventional radiology. "
    "**Failure mode**: continuing dissection after encountering orbital fat or clear fluid "
    "(CSF) rather than stopping immediately. Either finding means stop, identify the injury "
    "precisely, and manage it deliberately -- orbital fat: stop lateral dissection and inspect "
    "for hematoma; CSF: prepare for skull-base repair -- rather than pressing forward. "
    "**Postoperative plan**: endoscopic debridement to prevent adhesion/scarring between raw "
    "mucosal surfaces, and saline irrigation during healing."
)

ETHMOIDECTOMY_TEACH = (
    "Orbital fat or CSF means stop, identify the injury, and manage it deliberately. "
    "**Board pearl**: if the orbit balloons/proptoses intraoperatively or in recovery after "
    "ethmoid or frontal sinus work, think **retrobulbar hematoma from AEA injury** -- check "
    "for proptosis, a tense globe, a relative afferent pupillary defect, and rising "
    "intraocular pressure. **Treat immediately with lateral canthotomy/cantholysis** (+/- "
    "orbital decompression); vision loss is time-dependent. **Do not send the patient for "
    "embolization** -- the AEA's origin from the ophthalmic artery makes embolization a "
    "stroke/blindness risk, and it does nothing to relieve the orbital compartment pressure "
    "that is actually threatening the eye."
)

_RETROBULBAR_MARKER = "retrobulbar hematoma"

ESS_DANGER_ADDITION = (
    "Anterior ethmoidal artery injury -> retrobulbar hematoma: a surgical emergency (immediate "
    "lateral canthotomy/cantholysis +/- orbital decompression) -- do NOT embolize the AEA, "
    "it is a branch of the ophthalmic artery off the internal carotid and embolization there "
    "risks blindness and/or stroke."
)

ESS_FOLLOWUP_QA = (
    "If the AEA retracts into the orbit and there's rapid proptosis afterward, what's the fix?",
    "Retrobulbar hematoma from AEA injury is a surgical emergency: immediate lateral "
    "canthotomy and cantholysis (+/- medial/inferior orbital decompression) to relieve "
    "pressure on the optic nerve before permanent vision loss occurs. Do not wait for or "
    "pursue endovascular embolization -- the AEA is a branch of the ophthalmic artery off the "
    "internal carotid, so embolization there risks blindness and/or stroke. Open surgical "
    "decompression is the answer, not interventional radiology.",
)

FST_DANGER_ADDITION = (
    "Anterior ethmoidal artery injury during frontal recess/ethmoid dissection -> retrobulbar "
    "hematoma -- do NOT embolize (risks blindness/stroke; the AEA is an ophthalmic-artery "
    "branch off the internal carotid); treat with immediate lateral canthotomy/cantholysis."
)

FST_FOLLOWUP_QA = (
    "During frontal sinus/frontal recess work the orbit suddenly tenses and the eye proptoses -- "
    "what do you do?",
    "Treat this as a retrobulbar hematoma, most often from anterior ethmoidal artery injury "
    "during ethmoid/frontal recess dissection, until proven otherwise. Perform an immediate "
    "lateral canthotomy and cantholysis (+/- orbital decompression) to protect the optic "
    "nerve -- do not delay for imaging or consult interventional radiology for embolization. "
    "The AEA is a branch of the ophthalmic artery off the internal carotid, so attempted "
    "embolization there carries a real risk of blindness and/or stroke and does not relieve "
    "the orbital compartment pressure that threatens vision.",
)


# ---------------------------------------------------------------------------
# 4. OR-prep antibiotic prophylaxis field -- categorical defaults + per-slug map.
# ---------------------------------------------------------------------------

_CAVEAT = (
    " Reflects general teaching (ASHP/IDSA/SHEA/SIS surgical antibiotic-prophylaxis principles "
    "and procedure-specific literature), not a fixed rule -- confirm against current "
    "institutional protocol and attending preference."
)

ANTIBIOTIC_CATEGORIES = {
    "CLEAN_NO_IMPLANT": {
        "indicated": "Not routinely indicated",
        "regimen": (
            "No preoperative antibiotic is required for this clean procedure without an "
            "implant, prosthesis, or mucosal entry."
        ),
        "rationale": (
            "Clean procedures without prosthetic material or entry into a contaminated space "
            "do not benefit from prophylaxis; reserve antibiotics for a specific patient risk "
            "factor, not routine use." + _CAVEAT
        ),
    },
    "CLEAN_IMPLANT": {
        "indicated": "Selective -- a single preop dose is reasonable",
        "regimen": (
            "A single weight-based preoperative IV dose (commonly a first-generation "
            "cephalosporin such as cefazolin; clindamycin or vancomycin when appropriate "
            "for a serious beta-lactam allergy) covering skin flora. Start most agents "
            "within 60 minutes of incision; allow up to 120 minutes for vancomycin infusion."
        ),
        "rationale": (
            "Implant/prosthesis-containing cases are often treated as an exception to the "
            "'clean = no prophylaxis' rule because of the consequences of a prosthesis "
            "infection, even though high-quality trial evidence specific to each device is "
            "limited." + _CAVEAT
        ),
    },
    "NASAL_SINUS_CLEAN": {
        "indicated": "Not routinely indicated",
        "regimen": (
            "No routine preoperative antibiotic for this nasal/sinus procedure. If "
            "non-absorbable packing is left in place, follow institutional protocol for "
            "coverage during the packing period."
        ),
        "rationale": (
            "Evidence does not support routine perioperative antibiotics for septal or "
            "endoscopic sinus surgery; any use is typically tied to a specific "
            "nonabsorbable-packing practice, not the surgery itself." + _CAVEAT
        ),
    },
    "SKULL_BASE_CSF": {
        "indicated": "Selective -- a single preop dose is reasonable",
        "regimen": (
            "A single preoperative IV dose (commonly a first-generation cephalosporin, or "
            "coverage per institutional protocol) when entering the mastoid, middle ear, or a "
            "CSF-exposed field."
        ),
        "rationale": (
            "Common practice for neurotologic/lateral- and anterior-skull-base approaches that "
            "cross mastoid air cells or expose the subarachnoid space, though the evidence base "
            "is smaller than for other surgical categories." + _CAVEAT
        ),
    },
    "THYROID_PARA_CLEAN": {
        "indicated": "Not routinely indicated",
        "regimen": "No preoperative antibiotic required for this clean neck procedure.",
        "rationale": (
            "Thyroidectomy and parathyroidectomy are clean procedures without mucosal entry; "
            "prophylactic antibiotics are not supported by evidence and are not routinely "
            "given." + _CAVEAT
        ),
    },
    "CLEAN_CONTAMINATED_MUCOSAL": {
        "indicated": "Indicated for major mucosal surgery",
        "regimen": (
            "A single preoperative IV dose covering oral/pharyngeal flora (ampicillin-"
            "sulbactam is a common first-line choice; clindamycin, sometimes plus an agent with "
            "gram-negative coverage, if penicillin-allergic); redose intraoperatively for a "
            "long case or high blood loss per weight/half-life-based rules."
        ),
        "rationale": (
            "Any case entering the oral cavity, pharynx, larynx, or aerodigestive-tract mucosa "
            "is clean-contaminated. Surgical-prophylaxis guidance supports perioperative "
            "antibiotics here, sometimes continued for the first 24 hours in major "
            "head-and-neck cancer/free-flap cases (duration varies by institution)." + _CAVEAT
        ),
    },
    "FACIAL_TRAUMA_MUCOSAL": {
        "indicated": "Indicated when the fracture or approach enters mucosa or a sinus",
        "regimen": (
            "Preoperative IV antibiotic covering relevant oral or sinonasal flora when the "
            "fracture or operative approach enters the oral cavity or paranasal sinuses "
            "(agent selected by local protocol and allergy history); "
            "do not default to extending it for the full admission without a specific "
            "indication."
        ),
        "rationale": (
            "Facial-trauma literature most consistently supports perioperative prophylaxis for "
            "fractures approached through oral mucosa or communicating with the oral "
            "cavity/sinuses (e.g., mandible, some ZMC/NOE fractures); clean fractures without "
            "mucosal communication do not require it." + _CAVEAT
        ),
    },
    "ENDOSCOPIC_NO_INCISION": {
        "indicated": "Not routinely indicated",
        "regimen": (
            "No routine prophylactic antibiotics for uncomplicated diagnostic airway "
            "instrumentation or limited transoral/endoscopic mucosal work; reassess when "
            "there is established infection, perforation, or extensive reconstruction."
        ),
        "rationale": (
            "Brief endoscopic procedures and limited microlaryngeal work generally do not "
            "need routine prophylaxis; endoscopic access alone does not determine whether "
            "an operative wound needs coverage." + _CAVEAT
        ),
    },
    "PEDIATRIC_TONSIL": {
        "indicated": "Not routinely indicated",
        "regimen": "No routine perioperative or postoperative antibiotic course.",
        "rationale": (
            "The AAO-HNS Clinical Practice Guideline: Tonsillectomy in Children explicitly "
            "recommends against routine perioperative antibiotics for tonsillectomy with or "
            "without adenoidectomy -- they do not reduce pain, bleeding, or "
            "return-to-normal-activity time and add unnecessary risk." + _CAVEAT
        ),
    },
}

SLUG_CATEGORY = {
    "parathyroidectomy": "THYROID_PARA_CLEAN",
    "endoscopic-sinus-surgery": "NASAL_SINUS_CLEAN",
    "tympanostomy-tubes": "CLEAN_NO_IMPLANT",
    "tonsillectomy-adenoidectomy": "PEDIATRIC_TONSIL",
    "tympanoplasty": "CLEAN_IMPLANT",
    "direct-laryngoscopy-bronchoscopy": "ENDOSCOPIC_NO_INCISION",
    "supraglottoplasty": "ENDOSCOPIC_NO_INCISION",
    "thyroid-lobectomy": "THYROID_PARA_CLEAN",
    "total-thyroidectomy": "THYROID_PARA_CLEAN",
    "parotidectomy": "CLEAN_NO_IMPLANT",
    "mastoidectomy": "SKULL_BASE_CSF",
    "septoplasty": "NASAL_SINUS_CLEAN",
    "stapedotomy": "CLEAN_IMPLANT",
    "cochlear-implant": "CLEAN_IMPLANT",
    "total-laryngectomy": "CLEAN_CONTAMINATED_MUCOSAL",
    "submandibular-gland": "CLEAN_NO_IMPLANT",
    "sialendoscopy": "ENDOSCOPIC_NO_INCISION",
    "DLB": "ENDOSCOPIC_NO_INCISION",
    "airway-dilation": "ENDOSCOPIC_NO_INCISION",
    "medialization": "CLEAN_IMPLANT",
    "zenker": "CLEAN_CONTAMINATED_MUCOSAL",
    "tonsillectomy": "PEDIATRIC_TONSIL",
    "adenoidectomy": "PEDIATRIC_TONSIL",
    "thyroglossal": "CLEAN_NO_IMPLANT",
    "branchial": "CLEAN_NO_IMPLANT",
    "orbital-floor": "CLEAN_IMPLANT",
    "mandible-orif": "FACIAL_TRAUMA_MUCOSAL",
    "zmc-orif": "FACIAL_TRAUMA_MUCOSAL",
    "hypoglossal-stimulator": "CLEAN_IMPLANT",
    "ossiculoplasty": "CLEAN_IMPLANT",
    "canalplasty": "CLEAN_NO_IMPLANT",
    "tegmen-repair": "SKULL_BASE_CSF",
    "vestibular-schwannoma": "SKULL_BASE_CSF",
    "maxillary-antrostomy": "NASAL_SINUS_CLEAN",
    "sphenoidotomy": "NASAL_SINUS_CLEAN",
    "draf": "NASAL_SINUS_CLEAN",
    "csf-nasoseptal": "SKULL_BASE_CSF",
    "spa-ligation": "NASAL_SINUS_CLEAN",
    "tors": "CLEAN_CONTAMINATED_MUCOSAL",
    "oral-composite": "CLEAN_CONTAMINATED_MUCOSAL",
    "tep": "CLEAN_CONTAMINATED_MUCOSAL",
    "central-neck": "THYROID_PARA_CLEAN",
    "reop-thyroid": "THYROID_PARA_CLEAN",
    "four-gland": "THYROID_PARA_CLEAN",
    "reop-parathyroid": "THYROID_PARA_CLEAN",
    "parotid-total": "CLEAN_NO_IMPLANT",
    "peds-ltr": "CLEAN_CONTAMINATED_MUCOSAL",
    "ctr": "CLEAN_CONTAMINATED_MUCOSAL",
    "tracheal-resection": "CLEAN_CONTAMINATED_MUCOSAL",
    "injection-laryngoplasty": "ENDOSCOPIC_NO_INCISION",
    "arytenoid-adduction": "CLEAN_NO_IMPLANT",
    "cordotomy": "ENDOSCOPIC_NO_INCISION",
    "cp-myotomy": "CLEAN_CONTAMINATED_MUCOSAL",
    "laryngeal-botox": "ENDOSCOPIC_NO_INCISION",
    "septorhino": "NASAL_SINUS_CLEAN",
    "otoplasty": "CLEAN_NO_IMPLANT",
    "forehead-flap": "CLEAN_CONTAMINATED_MUCOSAL",
    "microflap": "ENDOSCOPIC_NO_INCISION",
    "rrp-debridement": "ENDOSCOPIC_NO_INCISION",
    "reconstructive-palate": "CLEAN_CONTAMINATED_MUCOSAL",
    "lingual-tonsillectomy": "CLEAN_CONTAMINATED_MUCOSAL",
    "hyoid-genioglossus": "CLEAN_CONTAMINATED_MUCOSAL",
    "closed-nasal-reduction": "CLEAN_NO_IMPLANT",
    "noe-orif": "FACIAL_TRAUMA_MUCOSAL",
    "bilobed-flap": "CLEAN_NO_IMPLANT",
    "melolabial-flap": "CLEAN_NO_IMPLANT",
    "cervicofacial-flap": "CLEAN_NO_IMPLANT",
    "skin-graft-face": "CLEAN_NO_IMPLANT",
    "facial-nerve-reanimation": "CLEAN_NO_IMPLANT",
    "free-flap-basics": "CLEAN_CONTAMINATED_MUCOSAL",
    "airway-fb": "ENDOSCOPIC_NO_INCISION",
    "conservation-laryngectomy": "CLEAN_CONTAMINATED_MUCOSAL",
    "transoral-laser-laryngeal-cancer": "CLEAN_CONTAMINATED_MUCOSAL",
    "microtia-reconstruction": "CLEAN_IMPLANT",
    "palatoplasty": "CLEAN_CONTAMINATED_MUCOSAL",
    "laryngotracheal-cleft-repair": "CLEAN_CONTAMINATED_MUCOSAL",
    "transnasal-esophagoscopy": "ENDOSCOPIC_NO_INCISION",
    "rigid-tracheobronchoscopy": "ENDOSCOPIC_NO_INCISION",
    "free-flap-takeback": "CLEAN_CONTAMINATED_MUCOSAL",
    "middle-fossa-skull-base": "SKULL_BASE_CSF",
    "retrosigmoid-skull-base": "SKULL_BASE_CSF",
    "translabyrinthine-skull-base": "SKULL_BASE_CSF",
    "jugular-foramen-tumor": "SKULL_BASE_CSF",
    "adult-ltr": "CLEAN_CONTAMINATED_MUCOSAL",
    "mma": "CLEAN_CONTAMINATED_MUCOSAL",
}

# Cases where a fixed category doesn't fit -- already-infected/therapeutic fields,
# or cases that split on an intraoperative finding rather than the diagnosis alone.
SLUG_BESPOKE = {
    "tracheostomy": {
        "indicated": "Selective -- a single preop dose is reasonable",
        "regimen": (
            "A single preoperative dose covering skin flora (e.g., cefazolin) is reasonable "
            "given entry into the airway; there is no good evidence for extending antibiotics "
            "beyond the perioperative period for a routine tracheostomy."
        ),
        "rationale": (
            "Tracheostomy is clean-contaminated because it opens the airway to "
            "skin/oropharyngeal flora, but the evidence for prophylaxis is weaker than for "
            "mucosal head-and-neck cases; practice varies by institution." + _CAVEAT
        ),
    },
    "neck-dissection": {
        "indicated": "Depends on whether the aerodigestive tract is entered",
        "regimen": (
            "An isolated neck dissection without violation of the oral cavity, pharynx, or "
            "larynx is clean and does not routinely need prophylaxis. A neck dissection "
            "combined with resection that enters the upper aerodigestive-tract mucosa becomes "
            "clean-contaminated and should get a preoperative dose covering oral flora (e.g., "
            "ampicillin-sulbactam)."
        ),
        "rationale": (
            "The mucosal-entry distinction, not the neck dissection itself, is what changes the "
            "antibiotic decision -- base it on the combined procedure, not a stand-alone rule."
            + _CAVEAT
        ),
    },
    "orbital-abscess": {
        "indicated": "Therapeutic, not prophylactic",
        "regimen": (
            "The patient has an established infection; use empiric broad-spectrum therapeutic "
            "antibiotics covering typical sinogenic organisms (including anaerobes) pending "
            "culture, continued postoperatively per infectious-disease/institutional protocol."
        ),
        "rationale": (
            "Drainage of an orbital abscess is source control for an active infection, so "
            "dosing and duration follow infection-treatment principles, not surgical "
            "prophylaxis rules." + _CAVEAT
        ),
    },
    "deep-neck-drain": {
        "indicated": "Therapeutic, not prophylactic",
        "regimen": (
            "The patient has an established deep neck space infection/abscess; use empiric "
            "therapeutic antibiotics covering oral/pharyngeal flora (including anaerobic "
            "coverage) pending culture, continued postoperatively per protocol."
        ),
        "rationale": (
            "Drainage of an infected deep neck space is source control, not a clean or "
            "clean-contaminated elective case, so prophylaxis categories do not apply directly."
            + _CAVEAT
        ),
    },
    "pta-drainage": {
        "indicated": "Therapeutic, not prophylactic",
        "regimen": (
            "Peritonsillar abscess drainage is treatment of an existing infection; continue "
            "therapeutic antibiotics covering oral/pharyngeal flora (a penicillin plus a "
            "beta-lactamase inhibitor, or clindamycin if allergic) rather than a single "
            "prophylactic dose."
        ),
        "rationale": (
            "The abscess is already present at the time of drainage, so this is infection "
            "treatment, not surgical prophylaxis." + _CAVEAT
        ),
    },
    "button-battery": {
        "indicated": "Case-dependent -- treat mucosal injury, not the procedure itself",
        "regimen": (
            "Antibiotic use tracks the depth of injury found at endoscopy: superficial mucosal "
            "injury generally does not need antibiotics, while a deep burn, suspected "
            "perforation, or mediastinal contamination requires therapeutic broad-spectrum "
            "coverage and urgent surgical/ID involvement."
        ),
        "rationale": (
            "The removal procedure itself does not define antibiotic need -- the tissue injury "
            "discovered during it does." + _CAVEAT
        ),
    },
    "esophageal-fb": {
        "indicated": "Selective",
        "regimen": (
            "If the mucosa is intact, no antibiotics are needed. If there is a mucosal tear, "
            "impaction-related pressure injury, or any suspicion of perforation, treat with "
            "therapeutic antibiotics covering oral/esophageal flora and evaluate urgently for "
            "perforation."
        ),
        "rationale": (
            "Uncomplicated foreign-body removal without mucosal injury does not warrant "
            "prophylaxis, but a suspected perforation changes this to an infection-treatment "
            "problem." + _CAVEAT
        ),
    },
    "pharyngocutaneous-fistula": {
        "indicated": "Treat infection if present; tailor perioperative coverage to the closure",
        "regimen": (
            "Assess for cellulitis, abscess, and systemic infection; use therapeutic antibiotics "
            "when infection is present, guided by cultures and oral/pharyngeal flora. For a "
            "noninfected elective closure entering mucosa, select perioperative prophylaxis "
            "according to the reconstructive approach; do not automatically continue a "
            "therapeutic course until closure."
        ),
        "rationale": (
            "A fistula is a wound-healing complication, but contamination alone does not "
            "establish an infection requiring a prolonged therapeutic course." + _CAVEAT
        ),
    },
    "laryngeal-fracture": {
        "indicated": "Selective",
        "regimen": (
            "A closed external laryngeal fracture repair without a mucosal laceration does not "
            "require prophylaxis beyond routine clean-case practice. When endoscopy or "
            "exploration finds a mucosal tear communicating with the airway, treat it as "
            "clean-contaminated and give a preoperative dose covering oral/respiratory flora."
        ),
        "rationale": (
            "Whether the mucosa is breached -- found intraoperatively -- determines the "
            "antibiotic category more than the injury mechanism itself." + _CAVEAT
        ),
    },
    "frontal-sinus-trauma": {
        "indicated": "Depends on the operative approach and associated injury",
        "regimen": (
            "An isolated closed repair without sinus or mucosal entry may not need prophylaxis. "
            "For operative sinus entry or cranialization, choose a preoperative agent by the "
            "approach and local protocol. Evaluate a CSF leak or dural injury separately; "
            "neither alone mandates prolonged postoperative prophylaxis."
        ),
        "rationale": (
            "Frontal sinus trauma repair sits between clean (isolated anterior-table fracture) "
            "and clean-contaminated/dural-exposed (posterior-table injury, CSF leak) -- base "
            "duration on what is actually found, not the diagnosis alone." + _CAVEAT
        ),
    },
}


def _find_module(deep, domain, topic):
    for m in deep.get(domain, []):
        if m.get("topic") == topic:
            return m
    return None


def apply_clinical_safety_and_format_gaps_v446(data_module, app_module=None):
    deep_source = getattr(data_module, "DEEP_MODULES_V6", None)
    reg_source = getattr(data_module, "OR_PREP_REGISTRY", None)
    if not isinstance(deep_source, dict) or not isinstance(reg_source, dict):
        raise RuntimeError("v44.6: production curriculum registries unavailable")

    deep = deepcopy(deep_source)
    reg = deepcopy(reg_source)

    # --- 1. Laryngeal trauma readability pilot ---
    lt = _find_module(deep, LARYNGEAL_TRAUMA_DOMAIN, LARYNGEAL_TRAUMA_TOPIC)
    if lt is None:
        raise RuntimeError(f"v44.6: missing topic {LARYNGEAL_TRAUMA_TOPIC!r}")
    for field, text in LARYNGEAL_TRAUMA_FIELDS.items():
        lt[field] = text

    # --- 2. Allergy testing intradermal + SPT criteria ---
    at = _find_module(deep, ALLERGY_DOMAIN, ALLERGY_TOPIC)
    if at is None:
        raise RuntimeError(f"v44.6: missing topic {ALLERGY_TOPIC!r}")
    if "intradermal" not in at.get("workup", "").lower():
        at["workup"] = ALLERGY_WORKUP

    # --- 3a. Ethmoidectomy retrobulbar hematoma content ---
    eth = _find_module(deep, ETHMOIDECTOMY_DOMAIN, ETHMOIDECTOMY_TOPIC)
    if eth is None:
        raise RuntimeError(f"v44.6: missing topic {ETHMOIDECTOMY_TOPIC!r}")
    if _RETROBULBAR_MARKER not in eth.get("operate", "").lower():
        eth["operate"] = ETHMOIDECTOMY_OPERATE
    if _RETROBULBAR_MARKER not in eth.get("teach", "").lower():
        eth["teach"] = ETHMOIDECTOMY_TEACH

    # --- 3b/3c. OR-prep cards: endoscopic-sinus-surgery + frontal-sinus-trauma ---
    ess = reg.get("endoscopic-sinus-surgery")
    if ess is None:
        raise RuntimeError("v44.6: missing OR card endoscopic-sinus-surgery")
    danger = list(ess.get("danger") or [])
    if not any(_RETROBULBAR_MARKER in str(d).lower() for d in danger):
        danger.append(ESS_DANGER_ADDITION)
        ess["danger"] = danger
    followup = list(ess.get("attending_followup") or [])
    if not any(_RETROBULBAR_MARKER in str(qa).lower() for qa in followup):
        followup.append(list(ESS_FOLLOWUP_QA))
        ess["attending_followup"] = followup

    fst = reg.get("frontal-sinus-trauma")
    if fst is None:
        raise RuntimeError("v44.6: missing OR card frontal-sinus-trauma")
    danger = list(fst.get("danger") or [])
    if not any(_RETROBULBAR_MARKER in str(d).lower() for d in danger):
        danger.append(FST_DANGER_ADDITION)
        fst["danger"] = danger
    followup = list(fst.get("attending_followup") or [])
    if not any(_RETROBULBAR_MARKER in str(qa).lower() for qa in followup):
        followup.append(list(FST_FOLLOWUP_QA))
        fst["attending_followup"] = followup

    # --- 4. Antibiotics field across every OR_PREP_REGISTRY card ---
    missing = [slug for slug in reg if slug not in SLUG_CATEGORY and slug not in SLUG_BESPOKE]
    if missing:
        raise RuntimeError(f"v44.6: no antibiotics mapping for OR cards: {missing}")
    extra = [
        slug for slug in list(SLUG_CATEGORY) + list(SLUG_BESPOKE) if slug not in reg
    ]
    if extra:
        raise RuntimeError(f"v44.6: antibiotics mapping references unknown OR cards: {extra}")

    antibiotics_set = 0
    for slug, card in reg.items():
        if "antibiotics" in card:
            continue
        if slug in SLUG_BESPOKE:
            card["antibiotics"] = dict(SLUG_BESPOKE[slug])
        else:
            card["antibiotics"] = dict(ANTIBIOTIC_CATEGORIES[SLUG_CATEGORY[slug]])
        antibiotics_set += 1

    data_module.DEEP_MODULES_V6.clear()
    data_module.DEEP_MODULES_V6.update(deep)
    data_module.OR_PREP_REGISTRY.clear()
    data_module.OR_PREP_REGISTRY.update(reg)
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
        app_module.OR_PREP_REGISTRY = data_module.OR_PREP_REGISTRY

    return {
        "laryngeal_trauma_rewritten": True,
        "allergy_testing_intradermal_added": True,
        "ethmoidectomy_retrobulbar_added": True,
        "or_cards_retrobulbar_added": ["endoscopic-sinus-surgery", "frontal-sinus-trauma"],
        "or_cards_antibiotics_set": antibiotics_set,
        "or_cards_total": len(reg),
    }
