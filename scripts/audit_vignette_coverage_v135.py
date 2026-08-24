"""ENT Mastery canonical vignette coverage + depth / call / OR audit.

Milestones are intentionally separate:
1) every canonical topic has a linked vignette;
2) every canonical topic has at least two independently linked vignettes;
3) the bank has enough explicit board, overnight-call, postoperative-call, and
   OR-prep cases in each domain, plus named high-risk topics that must carry an
   appropriate focus tag.

Integrity defects always fail. Material focus gaps are printed explicitly and
also fail this audit so '100%' cannot mean shallow title coverage only.
"""
from collections import Counter, defaultdict
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import wsgi

data = wsgi.data

# Minimum explicit tagged second-pass cases by domain. These are not intended to
# imply that every topic is an emergency/procedure; they enforce representative
# readiness in domains where the resident must make those decisions.
FOCUS_MINIMUMS = {
    "Otology / Neurotology": {"boards": 5, "OR_prep": 8, "overnight_call": 3},
    "Rhinology / Allergy / Skull Base": {"boards": 5, "OR_prep": 8, "overnight_call": 3},
    "Head & Neck Oncology": {"boards": 6, "OR_prep": 10, "overnight_call": 3},
    "Thyroid / Parathyroid / Salivary": {"boards": 5, "OR_prep": 8, "overnight_call": 2},
    "Pediatric Otolaryngology": {"boards": 6, "OR_prep": 8, "overnight_call": 4},
    "Laryngology / Voice / Swallowing": {"boards": 6, "OR_prep": 8, "overnight_call": 3},
    "Facial Plastics / Trauma": {"boards": 5, "OR_prep": 10, "overnight_call": 2},
    "Sleep Surgery": {"boards": 5, "OR_prep": 4},
    "General ENT / Emergencies": {"boards": 5, "OR_prep": 6, "overnight_call": 10},
}

