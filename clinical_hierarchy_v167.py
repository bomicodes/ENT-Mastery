"""v16.7 — Clinical-judgment hierarchy pass after duplicate canonicalization.

Keeps clinically distinct parent/child and operation/rescue concepts separate,
while making their educational relationship explicit. Also narrows several
child modules whose earlier prose repeated the parent concept and installs
backward concept-ID aliases so historical mastery follows retired nodes.
"""


SCOPE_REWRITES_V167 = {
    "Tympanostomy Tube Indications": {
        "recognize": "Treat this as a candidacy question, not a second AOM/OME lesson. The decision is whether a child with a defined middle-ear disease phenotype is likely to benefit from ventilation tubes now.",
        "localize": "Confirm the target is persistent or recurrent middle-ear ventilation failure behind the tympanic membrane and distinguish it from isolated otalgia, external-ear disease, sensorineural loss, or transient post-URI pressure symptoms.",
        "workup": "Anchor candidacy to present effusion, duration, age-appropriate hearing assessment, attributable symptoms, and developmental risk. In recurrent AOM, the current ear examination matters: infection history alone is not enough when effusion is absent at assessment.",
        "manage": "Use a guideline-style decision: chronic bilateral OME with hearing difficulty is a strong tube phenotype; chronic OME with meaningful attributable symptoms may also justify tubes; recurrent AOM with effusion supports candidacy, whereas recurrent AOM without effusion generally does not.",
        "operate": "Translate the indication into operative counseling: confirm laterality and current ear status, perform a safe myringotomy, evacuate fluid when present, seat the tube, and counsel about otorrhea, extrusion, obstruction, persistent perforation, follow-up, and water/activity expectations according to local practice.",
        "teach": "Do not re-count infections from memory. Ask: Is fluid present now? Has it persisted? What hearing, symptom, or developmental consequence makes ventilation worth the procedural risk?",
    },
    "CRSsNP": {
        "recognize": "Assume the learner already knows the generic CRS definition. Focus on chronic objective sinonasal inflammation without polyps and actively look for phenotypes that change the plan: localized disease, odontogenic source, unilateral disease, immune dysfunction, ciliary disease, or an anatomic bottleneck.",
        "localize": "Use endoscopy and CT distribution to decide whether disease is diffuse inflammatory CRS or a localized drainage-pathway/source problem. Maxillary-predominant unilateral disease should trigger odontogenic and other unilateral differentials rather than automatic routine-CRS labeling.",
        "workup": "Confirm objective disease, then selectively investigate the modifier suggested by the phenotype—dental source, immune deficiency, ciliary disorder, fungal process, tumor concern, or medication/systemic contributor. Avoid broad testing that will not alter management.",
        "manage": "Topical anti-inflammatory therapy and saline remain foundational, but escalation should target the phenotype. Treat an odontogenic or focal source when present; use surgery for medically refractory objective disease when anatomy and symptom burden support benefit.",
        "operate": "Plan ESS from the involved drainage pathways and the need for durable topical access, while correcting a focal source when relevant. The goal is not to convert every CRSsNP patient into the same extent of FESS.",
        "teach": "CRSsNP is not simply CRS without visible polyps. The chief-level move is identifying what is driving this non-polyp disease and tailoring both workup and surgical extent to that driver.",
    },
    "CRSwNP": {
        "recognize": "Assume generic CRS recognition is already mastered. Here the high-yield task is recognizing a polyp phenotype and asking what biology travels with it: type-2 inflammation, asthma, AERD, eosinophilia, recurrent disease, smell loss, and prior surgery burden.",
        "localize": "Map diffuse versus asymmetric polyp disease and distinguish expected bilateral inflammatory polyposis from a unilateral mass that requires a different tumor or fungal differential. Disease distribution also affects topical delivery and surgical access.",
        "workup": "Use endoscopy and CT to establish burden and anatomy, then phenotype selectively with asthma/AERD history and other inflammatory markers only when they will influence biologic or multidisciplinary decisions. Unilateral or atypical tissue requires appropriate pathologic evaluation.",
        "manage": "Build a longitudinal inflammatory plan: high-quality topical therapy, limited systemic rescue when appropriate, ESS for refractory disease or access, and biologic therapy for selected severe or recurrent type-2 disease. Choose sequencing from severity, prior surgery, asthma/AERD, smell, steroid burden, and patient goals.",
        "operate": "Surgery should remove obstructing inflammatory tissue, restore safe sinus access, and create a cavity that supports postoperative topical therapy and surveillance. It reduces disease burden but does not remove the inflammatory tendency to recur.",
        "teach": "The advanced CRSwNP question is not surgery or biologic in isolation. It is which sequence best controls a chronic type-2 disease while minimizing steroid exposure, revision burden, and lower-airway morbidity.",
    },
    "Mandibular Biomechanics and Occlusion": {
        "recognize": "Start after the fracture has already been identified. Read the mandible as a loaded ring: displacement reflects muscle pull, fracture geometry, dentition, and whether the segment is favorable or unfavorable under function.",
        "localize": "Identify tension and compression zones, torsional forces, tooth-bearing versus non-tooth-bearing segments, condylar influence on ramus height, and how each fracture pattern changes occlusion. Occlusion is the functional readout of reduction.",
        "workup": "Use the fracture map, dentition, preinjury occlusion, comminution, bone quality, and associated fractures to decide whether fixation can share load with bone or must bear the load. The imaging question is mechanical planning, not repeat diagnosis.",
        "manage": "Sequence reduction around restoration of facial width, height, and reproducible occlusion. Choose closed treatment, load-sharing miniplate concepts, or load-bearing reconstruction based on stability, comminution, infection, atrophy, and patient factors rather than a one-plate-fits-all rule.",
        "operate": "Establish occlusion and anatomic reduction before definitive fixation whenever feasible. Place fixation where it neutralizes the expected forces while protecting tooth roots, inferior alveolar nerve, mental nerve, and adjacent soft tissues; verify ramus height and condylar seating before accepting the bite.",
        "teach": "A mandible plate is not just hardware across a crack. Explain what force the construct is resisting, whether bone is sharing the load, and how you know the restored occlusion is mechanically trustworthy.",
    },
}


