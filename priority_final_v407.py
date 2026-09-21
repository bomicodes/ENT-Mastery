"""ENT Mastery v40.7 — consolidated priority patch from the 2026-09-20 audit.

This single overlay supersedes the unmerged v40.5/v40.6 review bundles.  It
applies all nine verified priority fixes atomically, keeps AJCC 8 as the
operative staging system taught and tested, adds AJCC Version 9 strictly as
labelled reference/awareness material (not yet this curriculum's adopted
clinical standard), and carries forward the already-reviewed BPPV, larynx,
button-battery, and OR follow-up repairs.
"""
from collections import Counter
from copy import deepcopy


GENERAL = "General ENT / Emergencies"

SOURCES = {
    "ajcc": "American College of Surgeons, AJCC Staging Online: current Version 9 protocols plus AJCC 8th Edition content: https://www.facs.org/quality-programs/cancer-programs/american-joint-committee-on-cancer/ajcc-staging-online/",
    "ajcc_transition": "AJCC/CAP joint statement announcing published AJCC Version 9 salivary-gland and HPV-associated oropharyngeal protocols: https://www.cap.org/news/cap-statement-on-salivary-gland-and-hpv-associated-oropharyngeal-carcinomas/ -- shown here for awareness only. AJCC 8 remains this curriculum's operative staging system for board preparation and current clinical use; AJCC 9 is not yet the adopted clinical standard and should not be treated as superseding AJCC 8 in practice.",
    "salivary": "Huang SH et al. Key Updates on Version 9 AJCC/UICC Salivary Gland Carcinoma. Ann Surg Oncol. 2026;33:4958-4963. https://pmc.ncbi.nlm.nih.gov/articles/PMC13499081/",
    "npc": "FDA approval of toripalimab for nasopharyngeal carcinoma, 2023-10-27: https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-toripalimab-tpzi-nasopharyngeal-carcinoma",
    "ted": "ATA/ETA Consensus Statement on Thyroid Eye Disease, 2022: https://pmc.ncbi.nlm.nih.gov/articles/PMC9727317/",
    "angioedema": "Sinert R et al. Randomized trial of icatibant for ACE-inhibitor-induced upper-airway angioedema. J Allergy Clin Immunol Pract. 2017. PMID 28552382.",
    "carotid": "Carotid blowout syndrome: modern trends in management. Cancer Manag Res. 2018;10:5617-5628. PMCID PMC6239123.",
    "neck_trauma": "Penetrating neck trauma: a comprehensive review. Trauma Surg Acute Care Open. 2025. PMCID PMC11956299.",
    "hns": "FDA Inspire Upper Airway Stimulation expanded adult indications, 2023: https://www.fda.gov/medical-devices/recently-approved-devices/inspire-upper-airway-stimulation-p130008s090",
    "frontal": "Current Concepts in Frontal Sinus Fracture Management. 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13108220/",
    "battery": "National Capital Poison Center button-battery guideline: https://www.poison.org/battery/guideline",
    "bppv": "AAO-HNS Clinical Practice Guideline: BPPV (Update). 2017. https://aao-hnsfjournals.onlinelibrary.wiley.com/doi/10.1177/0194599816689660",
}


