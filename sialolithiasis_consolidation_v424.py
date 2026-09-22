"""v42.4: consolidate sialolithiasis into a single gland-agnostic topic.

Requested 2026-09-21: rather than two separate cards ("Submandibular
Sialolithiasis" and the v42.3-added "Parotid Sialolithiasis / Stensen Duct
Stones"), combine all sialolithiasis content -- submandibular AND parotid --
under one "Sialolithiasis" topic, the way a resident would actually think
about the disease (one entity, gland-specific management nuances).

This module:
1. Renames the existing "Submandibular Sialolithiasis" row to "Sialolithiasis"
   and appends the parotid-specific content (Stensen duct anatomy, why open
   sialolithotomy is a poor choice specifically for parotid stones, and
   lithotripsy indications) into each of its six fields as a labeled
   addendum, so the single topic now genuinely covers both glands.
2. Removes the standalone "Parotid Sialolithiasis / Stensen Duct Stones" row
   added by v42.3.
3. Repoints the v42.3 Clinical Challenge that was filed under the standalone
   parotid topic to the merged "Sialolithiasis" topic/concept id, so it still
   surfaces on the merged concept page. The question content is unchanged.

Net topic-count effect: 349 -> 348 (Thyroid/Parathyroid/Salivary 36 -> 35,
undoing the v42.3 +1 for the now-removed standalone parotid card).
"""

import re


MERGED_TOPIC_NAME = "Sialolithiasis"
OLD_SUBMANDIBULAR_NAME = "Submandibular Sialolithiasis"
OLD_PAROTID_NAME = "Parotid Sialolithiasis / Stensen Duct Stones"
DOMAIN = "Thyroid / Parathyroid / Salivary"

MERGE_MARKER = "PAROTID STONES"

RECOGNIZE_ADDITION = (
    " PAROTID STONES: parotid (Stensen duct) stones are far less common than submandibular stones (roughly "
    "80-90% of sialoliths are submandibular) because parotid saliva is more serous/less mucinous and Stensen "
    "duct has no antigravity segment. They present with the same meal-provoked pattern but as preauricular/"
    "cheek swelling; palpate along the duct's course from the papilla opposite the second maxillary molar back "
    "across the masseter."
)

LOCALIZE_ADDITION = (
    " Stensen duct runs across the masseter, then turns medially through buccinator to pierce the buccal "
    "mucosa; parotid stones can lodge anywhere from the papilla to the hilum. The decisive anatomic difference "
    "from submandibular disease is that the facial nerve's buccal and zygomatic branches interdigitate "
    "directly over and around the parotid gland and duct, so any open approach aimed at the duct or gland "
    "carries a facial-nerve risk that transoral Wharton duct surgery does not share."
)

WORKUP_ADDITION = (
    " The same ultrasound-first, CT-when-needed approach applies to parotid stones; define stone size, "
    "mobility, number, and distance from the papilla, since these determine whether pure endoscopic retrieval "
    "is realistic for either gland."
)

MANAGE_ADDITION = (
    " PAROTID-SPECIFIC MANAGEMENT: escalate from least to most invasive rather than defaulting to open "
    "surgery. Sialendoscopy is first-line definitive treatment for accessible parotid stones. OPEN "
    "SIALOLITHOTOMY (incising the duct to remove a stone) is a poor primary choice specifically for PAROTID "
    "stones, for reasons distinct from submandibular disease: (1) the buccal and zygomatic facial-nerve "
    "branches cross directly over Stensen duct, so open dissection down to the duct risks facial nerve injury "
    "with no equivalent risk in transoral submandibular duct surgery; (2) only the short distal segment of "
    "Stensen duct is reachable without deep parotid dissection, so many parotid stones sit more proximally "
    "within or near the gland, meaning an open approach for a proximal parotid stone effectively commits to "
    "parotid-level dissection rather than the simple, low-morbidity duct-slitting used for distal submandibular "
    "stones; (3) duct injury, stricture, and salivary fistula after open parotid duct surgery are "
    "proportionally harder to salvage than after submandibular duct work. Lithotripsy is indicated for either "
    "gland when a stone is too large or too adherent/impacted for intact basket capture, rather than forcing "
    "repeated traumatic basket attempts that risk duct avulsion."
)