CURRICULUM_RELATIONSHIPS_V167 = {
    "Otosclerosis / Stapes Fixation": {"role": "procedure-linked disease", "parents": ["Audiogram Interpretation"]},
    "Tympanostomy Tube Indications": {"role": "procedure/candidacy", "parents": ["AOM / OME / Tympanostomy Decisions"]},
    "CRSsNP": {"role": "subtype", "parents": ["CRS Phenotyping"]},
    "CRSwNP": {"role": "subtype", "parents": ["CRS Phenotyping"]},
    "Mandibular Biomechanics and Occlusion": {"role": "advanced mechanics", "parents": ["Mandible Fracture"]},
    "Neck Dissection": {"role": "procedure", "parents": ["Neck Management by Primary Site"]},
    "Complications of Neck Surgery": {"role": "complication/rescue", "parents": ["Neck Dissection"]},
    "Free-Flap Monitoring / Compromise / Salvage": {"role": "complication/rescue", "parents": ["Reconstruction Selection After H&N Ablation"]},
    "Cochlear Implant Surgery": {"role": "procedure", "parents": ["Cochlear Implant Candidacy"]},
    "Cochlear Implant Failure / Revision": {"role": "failure/rescue", "parents": ["Cochlear Implant Surgery"]},
    "Type I Thyroplasty": {"role": "procedure", "parents": ["Unilateral Vocal Fold Paralysis"]},
    "Laryngeal Reinnervation": {"role": "procedure", "parents": ["Unilateral Vocal Fold Paralysis"]},
    "Posterior Cordotomy / Arytenoidectomy": {"role": "procedure", "parents": ["Bilateral Vocal Fold Immobility"]},
    "Microtia Reconstruction": {"role": "procedure", "parents": ["Microtia / Aural Atresia"]},
    "Endoscopic CSF Leak Repair": {"role": "procedure", "parents": ["CSF Rhinorrhea / Skull-Base Defects"]},
    "Salvage Surgery After Radiation / Chemoradiation": {"role": "salvage", "parents": ["Recurrent / Metastatic HNSCC"]},
}


# Only highly directional foundations are hard-gated. Rescue modules stay in the
# graph but are not hidden behind prerequisites; residents may need them urgently.
HARD_RELATIONSHIPS_V167 = {
    "Tympanostomy Tube Indications": ["AOM / OME / Tympanostomy Decisions"],
    "CRSsNP": ["CRS Phenotyping"],
    "CRSwNP": ["CRS Phenotyping"],
    "Mandibular Biomechanics and Occlusion": ["Mandible Fracture"],
}


def _module(data, topic):
    for domain, modules in data.DEEP_MODULES_V6.items():
        for module in modules:
            if module.get("topic") == topic:
                return domain, module
    return None, None


def _merge_unique(existing, additions):
    out = list(existing or [])
    seen = {str(x).strip().lower() for x in out}
    for item in additions or []:
        key = str(item).strip().lower()
        if key and key not in seen:
            out.append(item)
            seen.add(key)
    return out