ANGIOEDEMA = {
    "recognize": "Angioedema can rapidly obstruct the airway. Urticaria, pruritus, flushing, or hypotension favor mast-cell/histamine-mediated disease or anaphylaxis; recurrent nonurticarial attacks, abdominal symptoms, family history, ACE-inhibitor exposure, or acquired C1-inhibitor deficiency suggest a bradykinin pathway. These clues are imperfect: treat possible anaphylaxis immediately while serially assessing tongue, floor of mouth, voice, secretions, stridor, laryngeal involvement, and trajectory.",
    "workup": "Repeated airway examination and clinical trajectory come first. In stable cooperative patients, flexible nasolaryngoscopy can define tongue-base, supraglottic, or glottic involvement. Ask about ACE inhibitors even when long-standing, allergens/new drugs, urticaria, prior attacks, and family history. C4, C1-inhibitor quantity/function, and selected C1q testing support later hereditary/acquired differentiation but must not delay airway care or epinephrine for suspected anaphylaxis.",
    "manage": "Obtain expert airway/resuscitation help early for voice change, drooling, tongue-base or laryngeal edema, or rapid progression, with a surgical-airway rescue plan. Give IM epinephrine for suspected anaphylaxis; antihistamines are adjuncts and corticosteroids do not provide immediate airway rescue. Use approved syndrome-specific on-demand therapy for hereditary C1-inhibitor deficiency. ACE-inhibitor angioedema requires immediate, permanent ACE-inhibitor discontinuation and airway-directed support. Icatibant or C1-inhibitor use in ACE-inhibitor disease is off-label and not equivalent to established HAE treatment; a larger placebo-controlled trial did not show benefit, so no drug should delay control of a threatened airway.",
    "teach": "Airway threat first; then distinguish anaphylaxis/histamine disease, hereditary or acquired C1-inhibitor deficiency, and ACE-inhibitor angioedema. HAE-directed drugs are syndrome-specific, while ACE-inhibitor cessation is permanent and airway protection remains the decisive treatment.",
    "source_basis": [SOURCES["angioedema"]],
}

CAROTID_BLOWOUT = {
    "recognize": "After head-and-neck surgery, radiation, fistula, or recurrent tumor: exposed carotid/wound breakdown is threatened blowout; a self-limited sentinel bleed is impending blowout; uncontrolled hemorrhage is acute blowout. These are vascular/interventional categories, not NCCN staging. A resolved sentinel bleed remains an emergency.",
    "workup": "Activate surgical, anesthesia, transfusion, and neurointerventional/vascular support. Protect airway and circulation first; use careful direct pressure or packing when safe. Stable patients may undergo urgent CTA for localization and planning, whereas unstable active hemorrhage must not be delayed for routine CT. Catheter angiography can be diagnostic and therapeutic.",
    "manage": "Pressure/packing, airway control, and transfusion bridge to definitive vascular control. Parent-vessel occlusion and reconstructive covered stenting are case-dependent; assess collateral cerebral perfusion and stroke risk when physiology allows. Stents preserve flow but carry infection and rebleeding risk in exposed fields. Anatomy, cerebral perfusion, infection, goals of care, and local expertise determine strategy; treat associated infection/fistula and plan vascularized coverage when feasible.",
    "teach": "Exposed vessel = threatened; sentinel hemorrhage = impending; uncontrolled hemorrhage = acute. This classification and its endovascular options come from vascular/interventional literature, not an NCCN head-and-neck staging algorithm.",
    "source_basis": [SOURCES["carotid"]],
}

