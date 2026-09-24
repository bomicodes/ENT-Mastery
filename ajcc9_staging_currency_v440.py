"""v44.0: adopt AJCC 9th Edition as current standard for HPV-mediated oropharyngeal
cancer and salivary gland carcinoma (2026-09-23 audit finding, H&N Oncology domain).

The curriculum's "v40.7 evidence update" notes (authored before AJCC 9 site protocols
were released) taught AJCC 8 as current and treated AJCC 9 as reference-only /
"not yet adopted." Per the American College of Surgeons' own December 9, 2025
announcement (facs.org ACS Brief), the Version 9 Oropharynx (HPV-Associated) and
Salivary Glands protocols went LIVE and became the adopted clinical staging standard,
replacing 8th-edition content, effective January 1, 2026 -- confirmed via
https://www.facs.org/for-medical-professionals/news-publications/news-and-articles/acs-brief/december-9-2025-issue/new-ajcc-staging-system-protocols-for-salivary-glands-and-oropharynx-are-live/ .
As of this curriculum update (2026-09-23), that has been the standard for nearly
9 months, so teaching AJCC 8 as current and AJCC 9 as "awareness only" is now
factually backwards.

Specific staging changes taught here (verified against two independent sources --
Evans et al., "HPV-Associated Oropharyngeal Squamous Cell Carcinoma -- Key Updates
to the AJCC/UICC TNM9 Staging System," Ann Surg Oncol 2026, and a corroborating
head-and-neck-surgery summary; and for salivary glands, "Key Updates on the Version 9
AJCC/UICC Staging System for Salivary Gland Carcinoma," Ann Surg Oncol 2026):

HPV-mediated oropharyngeal SCC:
- cT categories and overall clinical stage-grouping criteria are UNCHANGED from
  AJCC 8.
- Clinical N: unequivocal imaging-detected extranodal extension (iENE) now
  upstages by one N-category (ipsilateral nodes <=6cm + iENE -> cN2; bilateral
  nodes <=6cm + iENE -> cN3). Without iENE, cN1-cN3 are unchanged from AJCC 8.
- Pathologic N: pN1 is now split into pN1a (a single node, no ENE) and pN1b
  (2-4 nodes, no ENE); >4 nodes without ENE remains pN2; pathologic ENE now
  upstages by one level (<=4 nodes + ENE -> pN2; >4 nodes + ENE -> pN3). This
  is the single highest-yield change: AJCC 8 pathologic N-staging for HPV+
  disease IGNORED extranodal extension entirely (unlike HPV-negative disease);
  AJCC 9 now factors it in.
- Pathologic stage grouping: Stage I = pT1-2 N0-N1(a/b); Stage II = pT1-2 N2-N3
  and pT3N2; Stage III = pT3N3 and any pT4.

Salivary gland carcinoma (major and minor glands, now one unified protocol):
- N1 = 1-3 positive nodes without ENE; N2 = more than 3 positive nodes OR any
  ENE (this text was already accurate in the curriculum's "awareness" note --
  only the adoption-status framing needed correcting).
- Stage IV is now restricted to M1 disease only.
"""

MARKER_OLD_HPV = "not yet the adopted clinical standard"
MARKER_OLD_SALIVARY = "not yet this curriculum's adopted clinical standard"
MARKER_OLD_TONSIL = "diagnosed from 2026-01-01"
AJCC9_SOURCE = (
    "American College of Surgeons, AJCC Version 9 Cancer Staging System: "
    "Salivary Glands and Oropharynx (HPV-Associated), effective January 1, 2026: "
    "https://www.facs.org/quality-programs/cancer-programs/american-joint-committee-on-cancer/version-9/"
)

