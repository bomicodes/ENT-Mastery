"""v36.7 — deepen exact Cleft / Craniofacial Otologic-Airway Care canonical topic.

This bounded successor preserves the exact 40-topic Pediatric Otolaryngology inventory while
making the cleft/craniofacial airway-hearing-speech pathway learner-facing in the Deep Curriculum.
Durable anatomy and operative principles are synthesized from the user's connected Cummings 7e,
Pasha 6e, and K.J. Lee 12e copies; current management is separated and updated with ACPA,
AAO-HNSF, and peer-reviewed evidence through 2026.
"""

DOMAIN = "Pediatric Otolaryngology"
TARGET = "Cleft / Craniofacial Otologic-Airway Care"

CONNECTED_TEXTBOOKS = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — connected Google Drive full-volume copy ID 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t; durable cleft/craniofacial airway, otologic, speech and operative-anatomy foundations.",
    "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e (2022) — connected Google Drive file ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52; cleft classification/repair framework, Eustachian-tube dysfunction, chronic middle-ear disease, velopharyngeal risk and pediatric airway principles.",
    "K.J. Lee's Essential Otolaryngology, 12e (2019) — connected Google Drive file ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR; tensor/levator-Eustachian-tube mechanics, cleft-associated middle-ear disease, Robin sequence and syndromic craniofacial airway/hearing foundations.",
]

CURRENT_SOURCES = [
    "American Cleft Palate Craniofacial Association. Parameters of Care for Evaluation and Treatment of Individuals with Cleft Lip/Palate and/or Other Craniofacial Differences, revised 2024 — longitudinal team care, audiology/hearing, airway/sleep and perioperative assessment.",
    "American Cleft Palate Craniofacial Association. Standards for Approval of Cleft Palate and Craniofacial Teams, revised 2026 and released May 4, 2026 — current multidisciplinary team standard aligned with the 2024 Parameters.",
    "Rosenfeld RM et al. Clinical Practice Guideline: Tympanostomy Tubes in Children (Update). Otolaryngol Head Neck Surg. 2022;166(1_suppl):S1-S55 — cleft/craniofacial children are developmentally at-risk; tube decisions remain individualized to persistent OME, hearing and developmental risk.",
    "Stanton E et al. Tympanostomy Tubes: Are They Necessary? A Systematic Review on Implementation in Cleft Care. Cleft Palate Craniofac J. 2023;60(4):430-445. PMID 35044261.",
    "Alper CM et al. Tensor Veli Palatini Muscle Tenopexy During Furlow Palatoplasty Fails to Improve Otologic Outcomes. Cleft Palate Craniofac J. 2026 Apr 3. PMID 41930721.",
    "Bachini S et al. Hearing and Otologic Outcomes After Routine Versus Selective Ventilation Tube Insertions in Children With Cleft Palate. Cleft Palate Craniofac J. 2026 May 29. PMID 42213516.",
    "Chahade J et al. Complications of tympanostomy tubes in patients with cleft palate. Paediatr Child Health. 2026;31(4):354-359. PMID 42266256.",
    "Atipas K et al. Eustachian Tube Opening in Children With and Without Cleft Palate and Association With Otitis Media. Laryngoscope. 2026 Jun 15. PMID 42298364.",
    "Zhou Z, Zhang Y, Chen R. Surgical Therapies for Cleft Palate Patients with Otitis Media with Effusion. J Craniofac Surg. 2026 Jul 31. PMID 42536027.",
]


def _append(row, field, addition, anchor):
    current = str(row.get(field) or "")
    if anchor.lower() not in current.lower():
        row[field] = (current.rstrip() + ("\n\n" if current.strip() else "") + addition).strip()


def _add_tags(row, values):
    tags = list(row.get("tags") or [])
    seen = {str(x).lower() for x in tags}
    for value in values:
        if value.lower() not in seen:
            tags.append(value)
            seen.add(value.lower())
    row["tags"] = tags