NECK_TRAUMA = {
    "topic": "Penetrating and Blunt Neck Trauma", "primary_domain": GENERAL,
    "recognize": "For penetrating injury determine platysma violation; for blunt injury consider occult carotid/vertebral dissection, laryngotracheal disruption, and pharyngoesophageal injury. Hard signs include active arterial bleeding, expanding hematoma, shock from neck injury, bruit/thrill, major airway compromise, air bubbling from the wound, or evolving focal neurologic deficit. Soft signs include a nonexpanding hematoma, dysphonia, dysphagia, minor hemoptysis, or subcutaneous emphysema.",
    "localize": "Classic zones describe exposure (I clavicle-to-cricoid, II cricoid-to-mandibular angle, III angle-to-skull base), but stable penetrating trauma is commonly evaluated with a selective no-zone pathway. Map trajectory to carotid/vertebral vessels, jugular veins, larynx/trachea, pharynx/esophagus, cervical spine, and cranial nerves. Blunt cerebrovascular screening is mechanism/risk based.",
    "workup": "Perform the primary trauma survey with cervical-spine precautions. Unstable patients or hard signs requiring immediate control proceed to operative/endovascular management without routine imaging delay. Stable selected patients undergo CTA based on mechanism and findings. CTA alone cannot exclude all esophageal injuries when trajectory, symptoms, air, or CT changes remain suspicious; add contrast evaluation and/or esophagoscopy. Use flexible laryngoscopy/bronchoscopy for suspected airway injury.",
    "manage": "Control hemorrhage with direct pressure and resuscitation; do not blindly clamp or probe a neck wound. Use a controlled airway plan with expert surgical backup when laryngotracheal disruption is suspected. Stable patients without operative indications receive selective CTA-based observation and serial examinations rather than mandatory Zone-II exploration. Suspected perforation requires prompt multidisciplinary evaluation, infection prevention, and timely repair or carefully selected nonoperative care.",
    "operate": "Operate for ongoing major hemorrhage, expanding hematoma, threatened airway, or demonstrated vascular/aerodigestive injury needing repair. Obtain proximal/distal vascular control when possible and select exposure by trajectory rather than enlarging a contaminated entry wound blindly. Inspect and repair/drain associated pharyngeal, esophageal, and airway injuries. Avoid reflexive intubation across suspected laryngotracheal separation.",
    "teach": "Resuscitation plus hard-versus-soft signs first. Stable patients receive selective CTA/no-zone assessment; unstable hemorrhage demands control. A negative CTA alone cannot clear a concerning esophageal trajectory. Blunt injury needs mechanism-based cerebrovascular screening.",
    "tags": ["neck trauma", "penetrating neck", "blunt cerebrovascular injury", "CTA", "no-zone", "esophageal injury"],
    "source_basis": ["Pasha & Golub, Otolaryngology–Head and Neck Surgery Clinical Reference Guide, 6th ed (2022), ch 10.", "Operative Otolaryngology: Head and Neck Surgery, 3rd ed, ch 75.", SOURCES["neck_trauma"]],
    "evidence_calibrated": "v40.7-primary-source-reviewed",
}

SALIVARY = {
    "topic": "Salivary Gland Malignancy", "primary_domain": "Head & Neck Oncology",
    "recognize": "A persistent or growing salivary mass with rapid growth, pain, fixation, skin involvement, facial weakness, or cervical adenopathy raises concern, although low-grade cancers may be painless. Histology and grade materially change nodal, perineural, distant-metastatic, and systemic-therapy behavior.",
    "localize": "Define major versus minor gland site, superficial/deep parotid relationships, facial-nerve function, skull-base perineural extension, and nodal levels at risk. Pretreatment facial weakness suggests nerve involvement; adenoid cystic carcinoma may track along V3 or VII.",
    "workup": "Perform a complete head-and-neck and cranial-nerve examination, targeted ultrasound with image-guided FNA/core biopsy, MRI for deep-lobe/perineural/skull-base questions, CT for bone, and risk-directed chest/distant staging. Report histology, grade, margins, PNI/LVI, nodal ENE, and actionable biomarkers. Stage with AJCC 8th Edition -- this remains the operative system for board preparation and current clinical use. AJCC/CAP have published a Version 9 salivary-gland protocol, included below for awareness, but it is not yet this curriculum's adopted clinical standard; do not treat it as replacing AJCC 8 or mix categories/stage groups across the two systems.",
    "manage": "Resect operable localized disease with site-appropriate oncologic margins and preserve a functioning facial nerve when it is not directly invaded and clearance is feasible. Base neck management and adjuvant radiation on histology/grade, T extent, nodes, margins, and PNI. Recurrent/metastatic disease requires histology- and biomarker-directed multidisciplinary evaluation (including AR, HER2, or NTRK when relevant), not one universal regimen.",
    "operate": "Select superficial/total parotidectomy or other gland resection by extent; document preoperative nerve function and avoid automatic sacrifice of a functioning uninvolved facial nerve. Address deep-lobe, skull-base, and neck disease with appropriate exposure/reconstruction and orient margins clearly for pathology.",
    "teach": "AJCC 8 is the primary system taught and tested here: major-gland T categories use size plus gross extraparenchymal/adjacent-structure invasion, minor-gland cancers follow their anatomic site, and the traditional head-and-neck nodal framework applies. AJCC Version 9 has been published (major and minor salivary carcinomas share one protocol; T1 is 2 cm or smaller without gross extraparenchymal extension, T2 is over 2 through 4 cm without it, T3 is over 4 cm or gross extraparenchymal extension for a major-gland primary, N1 is 1-3 positive nodes without ENE, N2 is more than 3 positive nodes or any ENE, stage IV reserved for M1) and is included here strictly for reference/awareness -- it is not yet this curriculum's clinical standard, so default to AJCC 8 unless a specific reason calls for the newer edition, and never blend categories across versions. Separate anatomic stage from histologic biology: adenoid cystic disease emphasizes perineural and late distant failure, while high-grade carcinomas carry greater nodal risk.",
    "tags": ["salivary gland cancer", "adenoid cystic", "mucoepidermoid", "perineural spread", "AJCC 8", "AJCC Version 9"],
    "source_basis": ["Pasha & Golub, 6th ed (2022), ch 5, pp 211-214.", SOURCES["ajcc"], SOURCES["ajcc_transition"], SOURCES["salivary"]],
    "evidence_calibrated": "v40.7-AJCC8-plus-AJCC9-transition",
}

