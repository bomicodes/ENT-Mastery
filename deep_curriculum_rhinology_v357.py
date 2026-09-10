"""v35.7 — lesion-specific depth for the exact Benign Sinonasal Tumor Framework.

This bounded pass intentionally reuses the v35.6 unilateral-mass safety framework and
adds only lesion-specific foundation -> application -> senior-decision depth for inverted
papilloma (IP), juvenile nasopharyngeal angiofibroma (JNA), and osteoma. It adds, removes,
or renames no canonical topic.

Textbook anchors: Cummings Otolaryngology—Head and Neck Surgery 7e, K.J. Lee's
Essential Otolaryngology 12e, and Pasha Clinical Reference Guide 6e. Contemporary tumor
principles are cross-checked against the 2024 International Consensus Statement on Allergy
and Rhinology: Sinonasal Tumors and the 2026 multidisciplinary consensus on sinonasal-mass
workup.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
TARGET = "Benign Sinonasal Tumor Framework"

SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e — Chapter 50 Benign Tumors of the Sinonasal Tract: IP attachment-directed resection and underlying bone treatment; JNA evaluation/vascular planning; osteoma observation versus symptom- or obstruction-driven surgery",
    "K.J. Lee's Essential Otolaryngology, 12e — benign sinonasal neoplasms, inverted papilloma, juvenile angiofibroma, and osteoma clinical framework",
    "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — unilateral nasal mass differential; papilloma and juvenile nasopharyngeal angiofibroma recognition and management pearls",
    "Kuan EC et al. International Consensus Statement on Allergy and Rhinology: Sinonasal Tumors. Int Forum Allergy Rhinol. 2024;14(2):149-608. PMID 37658764. doi:10.1002/alr.23262 — benign-neoplasm, biopsy, angiofibroma, inverted-papilloma, surgery, and surveillance consensus",
    "London NR Jr et al. Multidisciplinary Consensus Statement for Appropriate Evaluation and Workup of Sinonasal Masses. JAMA Otolaryngol Head Neck Surg. 2026;152(7):714-721. PMID 42207510. doi:10.1001/jamaoto.2026.1185 — current mass evaluation, imaging, biopsy, pathology, and workup consensus",
]

RECOGNIZE = (
    " FOUNDATION — BENIGN SINONASAL TUMORS are not one biologic entity. INVERTED PAPILLOMA is a benign but locally aggressive Schneiderian tumor with meaningful residual/recurrence risk and potential synchronous or subsequent squamous malignancy; a unilateral polypoid mass therefore needs tumor-level evaluation rather than routine CRSwNP assumptions. JUVENILE NASOPHARYNGEAL ANGIOFIBROMA is the classic hypervascular tumor of an adolescent male with progressive unilateral obstruction and recurrent epistaxis. OSTEOMA is a slow-growing bone-density lesion, often incidental in the frontal/ethmoid sinuses, whose mere presence on CT is not itself an indication for surgery."
)

LOCALIZE = (
    " APPLICATION — make localization change the operation. For IP, use CT for bony anatomy and attachment clues and MRI when tumor extent, skull-base/orbital relationship, or distinction from retained secretions is important; the surgical target is the ATTACHMENT, not simple debulking. For a suspected JNA, recognize the vascular phenotype and map extent/feeding vessels before tissue manipulation. For osteoma, define sinus of origin, frontal-recess/outflow relationship, orbital or skull-base proximity, and whether the lesion is actually causing obstruction or symptoms before attributing nonspecific headache to it."
)

WORKUP = (
    " SENIOR WORKUP DECISION — a convincing JNA phenotype is a DO-NOT-CASUALLY-BIOPSY problem: obtain contrast-enhanced cross-sectional imaging and vascular planning rather than provoking major hemorrhage with routine office tissue sampling. IP generally requires histologic confirmation when safe, but preoperative imaging should first exclude vascular or intracranial continuity and help map attachment/extension. For osteoma, serial observation is appropriate for many incidental, asymptomatic lesions; intervene when growth, sinus-outflow obstruction, recurrent secondary disease, deformity, orbital effects, neurologic/skull-base consequences, or another clearly attributable problem changes the risk-benefit balance."
)

MANAGE = (
    " SENIOR MANAGEMENT — treat IP with complete attachment-oriented resection rather than piecemeal debulking alone: remove involved mucosa/periosteum at the attachment and address underlying bone when required by the attachment pattern, then maintain endoscopic and/or imaging surveillance because recurrence can be delayed and malignant transformation/coexistent SCC matters. JNA management is stage- and anatomy-dependent, usually centered on definitive resection in appropriate candidates with multidisciplinary vascular planning and selective preoperative embolization when its expected blood-loss benefit outweighs embolization risk. Osteoma management is observation versus anatomy-directed resection, not automatic surgery for an incidental radiographic diagnosis."
)

OPERATE = (
    " OPERATIVE DANGER / BAILOUT — if a presumed benign unilateral lesion bleeds unexpectedly, has imaging features of marked vascularity, or appears continuous with skull base/intracranial structures, STOP routine biopsy/debulking and re-establish vascular/skull-base-safe planning. For IP, failure to identify and treat the attachment is a recurrence setup; choose an endoscopic, open, or combined corridor based on access to the attachment and critical boundaries rather than on a dogmatic approach label. For osteoma, do not trade an asymptomatic benign lesion for unnecessary frontal-recess, orbital, skull-base, or cosmetic morbidity when observation remains safer."
)

TEACH = (
    " Chief rule: BENIGN does not mean one management pathway. IP = FIND/TREAT THE ATTACHMENT + SURVEIL; JNA = HYPERVASCULAR, IMAGE/PLAN BEFORE TISSUE, CONTROL BLOOD-LOSS RISK; OSTEOMA = OBSERVE MOST INCIDENTAL LESIONS, OPERATE FOR A REAL ANATOMIC/CLINICAL INDICATION. This card deliberately hands generic unilateral-mass imaging and unsafe-biopsy triage back to the v35.6 Unilateral Sinonasal Disease card and owns only the lesion-specific decisions that follow."
)


def _append(row, field, text):
    existing = str(row.get(field) or "")
    if text not in existing:
        row[field] = existing + text


def apply_rhinology_benign_tumor_v357(data_module, app_module=None):
    rows = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    by_topic = {str(r.get("topic") or ""): r for r in rows}
    if len(rows) != 42 or len(by_topic) != 42:
        raise RuntimeError(f"v35.7 requires exact 42-topic Rhinology inventory; got rows={len(rows)} unique={len(by_topic)}")
    if TARGET not in by_topic:
        raise RuntimeError(f"v35.7 missing exact canonical target: {TARGET!r}")

    row = by_topic[TARGET]
    if not row.get("source_grounded_v357"):
        for field, text in (
            ("recognize", RECOGNIZE),
            ("localize", LOCALIZE),
            ("workup", WORKUP),
            ("manage", MANAGE),
            ("operate", OPERATE),
            ("teach", TEACH),
        ):
            _append(row, field, text)
        source_basis = list(row.get("source_basis") or [])
        for source in SOURCES:
            if source not in source_basis:
                source_basis.append(source)
        row["source_basis"] = source_basis
        row["source_grounded_v357"] = True
        row["deliberate_review_v357"] = {
            "foundation": "Separate IP, JNA, and osteoma by biology and natural history rather than teaching a generic benign-mass bucket.",
            "application": "Use attachment/vascularity/outflow localization to change biopsy, imaging, surveillance, and operative planning.",
            "senior_decision": "IP attachment treatment and surveillance; JNA no-casual-biopsy/vascular planning; osteoma observation versus indication-driven resection.",
        }

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": [TARGET], "count": 1}
