"""v30.4 — source-grounded complicated sinusitis Concept Hub rebuild.

Separates orbital from intracranial complications into different resident-level jobs:
ORBITAL owns Chandler-pattern recognition, serial eye examination, CT/MRI selection,
subperiosteal/orbital abscess decisions, and vision-preserving drainage. INTRACRANIAL
owns neurologic red flags, venous/meningeal/parenchymal spread, MRI-first escalation,
neurosurgical coordination, source control, and prolonged complication-directed therapy.
"""

import re

DOMAIN = "Rhinology / Allergy / Skull Base"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


COMPLICATED_SINUSITIS_V304 = {
    "orbital complications of sinusitis": {
        "recognize": "Recognize orbital spread as a VISION-THREATENING extension of acute sinus infection, especially ethmoid disease in children. Preseptal edema alone is not the same problem as postseptal disease. Pain with extraocular movement, ophthalmoplegia, diplopia, proptosis, chemosis, reduced acuity or color vision, relative afferent pupillary defect, or optic-disc/retinal findings demand urgent escalation. Use the Chandler framework as an anatomic severity language—preseptal cellulitis, orbital cellulitis, subperiosteal abscess, orbital abscess, and cavernous-sinus thrombosis—but manage the actual eye examination and imaging rather than the label alone.",
        "localize": "Localize infection relative to the ORBITAL SEPTUM, lamina papyracea, extraocular muscles, optic nerve, orbital apex, and cavernous sinus. Medial subperiosteal collections commonly track from ethmoid disease; superior/inferior or nonmedial collections, frontal sinus disease, dental source, gas, or extensive postseptal inflammation broaden both microbiology and operative planning. Serially document acuity, pupils/RAPD, color vision when feasible, motility, proptosis, pain, and fundus findings because deterioration—not just collection size—can change the drainage threshold.",
        "workup": "Obtain urgent contrast-enhanced CT of the sinuses and orbits when postseptal disease or an orbital complication is suspected because CT rapidly maps sinus source, bony pathways, and drainable collections. Add contrast MRI when CT is equivocal, orbital-apex/optic-nerve involvement is suspected, intracranial or cavernous-sinus extension is possible, or the clinical examination is worse than the CT suggests. Start broad IV antimicrobial therapy promptly and obtain ENT plus ophthalmology involvement for postseptal disease; blood cultures are most useful in toxic/septic patients, while operative cultures should guide narrowing when drainage occurs.",
        "manage": "Manage to preserve VISION and eradicate the SINUS SOURCE. Selected orbital cellulitis and some small medial subperiosteal abscesses—particularly in younger clinically stable children with a reliable eye exam and no optic compromise—may respond to closely observed IV antibiotics plus nasal/sinus therapy. Drainage becomes more compelling with declining vision/color vision or RAPD, ophthalmoplegia/proptosis that worsens, large or nonmedial abscess, frontal sinus source, older child/adult, anaerobic/dental concern, intracranial extension, or failure to improve on appropriate IV therapy. Observation is active: repeat eye examinations and reimage/escalate when the trajectory is wrong.",
        "operate": "Operate for two linked endpoints: decompress the threatened ORBIT and control the infected SINUS. Endoscopic ethmoidectomy with drainage of a medial subperiosteal abscess is often appropriate when anatomy permits; external or combined access may be required for superior, lateral, complex, or inaccessible collections. Orbital abscess, optic compromise, or progressive postseptal disease lowers the threshold for urgent drainage. Preserve the periorbita when possible during sinus source control, but open/drain the correct compartment when pus lies beyond it. Do not perform sinus surgery while assuming the orbital collection will necessarily decompress unless the operative route actually communicates with the abscess.",
        "teach": "Chief/boards framework: EYE EXAM DRIVES URGENCY. Preseptal findings are anterior; pain with EOM, ophthalmoplegia, proptosis or visual dysfunction means postseptal disease until proven otherwise. CT maps sinus/orbit anatomy; MRI is added for orbital apex, cavernous sinus, intracranial concern, or clinic-imaging discordance. The operative question is not simply 'abscess yes/no'—it is VISION + TRAJECTORY + LOCATION + SOURCE. This card ends at vision-preserving orbital/sinus control; meningitis, empyema, brain abscess, and cerebral venous disease belong to the intracranial card.",
        "tags": ["orbital cellulitis", "subperiosteal abscess", "orbital abscess", "Chandler classification", "lamina papyracea", "vision loss", "ethmoid sinusitis", "ophthalmology"],
        "source_basis": ["Cummings Otolaryngology—Head and Neck Surgery, 7e — acute rhinosinusitis complications and orbital infection", "K.J. Lee's Essential Otolaryngology, 12e — sinusitis complications and orbital cellulitis/abscess", "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — orbital complications, imaging, antibiotics, and drainage pearls", "ICAR-RS 2021 — acute rhinosinusitis complications and evidence-based management", "ACR Appropriateness Criteria: Sinonasal Disease 2021 Update — CT/MRI for suspected orbital and intracranial complications", "Werner et al., Ear Nose Throat J 2025 — multidisciplinary review of orbital and intracranial sinusitis complications"],
    },
    "intracranial complications of sinusitis": {
        "recognize": "Recognize intracranial spread when sinusitis is accompanied by severe or progressive headache, persistent fever/toxicity, vomiting, meningismus, altered mental status, seizure, focal neurologic deficit, cranial neuropathy, papilledema, or a course that deteriorates despite appropriate therapy. Important entities are meningitis, epidural abscess, subdural empyema, cerebritis/brain abscess, cavernous or other dural venous sinus thrombosis, and frontal-bone osteomyelitis/Pott puffy tumor with possible intracranial extension. Adolescents with frontal sinusitis are a classic risk group, but absence of dramatic nasal symptoms does not exclude intracranial disease.",
        "localize": "Localize the route and compartment of spread: frontal sinus can extend directly through posterior-table osteitis to epidural space or via valveless diploic veins to subdural/parenchymal compartments; ethmoid/sphenoid disease can reach cavernous sinus, skull base, meninges, or adjacent brain. Distinguish extra-axial epidural versus subdural collection, parenchymal abscess, meningeal enhancement, venous thrombosis, and associated osteomyelitis because neurosurgical urgency and drainage strategy differ. A Pott puffy tumor is frontal-bone osteomyelitis with subperiosteal abscess—not merely forehead edema.",
        "workup": "Escalate immediately to contrast MRI of brain/sinuses when intracranial complication is suspected because MRI better defines meninges, cerebritis, empyema, abscess, venous thrombosis, and diffusion restriction; obtain contrast CT when it is the fastest initial study, to map sinus/bony disease, or for surgical planning, but do not let a nondiagnostic CT override a concerning neurologic examination. Obtain ENT and neurosurgery involvement early, with infectious-disease input for antimicrobial duration/selection. Draw blood cultures when feasible without delaying antibiotics. Lumbar puncture is not a reflex test when mass lesion, empyema, elevated ICP, or focal findings are possible.",
        "manage": "Treat as a multidisciplinary intracranial infection: start broad IV antibiotics with CNS penetration and coverage appropriate to sinus flora and local resistance, then narrow to culture data. Provide seizure/ICP/venous-thrombosis management as indicated by the specific complication. Small selected epidural collections may occasionally be managed medically with very close imaging and specialty surveillance, but subdural empyema, significant brain abscess, neurologic deterioration, mass effect, or uncontrolled source generally requires urgent drainage. Antibiotic duration is measured in weeks and follows organism, compartment, osteomyelitis, drainage adequacy, and radiographic/clinical response rather than an uncomplicated-sinusitis course.",
        "operate": "Coordinate two-source control decisions: the INTRACRANIAL collection and the SINONASAL source. Neurosurgery determines need/route for cranial drainage; ENT should address obstructed/infected frontal, ethmoid, or sphenoid sinuses when persistent source threatens ongoing seeding. Endoscopic frontal/ethmoid/sphenoid drainage is tailored to the diseased pathway; frontal osteomyelitis or inaccessible disease may require combined approaches. Do not assume cranial drainage alone sterilizes an obstructed sinus, and do not delay necessary neurosurgical decompression while attempting sinus-only management of a subdural empyema or mass-effect lesion.",
        "teach": "Chief/boards framework: NEUROLOGIC RED FLAG + SINUSITIS = IMAGE THE BRAIN, not another routine antibiotic course. MRI is the high-yield study for intracranial soft-tissue/venous complications; CT remains valuable for speed and bony/sinus operative anatomy. Subdural empyema is particularly dangerous and usually needs urgent neurosurgical source control. Pott puffy tumor means frontal osteomyelitis with subperiosteal abscess and mandates a search for intracranial extension. This card owns meninges, venous sinuses, extra-axial and brain infection; orbital vision decisions remain in the orbital card.",
        "tags": ["intracranial sinusitis complication", "subdural empyema", "epidural abscess", "brain abscess", "meningitis", "cavernous sinus thrombosis", "Pott puffy tumor", "frontal sinusitis", "neurosurgery"],
        "source_basis": ["Cummings Otolaryngology—Head and Neck Surgery, 7e — intracranial complications of rhinosinusitis and frontal sinus infection", "K.J. Lee's Essential Otolaryngology, 12e — intracranial sinusitis complications and frontal osteomyelitis", "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — complicated sinusitis workup and surgical source control", "ICAR-RS 2021 — acute rhinosinusitis complications and management", "ACR Appropriateness Criteria: Sinonasal Disease 2021 Update — CT/MRI for suspected orbital and intracranial complications", "Werner et al., Ear Nose Throat J 2025 — multidisciplinary review of orbital and intracranial sinusitis complications"],
    },
}


def apply_rhinology_complications_rebuild_v304(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        payload = COMPLICATED_SINUSITIS_V304.get(_norm(module.get("topic")))
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v304"] = True
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