NEW_HPV_WORKUP = (
    "Workup includes complete mucosal examination, tissue diagnosis with p16 testing "
    "in appropriate OPSCC, contrast-enhanced neck imaging and staging chest/PET imaging "
    "as indicated. Assess dentition, nutrition, swallowing, speech, performance status, "
    "smoking history, and baseline hearing/renal function when cisplatin may be "
    "considered. Staging must use the HPV-mediated OPSCC schema rather than applying "
    "the HPV-negative larynx/oral-cavity rules.\n\n"
    "v44.0 evidence update: AJCC 9th Edition is now this curriculum's operative staging "
    "system -- the ACS's Version 9 Oropharynx (HPV-Associated) protocol went live and "
    "replaced 8th-edition content effective January 1, 2026, and is now the adopted "
    "clinical standard. cT categories and overall clinical stage-grouping criteria are "
    "unchanged from AJCC 8. What changed: clinical N now adds an imaging-detected "
    "extranodal extension (iENE) modifier that upstages one N-category when unequivocal "
    "(ipsilateral nodes ≤6cm + iENE → cN2; bilateral nodes ≤6cm + iENE → cN3). "
    "Pathologic N is more consequential: pN1 is now split into pN1a (a single node, no "
    "ENE) and pN1b (2-4 nodes, no ENE); more than 4 nodes without ENE remains pN2; and "
    "pathologic ENE now upstages by one level (≤4 nodes + ENE → pN2; >4 nodes + ENE "
    "→ pN3) -- AJCC 8 ignored ENE entirely in HPV+ pathologic N-staging, so this is the "
    "single highest-yield change to know cold. Record staging edition explicitly and "
    "never combine AJCC 8 and AJCC 9 N-categories or stage groups."
)

NEW_HPV_TEACH = (
    "Boards/chief framework: HPV-associated OPSCC is biologically and prognostically "
    "distinct, but it is still cancer requiring disciplined staging and risk-adapted "
    "therapy. Know p16's staging role, the tendency toward cystic nodal presentation, "
    "and the postoperative features that escalate adjuvant treatment. HPV positivity "
    "improves prognosis; it does not give permission to undertreat outside validated "
    "pathways.\n\n"
    "v44.0 evidence update: Edition check before stage assignment: AJCC 9 is now the "
    "current, adopted staging standard (effective January 1, 2026), replacing AJCC 8. "
    "The board-relevant discriminator is pathologic N: ask whether extranodal extension "
    "is present and how many nodes are involved (1 = pN1a, 2-4 = pN1b, >4 without ENE = "
    "pN2, ≤4 with ENE = pN2, >4 with ENE = pN3) -- AJCC 8 would have ignored ENE here "
    "entirely. Cite AJCC 8 only as a labelled historical comparison, never as the current "
    "answer."
)

NEW_TONSIL_WORKUP = (
    "p16/HPV-aware pathology, imaging and directed primary evaluation.\n\n"
    "v44.0 evidence update: Perform complete mucosal and cranial-nerve examination, "
    "contrast CT or MRI of primary/neck, chest/distant staging as risk dictates, and "
    "p16 testing for oropharyngeal SCC with HPV-specific testing when morphology/site or "
    "institutional protocol requires clarification. For an adult cystic cervical node, "
    "obtain image-guided FNA/core with appropriate HPV-related testing and complete the "
    "unknown-primary pathway before open excision. AJCC 9 is now the current staging "
    "standard for HPV-associated oropharyngeal cancer (effective January 1, 2026, "
    "replacing AJCC 8): cT categories are unchanged, but pathologic N now splits pN1 "
    "into pN1a (1 node, no ENE) and pN1b (2-4 nodes, no ENE), and extranodal extension "
    "upstages pathologic N by one level (≤4 nodes + ENE → pN2; >4 nodes + ENE → pN3) "
    "-- a change AJCC 8 did not make for HPV+ disease. Retain AJCC 8 only as a clearly "
    "labelled historical/board-legacy comparison, and never mix the two systems' nodal "
    "categories or stage groups."
)

NEW_SALIVARY_WORKUP = (
    "Ultrasound-guided FNA or core biopsy establishes a preoperative diagnosis in most "
    "accessible lesions; avoid routine open biopsy of a parotid mass. MRI is favored for "
    "deep-lobe, skull-base and perineural assessment; CT complements bony/chest/staging "
    "questions. Examine and document every facial-nerve division before surgery. Stage "
    "the neck and chest when high-grade or advanced disease makes regional/distant "
    "spread plausible. Pathology should report histologic subtype/grade, margins, "
    "PNI/LVI and nodal ENE.\n\n"
    "v44.0 evidence update: Perform a complete head-and-neck and cranial-nerve "
    "examination, targeted ultrasound with image-guided FNA/core biopsy, MRI for "
    "deep-lobe/perineural/skull-base questions, CT for bone, and risk-directed "
    "chest/distant staging. Report histology, grade, margins, PNI/LVI, nodal ENE, and "
    "actionable biomarkers. AJCC 9th Edition is now this curriculum's operative staging "
    "system -- the ACS's Version 9 salivary-gland protocol went live and replaced "
    "8th-edition content effective January 1, 2026, unifying major- and minor-gland "
    "staging into one protocol; do not default to AJCC 8 or mix categories/stage groups "
    "across the two systems."
)