def apply_peds_cleft_craniofacial_v367(data_module, app_module=None):
    rows = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    by_topic = {str(row.get("topic") or ""): row for row in rows}
    if len(rows) != 40 or len(by_topic) != 40:
        raise RuntimeError(
            f"v36.7 requires exact 40-topic Pediatric Otolaryngology inventory; got rows={len(rows)} unique={len(by_topic)}"
        )
    if TARGET not in by_topic:
        raise RuntimeError(f"v36.7 missing exact canonical target: {TARGET!r}")

    row = by_topic[TARGET]

    _append(
        row,
        "recognize",
        "Treat cleft and craniofacial ENT care as a LONGITUDINAL AIRWAY-HEARING-SPEECH pathway rather than a single palatal operation. Searchable clinical entry points include cleft palate, submucous cleft palate, cleft lip with disproportionate ear disease, craniofacial difference, Robin sequence / Pierre Robin sequence, micrognathia, glossoptosis, Treacher Collins syndrome, Eustachian-tube dysfunction (ETD), otitis media with effusion (OME), conductive hearing loss, velopharyngeal insufficiency (VPI), hypernasality and sleep-disordered breathing. Persistent effusion or hearing loss is expected often enough to demand surveillance, but 'expected' does not mean harmless; language development, tympanic-membrane retraction and cholesteatoma risk still matter. A small jaw, cleft, or syndrome does not identify the airway level by itself—localize obstruction before choosing an operation.",
        "longitudinal airway-hearing-speech",
    )
    _append(
        row,
        "localize",
        "Anatomy explains why the ears and airway behave differently. Abnormal levator veli palatini sling formation and altered tensor veli palatini mechanics impair active Eustachian-tube opening, producing negative middle-ear pressure, OME and conductive loss; palatal repair can improve anatomy without guaranteeing normal tubal physiology. At the same time, craniofacial obstruction may be multilevel: Robin-sequence tongue-base collapse from micrognathia/glossoptosis, midface/nasal or choanal narrowing, adenotonsillar tissue, hypotonia, pharyngeal reconstruction and lower-airway disease can coexist. For speech, distinguish palatal length/mobility and velopharyngeal closure pattern from nasal/adenoid obstruction. These are connected systems, but hearing loss, airway obstruction and VPI each require their own localization rather than one syndrome label.",
        "anatomy explains why the ears",
    )
    _append(
        row,
        "workup",
        "Make hearing a DEVELOPMENTAL VITAL SIGN. Follow the current ACPA longitudinal-care framework: infants with cleft/craniofacial differences need newborn/early audiologic evaluation and appropriate follow-up, then age-appropriate audiology plus otoscopy/tympanometry through childhood rather than waiting for a caregiver complaint. Document effusion persistence, hearing level, speech/language trajectory, TM retraction or chronic disease, prior tubes and follow-up reliability. For airway concerns, ask about work of breathing, desaturation/cyanosis, feeding failure, poor growth, snoring, witnessed events and prior anesthetic difficulty; use flexible airway examination and polysomnography when localization/severity or perioperative planning will change. Hypernasality, nasal regurgitation or suspected VPI should trigger perceptual speech assessment and structural/functional evaluation such as nasopharyngoscopy and/or multiview videofluoroscopy as appropriate. Before anesthesia, review prior airway records and define a primary plus RESCUE AIRWAY PLAN when difficult mask ventilation or intubation is plausible.",
        "developmental vital sign",
    )
    _append(
        row,
        "manage",
        "Current management separates aggressive surveillance from universal intervention. Cleft palate is an AAO-HNSF developmentally at-risk context; tympanostomy tubes may be offered when OME is present and likely to persist, especially when hearing, speech/language, TM disease or other developmental vulnerability increases consequence. Do NOT translate that into UNIVERSAL PROPHYLACTIC TUBES for every cleft, nor into a rigid wait that ignores developmental risk. Repeated tubes can cause otorrhea, granulation, tympanosclerosis, persistent perforation and repeated anesthetic exposure, so reassess phenotype at each decision. Current 2026 evidence also illustrates the boundary between mechanism and treatment: correct tensor/levator anatomy does not prove that tensor veli palatini tenopexy improves OME, and retrospective routine-versus-selective tube or palatoplasty-plus-VTI studies refine counseling but do not establish a universal mandate. Coordinate hearing, speech, feeding, dental/orthodontic, airway and surgical decisions through the cleft/craniofacial team.",
        "universal prophylactic tubes",
    )
    _append(
        row,
        "operate",
        "Senior operative decisions are purpose- and anatomy-driven. In Robin sequence, persistent clinically important obstruction may require positioning/nasopharyngeal airway support, tongue-lip adhesion, mandibular distraction or tracheostomy depending on obstruction level, severity, feeding/aspiration status, syndrome and local expertise; MICROGNATHIA ALONE is not an automatic indication for distraction. Before adenoid surgery, screen for overt/submucous cleft, short palate, poor palatal movement, prior VPI, hypernasality or nasal regurgitation because complete adenoidectomy can unmask/worsen VPI. If adenoid tissue materially contributes to obstruction and VPI risk is high, a deliberately limited or superior-partial approach may be appropriate in selected patients, but it does not guarantee normal speech. Secondary VPI operations such as pharyngeal flap or sphincter pharyngoplasty create an airway-speech tradeoff and can create/worsen OSA; postoperative obstruction must be evaluated without reflexively dismantling a successful speech reconstruction or preserving resonance at the expense of a dangerous airway. For an anticipated difficult craniofacial airway, agree on induction strategy, preservation of spontaneous ventilation when appropriate, rescue devices/personnel and postoperative monitoring before entering the OR.",
        "senior operative decisions are purpose",
    )
    _append(
        row,
        "teach",
        "Boards/chief synthesis: CLEFT/CRANIOFACIAL = longitudinal airway + hearing + speech + feeding care. Explain ET dysfunction from abnormal palatal muscle mechanics; obtain early and repeated audiology; ventilate ears when persistent OME/hearing/developmental risk warrants rather than by diagnosis alone; continue surveillance after palate repair; localize Robin/syndromic obstruction before selecting an airway operation; protect the velopharynx during adenoid and secondary speech surgery; recognize the OSA tradeoff after VPI reconstruction; and enter anesthesia with a shared primary/rescue airway plan. Textbook timing conventions for palatal surgery are useful historical frameworks, not universal deadlines—current timing belongs to the multidisciplinary cleft plan and the child's growth, airway and speech needs.",
        "boards/chief synthesis",
    )

    _add_tags(
        row,
        [
            "cleft palate", "submucous cleft palate", "craniofacial", "Robin sequence", "Pierre Robin sequence",
            "micrognathia", "glossoptosis", "Treacher Collins", "Eustachian tube dysfunction", "ETD", "OME",
            "conductive hearing loss", "velopharyngeal insufficiency", "VPI", "pharyngeal flap", "partial adenoidectomy",
            "difficult airway", "rescue airway",
        ],
    )

    sources = list(row.get("source_basis") or [])
    for source in CONNECTED_TEXTBOOKS + CURRENT_SOURCES:
        if source not in sources:
            sources.append(source)
    row["source_basis"] = sources
    row["source_grounded_v367"] = True
    row["source_metadata_v367"] = {
        "canonical_link": {"domain": DOMAIN, "topic": TARGET},
        "textbook_drive_ids": {
            "cummings_7e": "18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t",
            "pasha_6e": "14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52",
            "kj_lee_12e": "112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR",
        },
        "current_guidance": [
            "ACPA Parameters of Care 2024",
            "ACPA Standards for Approval of Cleft Palate and Craniofacial Teams 2026",
            "AAO-HNSF Tympanostomy Tubes in Children Update 2022",
            "PMID 41930721", "PMID 42213516", "PMID 42266256", "PMID 42298364", "PMID 42536027",
        ],
        "evidence_distinction": (
            "Durable palatal-muscle/Eustachian-tube, craniofacial-airway and velopharyngeal operative principles are retained from the three core textbooks. "
            "Current management follows ACPA/AAO-HNSF guidance and 2026 evidence: universal prophylactic tubes, a rigid universal palatoplasty age, guaranteed otologic benefit from tensor tenopexy, and any single Robin-sequence airway operation are explicitly not taught as universal rules."
        ),
    }

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": [TARGET], "count": 1}
