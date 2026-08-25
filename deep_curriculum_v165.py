"""v16.5 — Cross-domain Deep Curriculum enrichment, pass 6.

Continues the in-place depth audit with another decision-heavy topic in each
non-Otology domain. No new canonical topics or concept IDs are created.
"""


def _entry(candidates, recognize, localize, workup, manage, operate, teach, tags, sources=None):
    return {
        "candidates": tuple(candidates),
        "fields": {
            "recognize": recognize, "localize": localize, "workup": workup,
            "manage": manage, "operate": operate, "teach": teach,
            "tags": list(tags),
            **({"source_basis": list(sources)} if sources else {}),
        },
    }


PATCHES_V165 = {
    "Rhinology / Allergy / Skull Base": [
        _entry(
            ["Allergic Fungal Rhinosinusitis", "Allergic Fungal Sinusitis", "AFRS"],
            "Allergic fungal rhinosinusitis is a noninvasive, usually type-2/eosinophilic inflammatory phenotype occurring in immunocompetent patients, often with nasal polyposis, thick eosinophilic mucin, asthma/atopy, heterogeneous sinus opacification and bony expansion/remodeling. The dramatic CT appearance can mimic invasive fungal disease, but AFRS does not require fungal tissue invasion. Distinguish it from fungal ball, ordinary CRSwNP and acute invasive fungal rhinosinusitis because urgency and treatment are fundamentally different.",
            "AFRS commonly produces expansile sinus disease with pressure remodeling, thinning or focal erosion of skull base/orbit from chronic inflammation rather than angioinvasive necrosis. Allergic mucin contains eosinophils and fungal elements but the fungus remains extramucosal. Unilateral or asymmetric disease is common, and expansion into orbit/skull-base boundaries can be substantial despite the noninvasive biology.",
            "Use nasal endoscopy and CT to define polyps, allergic mucin, involved sinuses and expansion; MRI can help distinguish proteinaceous fungal mucin from surrounding inflamed mucosa and assess orbital/skull-base relationships. Histopathology should evaluate allergic/eosinophilic mucin and specifically exclude tissue invasion. Fungal stain/culture supports the phenotype but culture alone neither proves AFRS nor invasive disease. Assess asthma/atopy and recurrence burden as part of the inflammatory phenotype.",
            "Treatment combines complete surgical clearance of obstructing allergic mucin with durable sinus access plus postoperative anti-inflammatory therapy, especially topical corticosteroid irrigations and selected systemic steroids. Long-term endoscopic surveillance matters because recurrence is common. Antifungal drugs are not the central treatment for classic noninvasive AFRS, and a positive fungal culture should not trigger an invasive-fungal regimen without tissue invasion or the appropriate host/clinical syndrome.",
            "ESS should remove thick allergic mucin and polyps, ventilate involved sinuses and create access for postoperative topical therapy while respecting thinned/remodeled skull base and orbit. Expansion may distort landmarks, so image-based anatomic planning is essential. Do not mistake pressure-related bony erosion for a mandate to resect skull base/orbit; the goal is inflammatory source clearance and safe restoration of access, with repair only when a true defect is present.",
            "Boards/chief framework: AFRS can erode bone without invading tissue. Immunocompetent patient + polyps + allergic mucin + expansile heterogeneous sinus disease suggests AFRS; high-risk host + necrosis/cranial neuropathy + histologic invasion suggests AIFR. The pathology word that changes the emergency is invasion.",
            ["AFRS", "allergic fungal rhinosinusitis", "eosinophilic mucin", "nasal polyps", "bony expansion", "noninvasive fungal disease"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],
    "Head & Neck Oncology": [
        _entry(
            ["Oral Cavity Squamous Cell Carcinoma", "Oral Cavity SCC"],
            "Oral cavity SCC commonly presents as a persistent ulcer, exophytic lesion, induration, pain, bleeding, dysarthria/dysphagia or neck mass. Tobacco/alcohol remain major risks, but HPV-mediated staging does not apply to oral-cavity SCC simply because p16 is positive. Depth of invasion is a key oral-cavity staging and neck-risk concept: a small surface lesion can have clinically meaningful invasive depth and occult nodal risk.",
            "Localize the primary by oral-cavity subsite and its relationship to mandible, floor of mouth, tongue musculature, skin and neurovascular structures. Lymphatic spread commonly reaches levels I-III, with patterns modified by subsite and burden. Mandibular proximity does not equal invasion; distinguish periosteal contact/superficial cortical involvement from gross medullary invasion because marginal versus segmental mandibular resection has major functional consequences.",
            "Biopsy the primary and obtain contrast imaging of primary/neck when invasive disease is suspected; MRI can clarify tongue/perineural/soft-tissue extent and CT is useful for mandibular cortex/medulla. Document DOI, clinical nodal status, tongue mobility, V3 symptoms, trismus and nutritional/dental status. Chest/PET staging is risk-adapted. A clinically N0 neck still requires an occult-metastasis strategy based on DOI, subsite and tumor risk rather than observation by habit.",
            "Resectable oral-cavity cancer is primarily surgical: remove the primary with oncologically appropriate margins and treat the neck electively or therapeutically according to nodal risk/burden. Early lesions may need limited resection and selective neck dissection; advanced disease may require composite resection and reconstruction. Adjuvant radiation or chemoradiation follows pathologic risk, especially positive margin/ENE for concurrent systemic therapy. Functional rehabilitation of speech/swallow and dental/nutritional planning are part of cancer treatment, not afterthoughts.",
            "Choose marginal mandibulectomy when oncologic clearance is possible while preserving mandibular continuity; choose segmental resection when medullary/gross structural invasion prevents a sound margin. Neck dissection should be compartment-oriented rather than node-picking. Reconstruction should restore tongue mobility, oral competence and mandibular continuity as required; overly bulky reconstruction can impair function just as inadequate tissue can. Orient margins carefully so pathology can guide adjuvant treatment.",
            "Boards/chief framework: oral cavity cancer is a surgery-first disease when resectable. DOI matters because it predicts occult neck disease and participates in T staging. p16 does not convert an oral-tongue cancer into HPV-mediated OPSCC. Mandible management is based on true invasion and achievable margin, not proximity alone.",
            ["oral cavity SCC", "depth of invasion", "DOI", "mandibulectomy", "neck dissection", "oral tongue", "p16"],
            ["NCCN Head & Neck v2.2026", "Pasha 6e"],
        ),
    ],
    "Thyroid / Parathyroid / Salivary": [
        _entry(
            ["Pleomorphic Adenoma", "Benign Parotid Tumors", "Parotid Pleomorphic Adenoma"],
            "Pleomorphic adenoma is the most common benign salivary neoplasm and typically presents as a slow-growing painless mobile parotid mass. It is histologically benign but has microscopic pseudopod/satellite extensions and a long-term risk of recurrence and carcinoma ex pleomorphic adenoma, so simple shelling-out/enucleation is inadequate treatment. Rapid growth, pain, fixation or facial weakness should raise concern for malignant transformation or another malignancy.",
            "Most arise in superficial parotid but deep-lobe tumors can extend into the parapharyngeal space. The facial nerve is the central operative relationship; superficial versus deep location describes position relative to the nerve, not a true fascial division. Capsular violation and tumor spillage matter because microscopic extensions beyond an apparent capsule contribute to multifocal recurrence.",
            "Use ultrasound plus FNA/core biopsy for accessible masses and MRI when deep-lobe/parapharyngeal extent, recurrent disease or neural/skull-base relationships need definition. Document facial-nerve function preoperatively. A recurrent multinodular field after prior enucleation is a different surgical problem from a primary well-contained lesion and should be imaged carefully before reoperation.",
            "Definitive treatment is complete excision with an adequate cuff/plane of normal parotid tissue while preserving the facial nerve. Contemporary extracapsular dissection or partial/superficial parotid approaches may be appropriate for selected small superficial mobile tumors in experienced hands; formal superficial parotidectomy remains appropriate when anatomy, size or uncertainty demands it. Observation can be considered selectively in frail/high-risk patients after diagnostic confidence and counseling about growth/transformation risk.",
            "Identify and preserve facial-nerve branches appropriate to the chosen approach, avoid capsular rupture and remove the tumor intact. Deep-lobe tumors may require careful mobilization around the nerve and selected transcervical/transparotid exposure. Recurrent pleomorphic adenoma may be multifocal and densely related to facial nerve; balance complete control against nerve morbidity and discuss the higher recurrence/nerve-injury risk before surgery.",
            "Boards/chief framework: pleomorphic adenoma is benign but not an enucleation lesion. Pseudopods/satellite nodules explain recurrence after capsular violation. Preserve a functioning facial nerve and remove the tumor intact with an oncologically sound tissue plane; recurrent multifocal disease is much harder than doing the primary operation correctly.",
            ["pleomorphic adenoma", "parotid", "facial nerve", "pseudopods", "tumor spillage", "carcinoma ex pleomorphic adenoma"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],
    "Pediatric Otolaryngology": [
        _entry(
            ["Deep Neck Space Infection", "Retropharyngeal Abscess", "Pediatric Deep Neck Infection"],
            "Pediatric deep-neck infection can present with fever, toxic appearance, neck stiffness/torticollis, odynophagia, drooling, muffled voice, trismus or respiratory distress. Retropharyngeal suppuration is particularly common in younger children because retropharyngeal lymph nodes involute with age. Differentiate cellulitis/phlegmon from a drainable abscess and recognize airway compromise, mediastinal spread, vascular complication or sepsis as escalation features.",
            "Retropharyngeal space lies posterior to buccopharyngeal fascia; infection can track inferiorly through deep cervical fascial planes toward the mediastinum. Parapharyngeal infection lies lateral to pharynx and near carotid sheath/lower cranial nerves. Trismus suggests masticator/parapharyngeal involvement more than a simple midline retropharyngeal process. The anatomic space predicts both complications and surgical corridor.",
            "Airway assessment comes first. Contrast CT neck is the common rapid study for suspected abscess and deep-space extent, recognizing that rim enhancement/low density does not perfectly predict pus in children. Ultrasound can help selected superficial lesions; MRI is useful when avoiding radiation is feasible or skull-base/vascular/complex extension is suspected but should not delay urgent care. Obtain blood cultures in toxic patients and operative cultures when drained.",
            "Begin IV antibiotics covering expected aerobic/anaerobic upper-airway flora and monitor airway/clinical trajectory closely. Selected stable children with small collections and no airway/neurologic/vascular complication can improve with antibiotics alone. Drainage is favored for airway compromise, large/organized abscess, sepsis/complication, clinical deterioration or failure to improve with appropriate medical therapy. Steroids may improve edema/symptoms in selected protocols but do not substitute for source control when required.",
            "Secure the airway in a controlled setting when compromise is evolving; avoid forcing a distressed child supine if that worsens obstruction. Drain retropharyngeal collections transorally when safely accessible; lateral/parapharyngeal disease may require transcervical drainage depending on location and vascular relationships. Explore only the involved space needed for source control and protect carotid sheath/cranial nerves. Descending mediastinal infection requires multidisciplinary thoracic source-control planning.",
            "Boards/chief framework: deep-neck infection questions are airway + space + pus. CT helps map disease but does not make the drainage decision by size alone. A stable child can earn a monitored antibiotic trial; airway compromise, toxicity, complication or failure to improve moves you to drainage.",
            ["retropharyngeal abscess", "deep neck infection", "parapharyngeal", "airway", "torticollis", "transoral drainage"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],
    "Laryngology / Voice / Swallowing": [
        _entry(
            ["Unilateral Vocal Fold Paralysis", "Vocal Fold Paralysis", "Unilateral Vocal Fold Immobility"],
            "Unilateral vocal-fold paralysis causes breathy dysphonia, weak cough, vocal fatigue and variable dysphagia/aspiration, but an immobile fold is a finding rather than an etiologic diagnosis. Causes include iatrogenic vagal/RLN injury, malignancy anywhere along the nerve course, skull-base/central neurologic disease, intubation/arytenoid injury and idiopathic neuropathy. Position alone does not reliably identify lesion level.",
            "The vagus exits the jugular foramen; the RLN descends into chest before returning to larynx, especially far on the left around the aortic arch. A high vagal lesion can combine vocal-fold paralysis with pharyngeal weakness/palatal or sensory deficits, producing worse swallowing than an isolated RLN lesion. Cricoarytenoid fixation/dislocation can mimic neurogenic immobility and must remain in the differential after trauma/intubation.",
            "Perform flexible laryngoscopy/stroboscopy to assess mobility, glottic gap, height mismatch and compensation. If the cause is not clearly explained by recent surgery, image the vagus/RLN course from skull base through upper mediastinum/aortic arch as appropriate. Laryngeal EMG can help distinguish neuropathy from mechanical fixation and provide prognostic information in selected cases. Evaluate swallowing when aspiration symptoms, high vagal findings or poor pulmonary reserve are present.",
            "Treatment depends on symptoms, glottic insufficiency, aspiration risk and expected neural recovery. Voice therapy and temporary injection augmentation are useful early when recovery is possible. Persistent symptomatic paralysis can be treated with type I thyroplasty, arytenoid adduction for selected posterior gap/height mismatch, or reinnervation in appropriate patients. Observation is reasonable when function is acceptable and airway protection is safe.",
            "Injection laryngoplasty medializes the fold without committing the patient to permanent framework surgery during the recovery window. Thyroplasty allows adjustable durable medialization; arytenoid adduction addresses selected posterior gap/vertical mismatch. Reinnervation restores tone/bulk rather than immediate motion and is particularly attractive in younger patients. Always confirm the diagnosis before permanent medialization when joint fixation or another mechanical lesion remains possible.",
            "Boards/chief framework: unilateral immobility triggers two questions—why is the fold not moving, and does the patient need functional treatment now? Unexplained paralysis requires evaluation along the entire nerve course. Temporary injection is not 'giving up on recovery'; it bridges voice/swallow function while biology declares itself.",
            ["UVFP", "vocal fold paralysis", "RLN", "vagus", "injection laryngoplasty", "thyroplasty", "reinnervation"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],
    "Facial Plastics / Trauma": [
        _entry(
            ["Zygomaticomaxillary Complex Fracture", "ZMC Fracture", "Zygoma Fracture"],
            "ZMC fracture disrupts the malar prominence and orbital support and may present with facial flattening, infraorbital numbness, trismus, diplopia/enophthalmos, subconjunctival hemorrhage or palpable step-offs. The decision to operate is functional/aesthetic: malar displacement, persistent ocular-volume symptoms, trismus from arch impingement or unstable displacement matter more than the mere presence of fracture lines on CT.",
            "The zygoma articulates at zygomaticofrontal, zygomaticomaxillary, zygomaticosphenoid and zygomaticotemporal/arch relationships. The sphenozygomatic region is a key three-dimensional indicator of reduction; an apparently aligned infraorbital rim can coexist with rotational malreduction. V2 traverses the infraorbital canal and commonly produces numbness. Arch depression can impinge coronoid and cause trismus.",
            "Obtain thin-cut maxillofacial CT with multiplanar review. Document visual acuity, pupils, EOM/diplopia, globe position, V2 sensation, mouth opening and malar symmetry. Emergent ophthalmologic issues such as globe injury or true muscle entrapment take priority. Isolated sensory deficit alone is not an automatic ORIF indication, and acute edema can obscure cosmetic deformity.",
            "Observe minimally displaced fractures without functional/cosmetic deficit, with soft diet and follow-up as appropriate. ORIF is indicated for meaningful displacement causing malar deformity, orbital-volume change/enophthalmos/diplopia attributable to fracture, trismus from arch displacement or instability that will not maintain reduction. Orbital-floor reconstruction is based on the orbital defect/functional consequences, not automatically performed for every ZMC fracture.",
            "Reduce the zygoma in three dimensions and verify the sphenozygomatic alignment when exposed/visible; fixation points are chosen according to instability rather than a mandatory number. Common sites include zygomaticofrontal region, infraorbital rim and zygomaticomaxillary buttress. Protect globe/V2 and restore orbital volume when indicated. Before closure verify malar projection, mouth opening and globe position; plating a rotationally malreduced zygoma locks in the deformity.",
            "Boards/chief framework: ZMC is a three-dimensional rotation problem. Operate for displacement with functional or aesthetic consequence, not for CT drama alone. The sphenozygomatic relationship is a powerful reduction check, and orbital-floor repair is a separate decision based on orbital indication.",
            ["ZMC", "zygoma fracture", "malar projection", "sphenozygomatic", "V2", "orbital floor", "trismus"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],
    "Sleep Surgery": [
        _entry(
            ["Hypoglossal Nerve Stimulation", "Upper Airway Stimulation", "HNS for OSA"],
            "Hypoglossal nerve stimulation is a selected therapy for obstructive sleep apnea in patients unable or unwilling to use PAP effectively who meet device/program criteria. Selection depends on OSA severity, central-event burden, BMI/anatomic considerations and especially collapse pattern on drug-induced sleep endoscopy; complete concentric collapse at the velum is a classic exclusion for standard unilateral HNS pathways. It is not simply an implant for anyone who dislikes CPAP.",
            "The stimulation cuff targets protrusor branches of CN XII to recruit genioglossus and improve retrolingual airway patency, while avoiding excessive retrusor activation. A respiratory-sensing lead coordinates stimulation with inspiration in common systems. HNS primarily changes dynamic neuromuscular airway behavior; it does not remove tonsils, advance jaws or directly correct fixed nasal obstruction.",
            "Confirm current diagnostic sleep testing and characterize obstructive versus central burden. Perform DISE to define collapse pattern and exclude unfavorable complete concentric palatal collapse for conventional candidacy. Review BMI and payer/device-specific criteria, prior airway surgery, tongue motion/CN XII function and patient ability to operate/charge/follow the device. Counsel that implantation is followed by activation, titration and objective sleep testing rather than immediate cure on postoperative day one.",
            "Use HNS when the phenotype and candidacy criteria predict benefit and PAP is not a workable long-term therapy. Continue weight and comorbidity management because anatomy/weight change can alter response. After healing, activate and progressively titrate stimulation for comfort and efficacy, then verify outcome with sleep testing. Persistent residual OSA should trigger re-evaluation of settings, adherence, weight and residual collapse rather than reflexive explantation.",
            "Implantation requires identification of the appropriate hypoglossal nerve branches and cuff placement that preferentially recruits tongue protrusion, plus secure respiratory sensor/generator placement according to system. Intraoperative stimulation confirms tongue motion and helps avoid retrusor-dominant activation. Protect CN XII and adjacent structures and avoid cuff placement that produces tongue deviation without useful airway opening. Revision may be needed for lead migration, device failure or inadequate recruitment but is not first-line for a titration problem.",
            "Boards/chief framework: HNS is phenotype-selected neuromodulation. DISE matters because complete concentric velum collapse predicts poor candidacy for conventional unilateral systems. Implantation is only the first half of treatment—the device must be activated, titrated and objectively tested afterward.",
            ["hypoglossal nerve stimulation", "HNS", "DISE", "complete concentric collapse", "OSA", "genioglossus", "PAP intolerance"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],
    "General ENT / Emergencies": [
        _entry(
            ["Angioedema", "Angioedema and Upper Airway Obstruction"],
            "Angioedema is abrupt submucosal/subcutaneous swelling that can become an airway emergency. Histamine-mediated disease often accompanies urticaria/pruritus and may respond to epinephrine, antihistamines and corticosteroids; bradykinin-mediated angioedema from ACE inhibitors or hereditary/acquired C1-inhibitor disorders typically lacks urticaria and does not reliably respond to those therapies. Tongue/floor-of-mouth/laryngeal involvement, voice change, drooling, stridor or rapid progression are high-risk features.",
            "Airway risk depends on site and progression: isolated lip/facial edema is different from tongue base, floor of mouth, supraglottic or laryngeal edema. Flexible nasolaryngoscopy can define pharyngeal/laryngeal involvement in a stable cooperative patient. Progressive posterior oral/laryngeal edema can make both intubation and surgical airway increasingly difficult, so the safest airway may be an early controlled one rather than a late rescue.",
            "Assess trigger/medications, prior episodes/family history, urticaria/anaphylaxis features and airway symptoms while continuously reassessing progression. Flexible scope is useful when it will change disposition/airway planning and can be performed safely. Laboratory complement/C1-inhibitor testing helps diagnose hereditary/acquired bradykinin syndromes but does not guide the immediate airway decision. Do not delay treatment of suspected anaphylaxis for diagnostic testing.",
            "For histamine-mediated anaphylaxis/angioedema, IM epinephrine is first-line when systemic/anaphylactic features or significant airway involvement are present, with adjunct antihistamines/steroids as appropriate. Bradykinin-mediated attacks require airway vigilance and syndrome-specific therapy such as C1-inhibitor replacement or bradykinin-pathway agents where available; stop the offending ACE inhibitor permanently. Observe/disposition according to airway site, trajectory and treatment response rather than the amount of visible lip swelling alone.",
            "If airway control is needed, involve experienced airway/ENT/anesthesia teams early and choose awake or otherwise controlled techniques according to anatomy and progression while maintaining a surgical-airway backup. Repeated traumatic attempts worsen edema and can convert a manageable airway into a catastrophe. Cricothyrotomy/tracheostomy may be required when transoral/transnasal intubation is unsafe or impossible. The procedural goal is oxygenation before complete obstruction, not proving that a standard laryngoscope can work.",
            "Boards/chief framework: urticaria/pruritus points toward histamine; ACE inhibitor or hereditary episodes without hives point toward bradykinin. The medication distinction matters, but airway trajectory matters more. Posterior tongue/laryngeal progression deserves early expert airway planning because rescue becomes harder as swelling advances.",
            ["angioedema", "ACE inhibitor", "bradykinin", "histamine", "anaphylaxis", "airway", "C1 inhibitor"],
            ["Pasha 6e", "KJ Lee 12e"],
        ),
    ],
}


def apply_cross_domain_depth_v165(deep_modules):
    applied, missing = [], []
    for domain, patches in PATCHES_V165.items():
        modules = deep_modules.get(domain, [])
        for patch in patches:
            found = next((m for m in modules if m.get("topic") in patch["candidates"]), None)
            if found is None:
                missing.append((domain, patch["candidates"]))
                continue
            found.update(patch["fields"])
            applied.append((domain, found.get("topic")))
    return {"applied": applied, "missing": missing}
