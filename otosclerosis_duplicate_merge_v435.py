"""v43.5: clean up the last traces of the retired "Otosclerosis" topic.

Requested 2026-09-22 (site audit): raw data.py still defines two separate rows
for the same disease -- "Otosclerosis" (a thin, largely auto-generated stub)
and "Otosclerosis / Stapes Fixation" (the fully developed, evidence-calibrated
card). Checking the fully patched live app (not raw data.py) showed the
existing v16.6 canonicalization pass (deep_curriculum_canonicalize_v166.py,
CANONICAL_MERGES_V166) already retires the "Otosclerosis" DEEP_MODULES_V6 row
and repoints every CLINICAL_CHALLENGES_V119/CONCEPT_CHECKS_V112 item's
concept_id to the canonical id -- so this is NOT the 349-topic-affecting
consolidation it first looked like (topic count is untouched: still 349,
Otology / Neurotology still 53).

What v166's _repoint_linked_records() does NOT do is deduplicate or relabel
the question-bank rows themselves: it updates concept_id and adds a
"canonical_topic" field, but leaves "topic" as the stale "Otosclerosis" label
and leaves both the two now-redundant Concept Checks AND the richer pair
already filed under "Otosclerosis / Stapes Fixation" live side by side under
the same concept -- genuine duplicate content a resident would see twice.
This module finishes that cleanup:
1. Removes the two Concept Checks auto-generated under the stale topic label
   (cc-v112-rec/mgt-...-otosclerosis), since near-identical, better-written
   counterparts already exist under the canonical topic
   (cc-v112-rec/mgt-...-otosclerosis-stapes-fixation).
2. Relabels the one genuinely valuable item still carrying the stale label --
   a curated Clinical Challenge vignette (v11_oto_03) with real stem/curveball
   content not duplicated anywhere else -- so its display "topic" matches its
   already-correct concept_id instead of showing "Otosclerosis".
3. Also removes the (already-orphaned, always a no-op by the time this runs)
   DEEP_MODULES_V6 "Otosclerosis" row as a defensive no-op, in case a future
   change to the patch order ever runs this before v166.
"""

import re

THIN_TOPIC = "Otosclerosis"
MERGED_TOPIC = "Otosclerosis / Stapes Fixation"
DOMAIN = "Otology / Neurotology"

DUPLICATE_CONCEPT_CHECK_IDS = [
    "cc-v112-rec-otology-neurotology-otosclerosis",
    "cc-v112-mgt-otology-neurotology-otosclerosis",
]

REPOINT_CHALLENGE_ID = "v11_oto_03"


def _v6_item_id(domain, topic):
    return "v6-" + re.sub(r"[^a-z0-9]+", "-", (domain + "-" + topic).lower()).strip("-")


def apply_otosclerosis_duplicate_merge_v435(data_module, app_module=None):
    modules = data_module.DEEP_MODULES_V6
    bucket = modules.get(DOMAIN, [])
    result = {"thin_row_removed": False, "concept_checks_removed": [], "challenge_repointed": False}

    before = len(bucket)
    bucket[:] = [r for r in bucket if r.get("topic") != THIN_TOPIC]
    if len(bucket) != before:
        result["thin_row_removed"] = True
    modules[DOMAIN] = bucket

    checks = data_module.CONCEPT_CHECKS_V112
    before_checks = len(checks)
    kept = [q for q in checks if q.get("id") not in DUPLICATE_CONCEPT_CHECK_IDS]
    if len(kept) != before_checks:
        result["concept_checks_removed"] = [qid for qid in DUPLICATE_CONCEPT_CHECK_IDS
                                             if qid not in {q.get("id") for q in kept}]
    checks[:] = kept

    challenges = data_module.CLINICAL_CHALLENGES_V119
    for q in challenges:
        if q.get("id") == REPOINT_CHALLENGE_ID and q.get("topic") != MERGED_TOPIC:
            q["topic"] = MERGED_TOPIC
            q["concept_id"] = _v6_item_id(q.get("domain", DOMAIN), MERGED_TOPIC)
            result["challenge_repointed"] = True
            break

    data_module.CONCEPT_CHECK_BY_ID_V112 = {q["id"]: q for q in checks if q.get("id")}
    data_module.CLINICAL_CHALLENGE_BY_ID_V119 = {q["id"]: q for q in challenges if q.get("id")}
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = modules
        app_module.CONCEPT_CHECKS_V112 = checks
        app_module.CONCEPT_CHECK_BY_ID_V112 = data_module.CONCEPT_CHECK_BY_ID_V112
        app_module.CLINICAL_CHALLENGES_V119 = challenges
        app_module.CLINICAL_CHALLENGE_BY_ID_V119 = data_module.CLINICAL_CHALLENGE_BY_ID_V119
    return result