PATCHES = (
    ("Head & Neck Oncology", ("HPV-Associated Oropharyngeal SCC", "HPV-Associated Oropharyngeal Carcinoma", "HPV-Associated OPSCC"), {
        "workup": "AJCC 8 is this curriculum's operative staging system for board preparation and current clinical practice. AJCC/CAP have separately published a Version 9 HPV-associated oropharyngeal protocol; it is noted here for awareness only and is not yet the adopted clinical standard, so continue staging with AJCC 8 unless told otherwise. Record staging system, clinical versus pathologic context, primary subsite, p16/HPV classification, T extent, and nodal burden/distribution; never combine AJCC 8 N categories or stage groups with AJCC 9 elements.",
        "teach": "Edition check before stage assignment: AJCC 8 remains the primary system taught and tested here. AJCC Version 9 exists and is mentioned for awareness, but treat it as reference material, not a replacement -- do not infer an AJCC 9 numerical stage from AJCC 8 tables or use an AJCC 8 label without identifying it as such.",
    }, ("ajcc", "ajcc_transition")),
    ("Head & Neck Oncology", ("Nasopharyngeal Carcinoma",), {
        "workup": "Confirm histology, EBV context when appropriate, endoscopic primary assessment, MRI of the primary/skull base and neck, and burden-directed distant staging. Distinguish curable locoregionally advanced disease from recurrent/metastatic disease before selecting systemic therapy.",
        "manage": "For selected locoregionally advanced nonmetastatic NPC, induction gemcitabine/cisplatin followed by definitive cisplatin-based concurrent chemoradiation is an evidence-based pathway according to stage and fitness. Do not conflate that curative pathway with recurrent/metastatic treatment: toripalimab plus gemcitabine/cisplatin is FDA-approved first-line therapy for adults with metastatic or recurrent locally advanced NPC, and toripalimab monotherapy is approved after progression on or after platinum-containing chemotherapy for recurrent unresectable/metastatic disease. Check contraindications, organ function, prior therapy, goals, and the current protocol.",
        "teach": "Two separate NPC questions: induction gemcitabine/cisplatin then chemoradiation for selected curable locally advanced disease; toripalimab plus gemcitabine/cisplatin for eligible first-line recurrent/metastatic adults.",
    }, ("npc",)),
    ("Thyroid / Parathyroid / Salivary", ("Thyroid Eye Disease", "Graves Ophthalmopathy", "Thyroid Eye Disease / Graves Ophthalmopathy"), {
        "recognize": "Assess activity and severity separately. The 7-item CAS includes spontaneous and gaze-evoked pain, eyelid redness/swelling, conjunctival redness, chemosis, and caruncle/plica inflammation; at least 3/7 commonly supports active disease at initial assessment. Sight-threatening dysthyroid optic neuropathy or corneal breakdown requires urgent ophthalmologic management.",
        "workup": "Document acuity, color vision, pupils, corneal exposure, fields/disc, exophthalmometry, lids, motility/diplopia, activity, and severity over time. Image when optic neuropathy, atypical disease, or decompression planning is at issue. Assess smoking, thyroid control, pregnancy, metabolic risk, and hearing risk before biologic therapy.",
        "manage": "Use lubrication, smoking cessation, and thyroid optimization for suitable mild disease. In active moderate-to-severe TED, match therapy to phenotype: IV glucocorticoids remain important for inflammatory disease, while teprotumumab is an important option particularly for prominent proptosis/diplopia after individualized safety, access, and preference assessment. Treat sight-threatening optic neuropathy urgently with high-dose IV glucocorticoids and decompression when response is inadequate. Sequence rehabilitative decompression, strabismus, then eyelid surgery once sufficiently inactive/stable.",
        "teach": "CAS measures activity; it is not a stand-alone treatment switch. Separate activity, severity, sight threat, and the dominant inflammation-versus-proptosis/diplopia phenotype. Teprotumumab is not automatically first-line for every patient.",
    }, ("ted",)),
    ("Head & Neck Oncology", ("Laryngeal SCC", "Laryngeal Squamous Cell Carcinoma"), {
        "teach": "Use this as a decision hub: define glottic/supraglottic/subglottic subsite, T extent, vocal-fold mobility, cartilage/extralaryngeal spread, nodes, airway, and swallowing. Compare selected early endoscopic/radiation treatment, suitable organ preservation, and primary total laryngectomy for selected extensive cartilage-invasive T4a or nonfunctional larynges; use subsite cards for exact staging and operative detail.",
    }, ()),
    ("Otology / Neurotology", ("Benign Paroxysmal Positional Vertigo", "BPPV"), {
        "workup": "Transient torsional upbeating nystagmus on Dix-Hallpike supports posterior-canal BPPV. If history is compatible but Dix-Hallpike is horizontal or negative, perform a supine roll test for horizontal-canal disease. Atypical, persistent/nonfatigable nystagmus or neurologic deficits should prompt reconsideration of a central cause; routine imaging and vestibular suppressants are not indicated for otherwise typical BPPV.",
        "manage": "Use a canalith-repositioning maneuver such as Epley for posterior-canal BPPV. For horizontal-canal disease, identify geotropic versus apogeotropic physiology and use an appropriate Lempert/barbecue-roll or Gufoni maneuver. Reassess persistent symptoms for unresolved/multicanal BPPV or an alternative peripheral/central diagnosis.",
        "teach": "Dix-Hallpike with torsional upbeating nystagmus -> posterior canal -> Epley. Compatible history with horizontal/no Dix-Hallpike nystagmus -> supine roll -> horizontal-canal-specific maneuver.",
    }, ("bppv",)),
)