# High-consequence concepts that should not merely exist; at least one vignette
# must explicitly train the relevant decision mode.
CRITICAL_FOCUS = {
    "overnight_call": [
        ("General ENT / Emergencies", "Post-Tonsillectomy Hemorrhage"),
        ("General ENT / Emergencies", "Tracheostomy Emergency"),
        ("General ENT / Emergencies", "Angioedema"),
        ("General ENT / Emergencies", "Deep Neck Space Infection"),
        ("General ENT / Emergencies", "Carotid Blowout Syndrome"),
        ("General ENT / Emergencies", "Esophageal Foreign Body"),
        ("Head & Neck Oncology", "Free-Flap Monitoring / Compromise / Salvage"),
        ("Head & Neck Oncology", "Total Laryngectomy"),
        ("Pediatric Otolaryngology", "Epiglottitis"),
        ("Pediatric Otolaryngology", "Button Battery Ingestion"),
        ("Pediatric Otolaryngology", "Croup vs Epiglottitis"),
        ("Pediatric Otolaryngology", "Pediatric Vocal Fold Immobility"),
        ("Rhinology / Allergy / Skull Base", "Invasive Fungal Rhinosinusitis"),
        ("Rhinology / Allergy / Skull Base", "Orbital Complications of Sinusitis"),
        ("Rhinology / Allergy / Skull Base", "Epistaxis Surgical Control"),
        ("Otology / Neurotology", "Sudden Sensorineural Hearing Loss"),
        ("Otology / Neurotology", "Central Vestibular Disorders"),
        ("Otology / Neurotology", "Vestibular Neuritis"),
        ("Thyroid / Parathyroid / Salivary", "Thyroid Eye Disease / Graves Ophthalmopathy"),
        ("Facial Plastics / Trauma", "Septal Hematoma"),
        ("Facial Plastics / Trauma", "Structured Facial Trauma Examination"),
    ],
    "OR_prep": [
        ("Otology / Neurotology", "Chronic Otitis Media / Cholesteatoma"),
        ("Otology / Neurotology", "Otosclerosis"),
        ("Otology / Neurotology", "Cochlear Implant Failure / Revision"),
        ("Rhinology / Allergy / Skull Base", "Frontal Recess / Frontal Sinus"),
        ("Rhinology / Allergy / Skull Base", "Sphenoidotomy"),
        ("Rhinology / Allergy / Skull Base", "Epistaxis Surgical Control"),
        ("Head & Neck Oncology", "Total Laryngectomy"),
        ("Head & Neck Oncology", "Neck Dissection"),
        ("Head & Neck Oncology", "Free-Flap Monitoring / Compromise / Salvage"),
        ("Thyroid / Parathyroid / Salivary", "Four-Gland Parathyroid Exploration"),
        ("Thyroid / Parathyroid / Salivary", "Submandibular Gland Excision"),
        ("Thyroid / Parathyroid / Salivary", "Reoperative Thyroid Surgery"),
        ("Pediatric Otolaryngology", "Thyroglossal Duct Cyst"),
        ("Pediatric Otolaryngology", "Tracheomalacia / Bronchomalacia"),
        ("Laryngology / Voice / Swallowing", "Arytenoid Adduction / Reinnervation"),
        ("Laryngology / Voice / Swallowing", "Tracheobronchial Endoscopy Principles"),
        ("Laryngology / Voice / Swallowing", "Aspiration-Prevention Surgery"),
        ("Facial Plastics / Trauma", "Local Flap Reconstruction"),
        ("Facial Plastics / Trauma", "Rhinoplasty Tip Mechanics"),
        ("Facial Plastics / Trauma", "Mandibular Biomechanics and Occlusion"),
        ("Sleep Surgery", "Palatal Surgery"),
        ("Sleep Surgery", "Tongue Base Surgery"),
        ("General ENT / Emergencies", "ENT Perioperative Anesthesia / Difficult Airway Planning"),
        ("General ENT / Emergencies", "Airway Foreign Body"),
        ("General ENT / Emergencies", "Chyle Leak"),
    ],
}