NEW_SALIVARY_TEACH = (
    "Boards/chief framework: facial function is both a staging clue and an operative "
    "decision point. Preserve a functioning uninvolved nerve; sacrifice grossly invaded "
    "nerve for oncologic control and plan reanimation at the same operation when "
    "possible. High-grade histology, PNI, advanced T stage and nodal disease determine "
    "neck/adjuvant intensity. Adenoid cystic carcinoma's perineural tendency and late "
    "distant relapse make long-term surveillance especially important.\n\n"
    "v44.0 evidence update: AJCC 9 is the current, adopted staging system (effective "
    "January 1, 2026): major and minor salivary carcinomas now share one unified "
    "protocol; T1 is 2 cm or smaller without gross extraparenchymal extension, T2 is "
    "over 2 through 4 cm without it, T3 is over 4 cm or gross extraparenchymal extension "
    "for a major-gland primary; N1 is 1-3 positive nodes without ENE, N2 is more than 3 "
    "positive nodes or any ENE; Stage IV is now restricted to M1 disease only. Cite AJCC "
    "8 only as a labelled historical comparison, and never blend categories across "
    "versions. Separate anatomic stage from histologic biology: adenoid cystic disease "
    "emphasizes perineural and late distant failure, while high-grade carcinomas carry "
    "greater nodal risk."
)


def _update_topic(deep_modules, domain, topic, field_updates):
    for row in deep_modules.get(domain, []):
        if row.get("topic") == topic:
            row.update(field_updates)
            return True
    return False


def apply_ajcc9_staging_currency_v440(data_module, app_module=None):
    deep = data_module.DEEP_MODULES_V6
    result = {"hpv_opscc_updated": False, "tonsil_scc_updated": False, "salivary_updated": False}

    for row in deep.get("Head & Neck Oncology", []):
        if row.get("topic") == "HPV-Associated Oropharyngeal SCC" and MARKER_OLD_HPV in (row.get("workup") or ""):
            row["workup"] = NEW_HPV_WORKUP
            row["teach"] = NEW_HPV_TEACH
            result["hpv_opscc_updated"] = True
            _refresh_sources(row)
        if row.get("topic") == "Tonsil SCC" and MARKER_OLD_TONSIL in (row.get("workup") or ""):
            row["workup"] = NEW_TONSIL_WORKUP
            result["tonsil_scc_updated"] = True
            _refresh_sources(row)

    for row in deep.get("Thyroid / Parathyroid / Salivary", []):
        if row.get("topic") == "Salivary Gland Malignancy" and MARKER_OLD_SALIVARY in (row.get("workup") or ""):
            row["workup"] = NEW_SALIVARY_WORKUP
            row["teach"] = NEW_SALIVARY_TEACH
            result["salivary_updated"] = True
            _refresh_sources(row)

    # The imaging lab also presents AJCC 8 as the current system for HPV+ OPSCC.
    # Preserve its explicitly labelled historical comparison while teaching the
    # imaging-detected ENE rule used by the current Version 9 protocol.
    for case in data_module.INTERPRETATION_LABS.get("head-neck-imaging", {}).get("cases", []):
        if case.get("id") == "hn2":
            case["staging_edition"] = "AJCC Version 9 (HPV-associated oropharynx; effective 2026-01-01)"
            if "AJCC Version 9 adds" not in case.get("answer", ""):
                case["answer"] += (
                    " AJCC Version 9 adds imaging-detected extranodal extension "
                    "(iENE) as a clinical N modifier: unequivocal iENE raises the "
                    "N category one level. The AJCC 8 categories above are a "
                    "historical comparison, not the current staging answer."
                )
        elif case.get("id") in ("hn3", "hn4", "hn11"):
            case["staging_edition"] = "AJCC 8 (current protocol for this disease site)"
    if app_module is not None:
        app_module.INTERPRETATION_LABS = data_module.INTERPRETATION_LABS

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = deep
    return result


def _refresh_sources(row):
    sources = row.get("source_basis") or []
    row["source_basis"] = [
        source for source in sources
        if not ("awareness only" in source or "not yet the adopted" in source)
    ]
    if AJCC9_SOURCE not in row["source_basis"]:
        row["source_basis"].append(AJCC9_SOURCE)