OPERATE_ADDITION = (
    " For parotid stones, sialendoscopic basket or wire retrieval handles small, mobile stones; add "
    "intracorporeal lithotripsy (holmium or pulsed-dye laser fragmentation, or pneumatic lithotripsy) under "
    "direct endoscopic vision for larger or impacted stones, fragmenting them into basket-retrievable pieces "
    "in the same setting. Extracorporeal shock-wave lithotripsy (ESWL) is an older, less widely available "
    "alternative largely supplanted by intracorporeal technique. A combined approach -- endoscopic "
    "localization plus limited transfacial or intraoral access with facial-nerve monitoring when a facial "
    "incision is used -- is reserved for very proximal or partially intraparenchymal parotid stones; formal "
    "parotidectomy is the last resort."
)

TEACH_ADDITION = (
    " Boards/chief framework for PAROTID stones specifically: escalate hydration/massage -> sialendoscopy "
    "alone -> sialendoscopy plus intracorporeal lithotripsy -> combined endoscopic-assisted transfacial "
    "approach with nerve monitoring -> parotidectomy (last resort). Open sialolithotomy is the wrong reflex "
    "for parotid stones because it exposes facial nerve branches for a problem sialendoscopy usually solves; "
    "it remains reasonable for accessible distal submandibular (Wharton duct) stones, where only the lingual "
    "nerve, and only in the posterior floor of mouth, is at risk."
)

TAGS_TO_ADD = ["parotid sialolithiasis", "Stensen duct", "lithotripsy", "sialolithotomy", "facial nerve"]

SOURCE_BASIS_ADDITION = (
    "Cummings 7e — parotid vs. submandibular sialolithiasis, Stensen duct anatomy, and gland-preserving vs. "
    "open management including lithotripsy indications."
)

REPOINT_CHALLENGE_ID = "v423-sialolithiasis-parotid-open-01"


def _v6_item_id(domain, topic):
    return "v6-" + re.sub(r"[^a-z0-9]+", "-", (domain + "-" + topic).lower()).strip("-")


def apply_sialolithiasis_consolidation_v424(data_module, app_module=None):
    modules = data_module.DEEP_MODULES_V6
    result = {"merged": False, "parotid_row_removed": False, "challenge_repointed": False}

    bucket = modules.setdefault(DOMAIN, [])

    merged_row = next((r for r in bucket if r.get("topic") in (MERGED_TOPIC_NAME, OLD_SUBMANDIBULAR_NAME)), None)
    if merged_row is not None and MERGE_MARKER not in (merged_row.get("recognize") or ""):
        merged_row["topic"] = MERGED_TOPIC_NAME
        merged_row["recognize"] = (merged_row.get("recognize") or "").rstrip() + RECOGNIZE_ADDITION
        merged_row["localize"] = (merged_row.get("localize") or "").rstrip() + LOCALIZE_ADDITION
        merged_row["workup"] = (merged_row.get("workup") or "").rstrip() + WORKUP_ADDITION
        merged_row["manage"] = (merged_row.get("manage") or "").rstrip() + MANAGE_ADDITION
        merged_row["operate"] = (merged_row.get("operate") or "").rstrip() + OPERATE_ADDITION
        merged_row["teach"] = (merged_row.get("teach") or "").rstrip() + TEACH_ADDITION
        tags = merged_row.setdefault("tags", [])
        for tag in TAGS_TO_ADD:
            if tag not in tags:
                tags.append(tag)
        sources = merged_row.setdefault("source_basis", [])
        if SOURCE_BASIS_ADDITION not in sources:
            sources.append(SOURCE_BASIS_ADDITION)
        metadata = merged_row.get("source_metadata_v408")
        if isinstance(metadata, dict):
            metadata["canonical_topic"] = MERGED_TOPIC_NAME
            metadata["reviewed_after"] = "v42.4"
        result["merged"] = True
    elif merged_row is not None:
        merged_row["topic"] = MERGED_TOPIC_NAME

    before = len(bucket)
    bucket[:] = [r for r in bucket if r.get("topic") != OLD_PAROTID_NAME]
    if len(bucket) != before:
        result["parotid_row_removed"] = True
    modules[DOMAIN] = bucket

    challenges = data_module.CLINICAL_CHALLENGES_V119
    for q in challenges:
        if q.get("id") == REPOINT_CHALLENGE_ID and q.get("topic") != MERGED_TOPIC_NAME:
            q["topic"] = MERGED_TOPIC_NAME
            q["concept_id"] = _v6_item_id(q.get("domain", DOMAIN), MERGED_TOPIC_NAME)
            result["challenge_repointed"] = True
            break

    data_module.CLINICAL_CHALLENGE_BY_ID_V119 = {
        q["id"]: q for q in challenges if q.get("id")
    }
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = modules
        app_module.CLINICAL_CHALLENGES_V119 = challenges
        app_module.CLINICAL_CHALLENGE_BY_ID_V119 = data_module.CLINICAL_CHALLENGE_BY_ID_V119
    return result