def main():
    modules = data.DEEP_MODULES_V6
    cases = data.CLINICAL_CHALLENGES_V119
    canonical_by_domain = {
        domain: {m.get("topic") for m in topic_list if m.get("topic")}
        for domain, topic_list in modules.items()
    }
    canonical_ids = {
        data._v6_item_id(domain, topic): (domain, topic)
        for domain, topics in canonical_by_domain.items()
        for topic in topics
    }
    covered_ids = {q.get("concept_id") for q in cases if q.get("concept_id")}
    by_concept = defaultdict(list)
    for q in cases:
        by_concept[q.get("concept_id")].append(q)

    print("=== ENT MASTERY CANONICAL VIGNETTE COVERAGE + DEPTH ===")
    print(f"Total curriculum topics: {sum(len(x) for x in canonical_by_domain.values())}")
    print(f"Total vignettes: {len(cases)}")
    print()

    total_topics = total_covered = total_depth2 = 0
    missing_all, singleton = [], []
    for domain, topics in canonical_by_domain.items():
        covered = sorted(t for t in topics if data._v6_item_id(domain, t) in covered_ids)
        missing = sorted(topics - set(covered))
        depth2 = sorted(t for t in topics if len(by_concept.get(data._v6_item_id(domain, t), [])) >= 2)
        domain_singletons = sorted(t for t in topics if len(by_concept.get(data._v6_item_id(domain, t), [])) == 1)
        total_topics += len(topics); total_covered += len(covered); total_depth2 += len(depth2)
        pct = 100.0 * len(covered) / len(topics) if topics else 100.0
        depth_pct = 100.0 * len(depth2) / len(topics) if topics else 100.0
        print(f"DOMAIN|{domain}|{len(covered)}|{len(topics)}|{pct:.1f}%")
        print(f"DEPTH2_DOMAIN|{domain}|{len(depth2)}|{len(topics)}|{depth_pct:.1f}%")
        for topic in missing:
            print(f"MISSING|{domain}|{topic}"); missing_all.append((domain, topic))
        singleton.extend((domain, topic) for topic in domain_singletons)

    print()
    overall = 100.0 * total_covered / total_topics if total_topics else 100.0
    depth_overall = 100.0 * total_depth2 / total_topics if total_topics else 100.0
    print(f"OVERALL|{total_covered}|{total_topics}|{overall:.1f}%")
    print(f"DEPTH2_OVERALL|{total_depth2}|{total_topics}|{depth_overall:.1f}%")
    print(f"MISSING_TOTAL|{len(missing_all)}")

    ids = [q.get("id") for q in cases]
    duplicate_ids = sorted(k for k, n in Counter(ids).items() if k and n > 1)
    orphaned = [q for q in cases if q.get("concept_id") not in canonical_ids]
    malformed = []
    required = ("id", "domain", "topic", "stem", "choices", "answer", "explanation")
    for q in cases:
        absent = [k for k in required if q.get(k) is None]
        choices = q.get("choices") or []; answer = q.get("answer")
        if absent or not isinstance(choices, list) or len(choices) < 2 or not isinstance(answer, int) or not (0 <= answer < len(choices)):
            malformed.append((q.get("id"), absent))

    print(f"ORPHANED|{len(orphaned)}")
    for q in orphaned: print(f"ORPHAN|{q.get('id')}|{q.get('domain')}|{q.get('topic')}|{q.get('concept_id')}")
    print(f"DUPLICATE_IDS|{len(duplicate_ids)}")
    for qid in duplicate_ids: print(f"DUPLICATE|{qid}")
    print(f"MALFORMED|{len(malformed)}")
    for qid, absent in malformed: print(f"BAD_SCHEMA|{qid}|missing={','.join(absent)}")
    print(f"SINGLETON_TOPICS|{len(singleton)}")
    for domain, topic in sorted(singleton): print(f"SINGLETON|{domain}|{topic}")

    focus_counts = Counter(q.get("focus") for q in cases if q.get("focus"))
    focus_by_domain = defaultdict(Counter)
    for q in cases:
        if q.get("focus"):
            focus_by_domain[q.get("domain")][q.get("focus")] += 1
    for focus, count in sorted(focus_counts.items()): print(f"FOCUS|{focus}|{count}")
    for domain in canonical_by_domain:
        c = focus_by_domain[domain]
        print(f"FOCUS_DOMAIN|{domain}|boards={c['boards']}|OR_prep={c['OR_prep']}|overnight_call={c['overnight_call']}|postoperative_call={c['postoperative_call']}")

    material_gaps = []
    if missing_all: material_gaps.append(f"canonical topics missing={len(missing_all)}")
    if singleton: material_gaps.append(f"topics with <2 vignettes={len(singleton)}")

    for domain, mins in FOCUS_MINIMUMS.items():
        for focus, minimum in mins.items():
            actual = focus_by_domain[domain][focus]
            if actual < minimum:
                material_gaps.append(f"{domain}: {focus} {actual}<{minimum}")

    for focus, requirements in CRITICAL_FOCUS.items():
        for domain, topic in requirements:
            cid = data._v6_item_id(domain, topic)
            topic_cases = by_concept.get(cid, [])
            if not topic_cases:
                material_gaps.append(f"critical topic absent: {domain} / {topic}")
                continue
            if not any(q.get("focus") == focus for q in topic_cases):
                material_gaps.append(f"critical {focus} untagged: {domain} / {topic}")

    print(f"MATERIAL_GAPS|{len(material_gaps)}")
    for gap in material_gaps: print(f"MATERIAL_GAP|{gap}")

    if orphaned or duplicate_ids or malformed:
        raise SystemExit(2)
    if material_gaps:
        raise SystemExit(3)


if __name__ == "__main__":
    main()