BATTERY = {
    "indications": "An esophageal button battery requires immediate emergency endoscopic removal; do not delay for fasting, honey, or sucralfate. Distinguish esophageal location from a battery beyond the esophagus because location, age, and symptoms change management.",
    "exit_check": ["After removal inspect injury depth/orientation and perforation. Only when no perforation is evident, irrigate with 50-150 mL of 0.25% sterile acetic acid in increments with immediate suction; never irrigate a perforation."],
    "postop": ["Grade mucosal injury and plan airway, vascular, perforation, and delayed aorto-esophageal-fistula surveillance according to risk."],
}

FRONTAL = {
    "indications": "Base treatment on anterior-table displacement/cosmesis, posterior-table displacement/comminution, dural injury or persistent CSF leak, and frontal sinus outflow patency. Observe selected minimally displaced fractures with patent drainage and no persistent leak under reliable clinical/radiologic follow-up; consider sinus-preserving endoscopic treatment for suitable outflow obstruction and dural repair/cranialization for selected severe posterior-table injury or persistent leak. Obliteration and cranialization are not default coequal choices.",
    "exit_check": ["Verify posterior-table/dural status, frontal outflow management, and the explicit CSF-leak and long-term mucocele surveillance plan."],
}

FOLLOWUPS = {
    "tonsillectomy": ("What distinguishes primary from secondary post-tonsillectomy hemorrhage?", "Primary hemorrhage occurs within 24 hours; secondary hemorrhage occurs later, classically with eschar separation. Active bleeding requires airway/resuscitation preparation and operative control as indicated."),
    "tonsillectomy-adenoidectomy": ("Which findings support overnight observation after pediatric adenotonsillectomy?", "Age under 3 years or severe OSA (AHI at least 10 obstructive events/hour or oxygen nadir under 80%) supports inpatient monitoring under the 2019 AAO-HNS guideline; comorbidity also affects disposition."),
    "cochlear-implant": ("How do you protect the facial nerve and verify electrode placement?", "Use mastoid/facial-recess landmarks, protect facial nerve and chorda boundaries, access the planned round-window/cochleostomy site, then confirm insertion, impedances, and neural responses per protocol."),
    "total-laryngectomy": ("Why can a laryngectomy patient not be ventilated through the mouth?", "The airway is permanently separated from the upper aerodigestive tract. Oxygenate and ventilate through the neck stoma and treat obstruction there."),
    "neck-dissection": ("What is the key shoulder complication of level II/V dissection?", "CN XI traction or injury causes trapezius weakness, shoulder pain, and dysfunction; preserve it when oncologically feasible and begin rehabilitation appropriately."),
    "hypoglossal-stimulator": ("What DISE pattern excludes standard unilateral Inspire candidacy?", "Complete concentric collapse at the soft palate excludes standard candidacy. Also confirm current labeling for PAP intolerance, age, AHI, central-event burden, anatomy, and other patient factors."),
    "pta-drainage": ("Which anatomy is at risk if peritonsillar drainage passes too deeply?", "The internal carotid lies posterolateral to the tonsillar fossa; use an appropriate superficial trajectory, controlled depth, and landmarks."),
    "airway-fb": ("Why is rigid bronchoscopy favored for a high-risk pediatric airway foreign body?", "It combines airway control, ventilation, and direct extraction; prepare size-matched scopes/forceps and rescue for migration, obstruction, or bleeding."),
    "button-battery": ("When is acetic-acid irrigation appropriate after esophageal button-battery removal?", "Only after inspection confirms no perforation: use 50-150 mL of 0.25% sterile acetic acid incrementally with suction. Do not delay removal or irrigate a perforation."),
    "frontal-sinus-trauma": ("Which features favor observation versus cranialization?", "Minimal displacement with intact dura and patent drainage may be observed with follow-up; severe posterior-table injury, intracranial communication, or persistent CSF leak may require dural repair and cranialization."),
}