def _merge_adaptive_rows(a, b):
    """Combine two historical curriculum_mastery rows after aliasing."""
    if not a:
        return dict(b)
    out = dict(a)
    out["mastery_level"] = max(int(a.get("mastery_level") or 0), int(b.get("mastery_level") or 0))
    out["attempts"] = int(a.get("attempts") or 0) + int(b.get("attempts") or 0)
    out["correct"] = int(a.get("correct") or 0) + int(b.get("correct") or 0)
    if str(b.get("last_seen") or "") > str(a.get("last_seen") or ""):
        out["last_seen"] = b.get("last_seen")
        out["topic"] = b.get("topic") or out.get("topic")
        out["domain"] = b.get("domain") or out.get("domain")
    dues = [x for x in (a.get("next_due"), b.get("next_due")) if x is not None]
    if dues:
        try:
            out["next_due"] = min(dues)
        except TypeError:
            out["next_due"] = min(dues, key=lambda x: str(x))
    return out


def _install_mastery_aliases(data, id_map, topic_map):
    """Make retired concept IDs read/write as their canonical concept IDs."""
    if not id_map:
        return

    old_cid = getattr(data, "canonical_concept_id_v98", None)
    old_domain = getattr(data, "canonical_concept_domain_v98", None)
    if callable(old_cid) and not getattr(old_cid, "_v167_alias_wrapper", False):
        def canonical_concept_id_v167(concept_id, domain=None):
            base = old_cid(concept_id, domain)
            return id_map.get(base, id_map.get(concept_id, base))
        canonical_concept_id_v167._v167_alias_wrapper = True
        data.canonical_concept_id_v98 = canonical_concept_id_v167

    # Keep current domain canonicalization behavior; ID aliasing is the critical
    # requirement. Then wrap modern DB reads/writes so Daily Path history follows.
    try:
        import db
    except Exception:
        return

    if not getattr(db, "_V167_MASTERY_ALIASES_INSTALLED", False):
        raw_adaptive = db.adaptive_mastery_map
        def adaptive_mastery_map_v167():
            raw = raw_adaptive()
            out = {}
            for cid, row in raw.items():
                canonical = id_map.get(cid, cid)
                item = dict(row)
                item["concept_id"] = canonical
                if canonical != cid:
                    for (domain, old_topic), new_topic in topic_map.items():
                        if item.get("topic") == old_topic:
                            item["topic"] = new_topic
                            item["domain"] = domain
                            break
                out[canonical] = _merge_adaptive_rows(out.get(canonical), item)
            return out
        db.adaptive_mastery_map = adaptive_mastery_map_v167

        raw_record_adaptive = db.record_adaptive_result
        def record_adaptive_result_v167(concept_id, item_id, domain, topic, stage, level, rating, interval_days):
            canonical = id_map.get(concept_id, concept_id)
            if canonical != concept_id:
                topic = topic_map.get((domain, topic), topic)
            return raw_record_adaptive(canonical, item_id, domain, topic, stage, level, rating, interval_days)
        db.record_adaptive_result = record_adaptive_result_v167

        raw_record_event = db.record_mastery_event
        def record_mastery_event_v167(concept_id, domain, dimension, score, source_type=None, source_id=None, miss_type=None):
            return raw_record_event(id_map.get(concept_id, concept_id), domain, dimension, score, source_type, source_id, miss_type)
        db.record_mastery_event = record_mastery_event_v167

        db._V167_MASTERY_ALIASES_INSTALLED = True


def apply_clinical_hierarchy_v167(data, id_map=None, topic_map=None):
    id_map = id_map if id_map is not None else {}
    topic_map = topic_map if topic_map is not None else {}

    for topic, rewrite in SCOPE_REWRITES_V167.items():
        _domain, module = _module(data, topic)
        if module is not None:
            module.update(rewrite)

    data.CURRICULUM_RELATIONSHIPS_V167 = dict(CURRICULUM_RELATIONSHIPS_V167)

    suggested = getattr(data, "PREREQUISITES_SUGGESTED_V114", None)
    if isinstance(suggested, dict):
        for topic, rel in CURRICULUM_RELATIONSHIPS_V167.items():
            suggested[topic] = _merge_unique(suggested.get(topic), rel.get("parents"))

    hard = getattr(data, "HARD_PREREQUISITES_V114", None)
    if isinstance(hard, dict):
        for topic, parents in HARD_RELATIONSHIPS_V167.items():
            hard[topic] = _merge_unique(hard.get(topic), parents)

    # Ensure all alias pairs, including the v16.6 merges and the new otosclerosis
    # merge, remain visible to persistence/read models after the node disappears.
    data.RETIRED_CONCEPT_ALIASES_V167 = dict(id_map)
    data.RETIRED_TOPIC_ALIASES_V167 = {
        old_topic: new_topic for (_domain, old_topic), new_topic in topic_map.items()
    }
    _install_mastery_aliases(data, id_map, topic_map)

    return {
        "scope_rewrites": [t for t in SCOPE_REWRITES_V167 if _module(data, t)[1] is not None],
        "relationships": dict(CURRICULUM_RELATIONSHIPS_V167),
        "hard_relationships": dict(HARD_RELATIONSHIPS_V167),
        "retired_concept_aliases": dict(id_map),
    }
