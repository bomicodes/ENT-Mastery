"""v38.7: Validate topic-based prerequisite gates and honor cross-domain prerequisites.

Legacy prerequisite labels drifted away from the current disease-centric
curriculum. Only real, unambiguous DEEP_MODULES_V6 topics may be prerequisites.
Unrelated duplicate topic names elsewhere in the curriculum must not prevent
production startup; those are a separate curriculum-quality audit concern.
"""
import re


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", (value or "").lower()).strip()


PREREQUISITES_GATING_V114_FIXED = {
    "Audiogram Interpretation": ["Auditory Neuroanatomy / Cochlear Physiology"],
    "Tympanic Membrane Perforation": ["Audiogram Interpretation"],
    "Chronic Otitis Media / Cholesteatoma": ["Temporal Bone Anatomy"],
    "Otosclerosis / Stapes Fixation": ["Audiogram Interpretation"],
    "Cochlear Implant Candidacy": ["Pediatric Hearing Loss Workup", "Audiogram Interpretation"],
    "Ethmoidectomy": ["Nasal Anatomy for Endoscopy", "CRSsNP", "CRSwNP"],
    "Frontal Sinusotomy / Draf Procedures": ["Ethmoidectomy", "Frontal Recess / Frontal Sinus"],
    "Revision FESS": ["Ethmoidectomy"],
    "Differentiated Thyroid Cancer": ["Thyroid Nodule"],
    "Laryngotracheal Reconstruction": ["Pediatric Subglottic Stenosis", "Pediatric Tracheostomy / Decannulation", "Laryngeal Anatomy"],
    "Supraglottoplasty": ["Laryngomalacia"],
    "Medialization Thyroplasty": ["Unilateral Vocal Fold Paralysis", "Laryngeal Anatomy"],
    "Hypoglossal Nerve Stimulation": ["Adult PSG Interpretation", "DISE"],
    "Functional Septorhinoplasty": ["Functional Nasal Obstruction"],
}


def install_prerequisites_gating_fix_v387(data_module, app_module=None):
    required_topics = {_norm(topic) for topic in PREREQUISITES_GATING_V114_FIXED}
    required_topics.update(_norm(pre) for requirements in PREREQUISITES_GATING_V114_FIXED.values()
                           for pre in requirements)
    topics = {}
    for domain, modules in data_module.DEEP_MODULES_V6.items():
        for module in modules:
            normalized = _norm(module.get("topic"))
            # Duplicate names elsewhere are pre-existing curriculum defects, not
            # ambiguous prerequisite joins. Only reject names this gate will use.
            if normalized in topics and normalized in required_topics:
                raise RuntimeError(f"v38.7: duplicate prerequisite topic {normalized!r}")
            topics.setdefault(normalized, domain)
    invalid = []
    for topic, requirements in PREREQUISITES_GATING_V114_FIXED.items():
        if _norm(topic) not in topics:
            invalid.append(("topic", topic))
        for prerequisite in requirements:
            if _norm(prerequisite) not in topics:
                invalid.append((f"prerequisite for {topic}", prerequisite))
            if _norm(prerequisite) == _norm(topic):
                invalid.append((f"circular prerequisite for {topic}", prerequisite))
    if invalid:
        raise RuntimeError(f"v38.7: unresolved curriculum prerequisites: {invalid}")
    data_module.PREREQUISITES_GATING_V114 = dict(PREREQUISITES_GATING_V114_FIXED)
    if app_module is not None:
        app_module.PREREQUISITES_GATING_V114 = data_module.PREREQUISITES_GATING_V114
        # The legacy planner indexes prerequisite concepts by (current domain,
        # topic); cross-domain prerequisites are otherwise silently ignored.
        # Wrap its result BEFORE v38.4's Daily Path installer captures the plan.
        original_plan = app_module._adaptive_plan
        cross_domain = {
            _norm(topic): [pre for pre in requirements
                           if topics[_norm(pre)] != topics[_norm(topic)]]
            for topic, requirements in PREREQUISITES_GATING_V114_FIXED.items()
            if any(topics[_norm(pre)] != topics[_norm(topic)] for pre in requirements)
        }

        def guarded_plan(target_minutes=30, focus=None, concept_id=None):
            selected, unused = original_plan(target_minutes, focus, concept_id)
            try:
                from db import adaptive_mastery_map
                mastery = adaptive_mastery_map()
                item_by_topic = {}
                for item in data_module.get_adaptive_items_v120():
                    item_by_topic.setdefault(_norm(item.get("topic")), []).append(item)
                output = []
                used_ids = set()
                for item in selected:
                    prerequisites = cross_domain.get(_norm(item.get("topic")), []) if item.get("mastery_before", 0) == 0 else []
                    unmet = []
                    for prerequisite in prerequisites:
                        options = item_by_topic[_norm(prerequisite)]
                        prerequisite_id = options[0]["concept_id"]
                        if int(mastery.get(prerequisite_id, {}).get("attempts") or 0) == 0:
                            unmet.append(prerequisite)
                    if unmet:
                        # Teach the actual missing prerequisite instead of letting
                        # an unseen advanced topic bypass the gate.
                        for prerequisite in unmet:
                            prerequisite_item = sorted(item_by_topic[_norm(prerequisite)], key=lambda x: x["level"])[0]
                            if prerequisite_item["id"] not in used_ids:
                                output.append(dict(prerequisite_item,
                                                   prompt=app_module._adaptive_question(prerequisite_item),
                                                   mastery_before=0,
                                                   reason=f"Prerequisite for {item['topic']}"))
                                used_ids.add(prerequisite_item["id"])
                    elif item["id"] not in used_ids:
                        output.append(item)
                        used_ids.add(item["id"])
                # Keep the same approximate budget without dropping the first
                # prerequisite when its estimated duration exceeds the session.
                bounded = []
                total = 0
                for item in output:
                    if total and total + item["minutes"] > target_minutes + 3:
                        break
                    bounded.append(item)
                    total += item["minutes"]
                return bounded, total
            except (KeyError, TypeError, ValueError) as exc:
                raise RuntimeError(f"v38.7: adaptive prerequisite resolution failed: {exc}") from exc

        app_module._adaptive_plan = guarded_plan
    return {"gating_rules": len(PREREQUISITES_GATING_V114_FIXED), "validated": True,
            "cross_domain_guard": app_module is not None}