HNS_OLD = "The repository's existing OR framework correctly avoids treating one historical payer cutoff as universal and instead requires current criteria plus physiologic and anatomic fit."
HNS_NEW = "HNS selection is multidimensional: confirm predominantly obstructive OSA, documented PAP failure or intolerance, current device/coverage criteria, an acceptable central-plus-mixed event burden, and a compatible DISE pattern without complete concentric palatal collapse. Age, AHI, BMI, anatomy, prior surgery, neurologic function, and implanted-device considerations should be checked against current labeling and local coverage rather than reduced to one historical cutoff."


def _topic(registry, domain, aliases):
    if domain not in registry or not isinstance(registry[domain], list):
        raise RuntimeError("v40.7: missing canonical domain: " + domain)
    names = {x.casefold() for x in aliases}
    matches = [item for item in registry[domain] if str(item.get("topic", "")).casefold() in names]
    if len(matches) != 1:
        raise RuntimeError("v40.7: expected one topic %r; found %d" % (aliases, len(matches)))
    return matches[0]


def _append(item, field, text, label="v40.7 evidence update"):
    prior = item.get(field) or ""
    if not isinstance(prior, str):
        raise RuntimeError("v40.7: unexpected text field %s on %s" % (field, item.get("topic")))
    marker = label + ": " + text
    if marker not in prior:
        item[field] = prior.rstrip() + ("\n\n" if prior.strip() else "") + marker


