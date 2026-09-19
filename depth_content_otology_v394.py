"""v39.4 -- Otology / Neurotology depth repair (content-staleness sweep, batch 5/9).

Same two defects as v39.0-v39.3. Otosclerosis / Stapes Fixation already had
distinct, layered recognize/localize content from earlier refinement
patches -- only its operate field carried the unfilled boilerplate prefix,
so only that field is touched here; the rest of this batch replaces both
recognize/localize and operate. See thyroglossal_duct_cyst_depth_v389 for
the pattern and rationale.
"""

DOMAIN = "Otology / Neurotology"

DEPTH_V394 = {
    "Otosclerosis / Stapes Fixation": {
        "operate": (
            "Indication: audiometrically and clinically convincing otosclerotic conductive/mixed "
            "loss in a patient who understands and accepts the alternative to hearing aids. Setup: "
            "transcanal microscopic or endoscopic approach, tympanomeatal flap elevation to expose "
            "the middle ear. Key steps: confirm stapes fixation and rule out an alternative "
            "mechanical cause (ossicular discontinuity, congenital fixation, superior canal "
            "dehiscence) under direct vision before committing; create a controlled fenestra in the "
            "footplate (small-fenestra stapedotomy is the common modern approach, by laser or "
            "microdrill), then place and crimp a properly sized prosthesis between the incus long "
            "process and the vestibule. Danger structures: the facial nerve (which can overhang the "
            "oval window), the chorda tympani (preserve when feasible), the incus long process "
            "(avoid over-crimping or subluxation), and the inner ear itself, where excessive footplate "
            "manipulation risks a perilymph gusher or profound sensorineural loss. Failure mode: "
            "forcing the sequence through when the footplate becomes floating, the facial nerve "
            "markedly overhangs the field, bleeding obscures visualization, or unexpected "
            "perilymphatic flow raises concern for a gusher -- any of these should stop the planned "
            "steps, control the immediate problem, and prompt reassessment or abandonment rather than "
            "pushing to finish. Postoperative plan: counsel on expected transient vertigo/taste "
            "change, avoid pressure/water exposure during healing, and obtain postoperative "
            "audiometry to confirm air-bone gap closure rather than assuming success from the "
            "intraoperative appearance alone."
        ),
    },
    "Audiogram Interpretation": {
        "recognize": (
            "Reading an audiogram starts with test reliability (consistent thresholds, appropriate "
            "masking), then the air-bone relationship at each frequency to classify conductive, "
            "sensorineural, or mixed loss, then symmetry between ears and the shape (configuration) "
            "of the loss across frequencies -- flat, sloping, cookie-bite, or notched -- each of which "
            "narrows the differential before you even consider speech scores."
        ),
        "localize": (
            "An air-bone gap localizes pathology to the outer/middle ear (conductive component); "
            "bone-conduction threshold elevation localizes to the cochlea or beyond (sensorineural "
            "component); word recognition score disproportionately worse than the pure-tone average "
            "predicts, or striking interaural asymmetry, localizes suspicion toward a retrocochlear "
            "process (e.g., vestibular schwannoma) rather than routine cochlear disease."
        ),
        "operate": (
            "The audiogram itself is not operated on, but it is the decision instrument for nearly "
            "every otologic procedure: it defines candidacy thresholds (stapedotomy for a conductive/"
            "mixed loss with adequate cochlear reserve, cochlear implantation for severe-to-profound "
            "loss with limited aided benefit), confirms whether a planned procedure is even addressing "
            "the loss present (e.g., don't plan a conductive-repair operation on a purely "
            "sensorineural pattern), and provides the baseline against which postoperative hearing "
            "results are judged. Failure mode: reading a single threshold or a single visit's audiogram "
            "in isolation and using it to justify a procedure, instead of confirming the pattern is "
            "reproducible, fits the exam, and is the kind of loss the planned intervention can "
            "actually be expected to improve."
        ),
    },
    "Tympanic Membrane Perforation": {
        "recognize": (
            "Characterize any perforation along several axes before deciding on management: acute "
            "(traumatic/infectious, often self-limited) versus chronic (present beyond ~3 months, "
            "unlikely to close spontaneously); size and quadrant; margin appearance (rolled/"
            "epithelialized edges suggest chronicity and reduce spontaneous closure chances); presence "
            "of active infection/otorrhea; and associated hearing loss or signs of deeper disease "
            "(retraction, keratin debris suggesting cholesteatoma)."
        ),
        "localize": (
            "Site matters beyond the hole itself: marginal or attic perforations carry higher risk of "
            "associated cholesteatoma and ossicular erosion than a central pars tensa perforation, and "
            "a perforation with an air-bone gap larger than expected for its size should raise concern "
            "for ossicular discontinuity rather than the perforation alone explaining the hearing loss."
        ),
        "operate": (
            "Indication: persistent (generally beyond 3 months), symptomatic (hearing loss, recurrent "
            "infection, water-precaution burden) perforation, or one associated with suspected "
            "ossicular/deeper disease. Setup: myringoplasty (graft alone) for a simple perforation "
            "with normal ossicular chain, or tympanoplasty with ossicular assessment/reconstruction "
            "when discontinuity is suspected. Key steps: freshen perforation edges, elevate a "
            "tympanomeatal flap if using an underlay technique, place graft material (temporalis "
            "fascia, perichondrium, or fat for a small perforation) under or over the remnant drum, "
            "and support with packing. Danger structures: the chorda tympani (preserve when possible) "
            "and, if working near the ossicular chain, the incus and stapes superstructure. Failure "
            "mode: treating every perforation as the primary diagnosis rather than a window revealing "
            "deeper middle-ear disease (cholesteatoma, ossicular erosion) that must be addressed at "
            "the same operation or the repair will fail or mask progressive disease. Postoperative "
            "plan: water precautions during healing, and audiometry at follow-up to confirm both graft "
            "take and hearing improvement, not graft closure alone."
        ),
    },
    "Hearing Aids and Bone-Conduction Devices": {
        "recognize": (
            "Match the rehabilitation technology to the type of hearing loss and the physical "
            "usability of the ear: conventional air-conduction aids can rehabilitate sensorineural, "
            "conductive, and mixed hearing loss when the canal accepts an earmold and output is "
            "sufficient; atresia, persistent otorrhea, intolerance, or an excessive conductive "
            "component may favor bone-conduction bypass rather than conventional amplification."
        ),
        "localize": (
            "When the outer/middle ear pathway cannot be used (aural atresia or chronic draining ear), "
            "bone conduction bypasses that pathway; for single-sided deafness, the reason to route "
            "signal to the better ear is unilateral cochlear/neural deficit, not a conductive lesion. "
            "Available solutions include "
            "bypassing it -- bone-conduction devices (percutaneous, transcutaneous, or a bone-"
            "conduction hearing implant) or, for single-sided deafness/severe asymmetry, CROS/BiCROS "
            "routing sends signal from the poorer to the better ear; sensorineural loss with a usable "
            "canal and adequate residual hearing is instead managed with a conventional or, if "
            "severe-to-profound, cochlear implant pathway."
        ),
        "operate": (
            "Indication for a surgically placed device (percutaneous or transcutaneous bone-"
            "conduction implant): conductive/mixed loss with an unusable ear canal or middle ear "
            "(atresia, chronic drainage) where conventional amplification cannot be delivered or "
            "tolerated, or single-sided deafness when a bone-conduction/CROS solution is preferred "
            "over a non-surgical CROS aid. Setup: implant placed over the mastoid at a location and "
            "depth that allows sound transducer coupling. Danger structures: the sigmoid sinus and "
            "dura, which limit safe implant positioning on a thin or anatomically unfavorable "
            "mastoid, and the skin/soft tissue overlying a percutaneous abutment, which is prone to "
            "irritation or infection. Failure mode: selecting a device by the audiogram label alone "
            "(e.g., defaulting to a bone-conduction device for any conductive loss) rather than by "
            "whether the ear canal/middle ear pathway is actually usable -- a reconstructable "
            "conductive problem may be better served by addressing the underlying pathology (e.g., "
            "ossiculoplasty) than by bypassing it permanently. Postoperative plan: skin care around a "
            "percutaneous abutment or monitoring for transcutaneous implant-site issues, and fitting/"
            "programming once healed."
        ),
    },
    "Ototoxic / Noise-Induced Hearing Loss": {
        "recognize": (
            "A history of significant noise exposure (occupational, recreational, blast) or a "
            "known ototoxic exposure (aminoglycosides, cisplatin, loop diuretics at high dose) paired "
            "with a compatible sensorineural pattern raises the diagnosis; tinnitus frequently appears "
            "before the patient perceives functional hearing loss, so tinnitus alone in an exposed "
            "patient warrants audiometric evaluation rather than reassurance."
        ),
        "localize": (
            "Noise-induced loss classically localizes to the 4 kHz region (a 'noise notch') on the "
            "audiogram, reflecting the cochlear region most vulnerable to acoustic trauma, while "
            "ototoxic drug effects more often begin in the high frequencies and progress, with "
            "aminoglycosides and cisplatin acting primarily on cochlear (and sometimes vestibular) "
            "hair cells rather than a retrocochlear site."
        ),
        "operate": (
            "This is not a surgical disease; the actionable decisions are preventive and "
            "monitoring-based rather than procedural. Key steps: for patients on ototoxic therapy, "
            "follow an established serial-monitoring protocol (baseline plus interval audiometry, "
            "including high-frequency/ultra-high-frequency testing where available) so a change is "
            "caught while therapy adjustment is still possible, and coordinate with the prescribing "
            "team about dose modification or alternative agents when hearing changes emerge. For "
            "noise exposure, counsel on hearing protection and exposure reduction. Failure mode: "
            "waiting for a large, obviously disabling threshold shift before acting -- serial "
            "audiometric change, not an arbitrary severity cutoff, is what should trigger "
            "intervention, since ototoxic injury is often only partially reversible once advanced. "
            "Postoperative/ongoing plan: once loss is established and stable, rehabilitate with "
            "amplification or implantable options as appropriate to severity."
        ),
    },
    "Autoimmune Inner Ear Disease": {
        "recognize": (
            "Suspect autoimmune inner ear disease with rapidly progressive or fluctuating "
            "sensorineural hearing loss, often but not always bilateral and asymmetric, evolving "
            "over weeks to months; there is no single confirmatory biomarker, so this remains a "
            "clinical diagnosis of pattern recognition plus response to treatment, not a positive "
            "lab test."
        ),
        "localize": (
            "The presumed site of disease is the cochlea (and sometimes vestibular end organ) under "
            "immune-mediated attack, either as an isolated inner-ear process or as part of a "
            "systemic autoimmune/vasculitic disease (e.g., granulomatosis with polyangiitis, "
            "relapsing polychondritis, systemic lupus erythematosus), which is why a systemic review "
            "of symptoms and, when indicated, rheumatologic workup accompanies the audiologic picture."
        ),
        "operate": (
            "Not a surgical disease at diagnosis; the key decisions are diagnostic and "
            "pharmacologic. Key steps: obtain serial audiometry to document the fluctuating/"
            "progressive pattern, pursue a targeted systemic workup only when history suggests a "
            "specific associated disease (rather than a broad undirected autoimmune panel), and "
            "exclude more common mimics (Meniere's disease, retrocochlear pathology) before "
            "committing to an autoimmune diagnosis. A corticosteroid trial, directed by "
            "otology/rheumatology, is both diagnostic (response supports the diagnosis) and "
            "therapeutic. Failure mode: treating a positive autoimmune-associated lab value as "
            "sufficient to make the diagnosis, or conversely dismissing the diagnosis because no "
            "single test is positive -- this is a syndrome of exclusion plus treatment response, not "
            "a lab-confirmed entity. Postoperative/ongoing plan: for patients who progress to "
            "severe-to-profound loss despite treatment, cochlear implantation remains an effective "
            "rehabilitation option and should be discussed rather than withheld because of the "
            "underlying autoimmune process."
        ),
    },
    "CSF Otorrhea / Temporal Encephalocele": {
        "recognize": (
            "Suspect a tegmen defect with or without encephalocele when a patient has persistent "
            "unilateral 'middle-ear effusion' that does not behave like typical otitis media with "
            "effusion, clear watery otorrhea, recurrent meningitis, or a previously placed tube with "
            "unremitting clear drainage -- any of these should prompt testing the fluid (beta-2 "
            "transferrin) rather than assuming routine effusion."
        ),
        "localize": (
            "The defect is localized to the tegmen tympani/mastoideum, the thin bony roof separating "
            "the middle ear/mastoid from the middle cranial fossa; herniated dura with or without "
            "brain tissue (encephalocele) through that defect is what produces the CSF leak, and "
            "high-resolution CT (bony defect) paired with MRI (soft-tissue herniation) together define "
            "site and size before planning repair."
        ),
        "operate": (
            "Indication: confirmed CSF leak or symptomatic encephalocele, or recurrent meningitis "
            "traced to a tegmen defect. Setup: strategy (transmastoid, middle fossa, or combined) is "
            "chosen by defect size, location, and number of defects -- small, single, accessible "
            "defects often suit a transmastoid approach, while larger or multiple defects, or those "
            "far anterior/medial on the tegmen, often need a middle fossa approach for adequate "
            "exposure. Key steps: reduce any herniated encephalocele tissue (resect if "
            "non-functional/necrotic, reduce if viable), and repair the bony defect in a multilayer "
            "fashion (e.g., bone/cartilage graft plus soft tissue, sometimes with fascia) rather than "
            "soft tissue alone, which is prone to re-herniation. Danger structures: the dura and "
            "underlying temporal lobe, the ossicular chain and facial nerve in the middle ear/mastoid "
            "field, and the sigmoid sinus depending on approach. Failure mode: treating a leak as "
            "routine middle-ear effusion and placing a tube, which does not address the underlying "
            "dural defect and can worsen the leak or delay diagnosis of an evolving intracranial "
            "problem -- recognizing that the 'effusion' is actually CSF changes every subsequent "
            "step, including the urgency of imaging and referral. Postoperative plan: monitor for "
            "recurrent leak or meningitis, and consider intracranial pressure physiology (e.g., "
            "obesity-associated idiopathic intracranial hypertension) as a contributor that may need "
            "separate management to prevent recurrence."
        ),
    },
    "Petrous Apex Lesions": {
        "recognize": (
            "An expansile petrous apex lesion is recognized on imaging, often incidentally, and must "
            "be distinguished by CT bone behavior and MRI signal characteristics: cholesterol "
            "granuloma (T1 and T2 hyperintense, expansile, smoothly marginated), petrous apex "
            "cholesteatoma/epidermoid (T1 hypo- to isointense, restricted diffusion), and neoplasm "
            "(variable, often with more aggressive bone destruction or enhancement) behave "
            "differently and require different management."
        ),
        "localize": (
            "Localization within the petrous apex, and its relationship to the internal carotid "
            "artery, cochlea, internal auditory canal, and Meckel's cave, determines which surgical "
            "corridor (if any) is safe -- an asymptomatic, non-expansile lesion in a good position for "
            "observation is managed very differently from one abutting the carotid canal or causing "
            "cranial neuropathy."
        ),
        "operate": (
            "Indication: symptomatic, growing, or diagnostically uncertain lesions; a stable, "
            "asymptomatic, imaging-characteristic cholesterol granuloma or trapped fluid can often be "
            "observed with serial imaging rather than operated on. Setup: corridor choice (transcanal "
            "infracochlear, infralabyrinthine, middle fossa, or transsphenoidal endoscopic approach "
            "for medially positioned lesions) depends on the lesion's exact position and the "
            "available aerated or safe anatomic pathway around the cochlea, carotid, and labyrinth. "
            "Key steps: for a cholesterol granuloma, the goal is usually drainage and creation of a "
            "permanent aeration tract rather than complete lesion removal, since recurrence is common "
            "without ongoing drainage; a neoplasm instead requires biopsy/resection matched to its "
            "specific pathology. Danger structures: internal carotid artery, cochlea and labyrinth, "
            "and lower cranial nerves depending on the chosen corridor. Failure mode: choosing an "
            "approach based on surgeon familiarity rather than the lesion's biology and the actual "
            "aerated/anatomic corridors available in that patient's temporal bone -- the safest route "
            "is dictated by the anatomy and diagnosis, not a default technique. Postoperative plan: "
            "serial imaging to confirm the drainage tract remains patent (cholesterol granuloma) or "
            "to monitor for recurrence (neoplasm), since these lesions are tracked over years, not "
            "just at a single postoperative visit."
        ),
    },
}


def apply_depth_content_otology_v394(data_module):
    modules = {m.get("topic"): m for m in data_module.DEEP_MODULES_V6.get(DOMAIN, [])}
    missing = [t for t in DEPTH_V394 if t not in modules]
    if missing:
        raise RuntimeError(f"v39.4: expected {DOMAIN} topics not found: {missing}")
    for topic, fields in DEPTH_V394.items():
        modules[topic].update(fields)
    return {"enriched": list(DEPTH_V394.keys())}