def _sources(item, keys):
    current = item.get("source_basis") or []
    if isinstance(current, str):
        current = [current]
    if not isinstance(current, list):
        raise RuntimeError("v40.7: unsupported source_basis schema on " + str(item.get("topic")))
    item["source_basis"] = list(dict.fromkeys(current + [SOURCES[k] for k in keys]))


def _or_update(ops, slug, updates, source_key):
    if slug not in ops:
        raise RuntimeError("v40.7: missing OR card: " + slug)
    entry = ops[slug]
    for field, value in updates.items():
        if isinstance(value, str):
            _append(entry, field, value)
        else:
            current = entry.get(field) or []
            if not isinstance(current, list):
                raise RuntimeError("v40.7: unsupported OR field schema: %s.%s" % (slug, field))
            for line in value:
                if line not in current:
                    current.append(line)
            entry[field] = current
    _sources(entry, (source_key,))


def _normalize_qa(value):
    if not isinstance(value, (list, tuple)):
        return None
    rows = []
    for pair in value:
        if not (isinstance(pair, (list, tuple)) and len(pair) == 2 and all(isinstance(x, str) for x in pair)):
            return None
        rows.append((pair[0].strip(), pair[1].strip()))
    return tuple(rows)


def _replace_generic_followups(ops):
    # The review found two non-procedure-specific three-pair templates copied
    # across many OR cards. Detect exact repeated templates regardless of length.
    signatures = Counter()
    for entry in ops.values():
        normalized = _normalize_qa(entry.get("attending_followup"))
        if normalized:
            signatures[normalized] += 1
    generic_signatures = {sig for sig, count in signatures.items() if count >= 5}
    replaced, preserved = [], []
    for slug, pair in FOLLOWUPS.items():
        if slug not in ops:
            preserved.append(slug + ":missing")
            continue
        current = ops[slug].get("attending_followup")
        normalized = _normalize_qa(current)
        if normalized == (pair,):
            replaced.append(slug)
            continue
        if normalized in generic_signatures:
            ops[slug]["attending_followup"] = [list(pair)]
            replaced.append(slug)
        else:
            preserved.append(slug + ":individualized-or-unrecognized")
    return replaced, preserved


def apply_priority_final_v407(data_module, app_module=None):
    """Validate all nine priority targets, then publish one atomic overlay."""
    deep_source = getattr(data_module, "DEEP_MODULES_V6", None)
    ops_source = getattr(data_module, "OR_PREP_REGISTRY", None)
    challenges_source = getattr(data_module, "CLINICAL_CHALLENGES_V119", None)
    if not isinstance(deep_source, dict) or not isinstance(ops_source, dict) or not isinstance(challenges_source, list):
        raise RuntimeError("v40.7: production registries unavailable")
    deep, ops, challenges = deepcopy(deep_source), deepcopy(ops_source), deepcopy(challenges_source)

    emergency = {x.get("topic"): x for x in deep.get(GENERAL, [])}
    for required in ("Angioedema", "Carotid Blowout Syndrome"):
        if required not in emergency:
            raise RuntimeError("v40.7: missing canonical emergency topic: " + required)
    if "button-battery" not in ops or "frontal-sinus-trauma" not in ops:
        raise RuntimeError("v40.7: required OR cards unavailable")
    hns = [q for q in challenges if q.get("id") == "v263_sleep_hns_app"]
    if len(hns) != 1:
        raise RuntimeError("v40.7: expected one v263_sleep_hns_app vignette")
    explanation = hns[0].get("explanation")
    if not isinstance(explanation, str) or (HNS_OLD not in explanation and HNS_NEW not in explanation):
        raise RuntimeError("v40.7: HNS explanation changed; manual reconciliation required")
    targets = [(domain, aliases, _topic(deep, domain, aliases)) for domain, aliases, _, _ in PATCHES]

    for name, fields in (("Angioedema", ANGIOEDEMA), ("Carotid Blowout Syndrome", CAROTID_BLOWOUT)):
        current_sources = emergency[name].get("source_basis") or []
        if isinstance(current_sources, str):
            current_sources = [current_sources]
        emergency[name].update({k: deepcopy(v) for k, v in fields.items() if k != "source_basis"})
        emergency[name]["source_basis"] = list(dict.fromkeys(current_sources + fields["source_basis"]))
        emergency[name]["evidence_calibrated"] = "v40.7-primary-source-reviewed"
    if not any(x.get("topic") == NECK_TRAUMA["topic"] for x in deep[GENERAL]):
        deep[GENERAL].append(deepcopy(NECK_TRAUMA))

    modified = []
    for (domain, aliases, item), (_, _, fields, source_keys) in zip(targets, PATCHES):
        for field, text in fields.items():
            _append(item, field, text)
        _sources(item, source_keys)
        modified.append(item["topic"])
    oncology = deep.get("Head & Neck Oncology")
    if not isinstance(oncology, list):
        raise RuntimeError("v40.7: Head & Neck Oncology domain unavailable")
    existing_salivary = None
    for domain_topics in deep.values():
        if not isinstance(domain_topics, list):
            continue
        for x in domain_topics:
            if isinstance(x, dict) and x.get("topic") == SALIVARY["topic"]:
                existing_salivary = x
                break
        if existing_salivary is not None:
            break
    if existing_salivary is None:
        oncology.append(deepcopy(SALIVARY))
    else:
        for field in ("recognize", "localize", "workup", "manage", "operate", "teach"):
            if field in SALIVARY:
                _append(existing_salivary, field, SALIVARY[field])
        current_sources = existing_salivary.get("source_basis") or []
        if isinstance(current_sources, str):
            current_sources = [current_sources]
        existing_salivary["source_basis"] = list(dict.fromkeys(current_sources + SALIVARY["source_basis"]))
        existing_tags = existing_salivary.get("tags") or []
        existing_salivary["tags"] = list(dict.fromkeys(existing_tags + SALIVARY.get("tags", [])))
        existing_salivary["evidence_calibrated"] = SALIVARY["evidence_calibrated"]

    _or_update(ops, "button-battery", BATTERY, "battery")
    _or_update(ops, "frontal-sinus-trauma", FRONTAL, "frontal")
    followup_replaced, followup_preserved = _replace_generic_followups(ops)
    if HNS_OLD in explanation:
        hns[0]["explanation"] = explanation.replace(HNS_OLD, HNS_NEW)

    data_module.DEEP_MODULES_V6.clear(); data_module.DEEP_MODULES_V6.update(deep)
    data_module.OR_PREP_REGISTRY.clear(); data_module.OR_PREP_REGISTRY.update(ops)
    data_module.CLINICAL_CHALLENGES_V119[:] = challenges
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
        app_module.OR_PREP_REGISTRY = data_module.OR_PREP_REGISTRY
        app_module.CLINICAL_CHALLENGES_V119 = data_module.CLINICAL_CHALLENGES_V119
    return {
        "priority_items_fixed": 9,
        "deep_updated": ["Angioedema", "Carotid Blowout Syndrome"] + modified,
        "deep_added": [NECK_TRAUMA["topic"]] + ([] if existing_salivary is not None else [SALIVARY["topic"]]),
        "salivary_merged_into_existing_domain": (existing_salivary or {}).get("primary_domain"),
        "hns_vignette_fixed": True,
        "or_cards_updated": ["button-battery", "frontal-sinus-trauma"],
        "followups_replaced": followup_replaced,
        "followups_preserved": followup_preserved,
        "ajcc_policy": "AJCC 8 is the operative staging system for boards and current clinical use; AJCC 9 is included for reference/awareness only and is not treated as this curriculum's adopted clinical standard; no cross-version numerical inference",
    }
