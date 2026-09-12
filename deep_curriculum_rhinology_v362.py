"""v36.2 — source-grounded Revision FESS diagnostic and operative decision depth.

The existing canonical Revision FESS ladder already teaches the key senior principle that
revision surgery should correct the mechanism of failure rather than simply repeat or
maximize prior surgery. This bounded successor keeps that strong material and adds the
missing systematic revision framework: re-verify the diagnosis/phenotype, identify the
specific anatomic or nonanatomic failure mechanism, map altered anatomy with endoscopy and
fine-cut CT, preserve functioning prior surgery, and stop/reorient when scarred landmarks
make orbit/skull base/vascular dissection unsafe. No canonical topic is added or renamed.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "Revision FESS"

SOURCES_V362 = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e — revision endoscopic sinus surgery, residual anatomy, scar/osteitis, frontal and sphenoid revision principles, complications, and image-guided orientation. Connected Google Drive file id 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t.",
    "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — revision sinus evaluation, recurrent/persistent CRS, altered anatomy and operative safety. Connected Google Drive file id 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "K.J. Lee's Essential Otolaryngology, 12e — ESS failure mechanisms, postoperative anatomy, recurrent disease and revision principles. Connected Google Drive file id 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
    "Shin JJ et al. Clinical Practice Guideline: Surgical Management of Chronic Rhinosinusitis. Otolaryngol Head Neck Surg. 2025;172 Suppl 2:S1-S47. PMID 40424072; doi:10.1002/ohn.1287 — verify CRS/candidacy, fine-cut CT for planning, disease-appropriate extent, postoperative care and outcome follow-up.",
    "Shin JJ et al. Executive Summary of the Clinical Practice Guideline on the Surgical Management of Chronic Rhinosinusitis. Otolaryngol Head Neck Surg. 2025;172(6):1807-1832. PMID 40437675; doi:10.1002/ohn.1286 — KAS 7-11 operative planning, extent, counseling and follow-up.",
    "Bewick J et al. Anatomic findings in revision endoscopic sinus surgery: Case series and review of contributory factors. Allergy Rhinol (Providence). 2016;7(3):151-157. PMID 28107148 — residual uncinate, non-natural-ostium antrostomy, synechiae, middle-meatal stenosis and osteitis as recurrent revision findings.",
    "Englhard AS, Ledderose GJ. Anatomical findings in patients with chronic rhinosinusitis without nasal polyps requiring revision surgery. Braz J Otorhinolaryngol. 2023;89(4):101287. PMID 37442058 — incomplete ethmoidectomy, residual uncinate, middle-turbinate lateralization, frontal-recess scarring and stenosis in revision CRSsNP.",
]

FOUNDATION_ADD = (
    " FOUNDATION — PERSISTENT SYMPTOMS AFTER ESS DO NOT AUTOMATICALLY MEAN 'FAILED SURGERY.' "
    "Revision evaluation starts by naming the failure mechanism: persistent/residual disease from unopened or incompletely opened anatomy; recurrent inflammatory disease such as polyposis/AERD; scar, synechiae or ostial stenosis; maxillary recirculation from an antrostomy that does not incorporate the natural ostium; retained uncinate or ethmoid/frontal partitions; middle-turbinate lateralization; osteitis; untreated sphenoid/frontal disease; odontogenic, fungal, neoplastic or host-factor disease; inadequate topical delivery/adherence; or a NONRHINOGENIC symptom generator such as migraine/neuralgia. A technically patent cavity plus discordant symptoms is a reason to reconsider the diagnosis, not an automatic indication for more surgery."
)

WORKUP_ADD = (
    " APPLICATION — reconstruct what happened before planning what to revise. Review the original operative note, pathology/cultures, prior CT, postoperative endoscopy, complications, disease phenotype, treatment adherence and the duration/quality of any postoperative improvement. Perform current nasal endoscopy and obtain a FINE-CUT sinus CT for revision planning. On imaging/endoscopy deliberately trace the natural maxillary ostium and prior antrostomy for recirculation, residual uncinate, retained anterior/posterior ethmoid or frontal-recess cells, middle-turbinate position, synechiae/stenosis, osteitic partitions, persistent sphenoid/frontal disease, and altered orbit/skull-base boundaries. Re-open dental source, fungal disease, unilateral tumor, immune/CF/PCD, AERD/type-2 inflammation and nonrhinogenic facial-pain/headache pathways when the pattern demands them."
)

MANAGE_ADD = (
    " MANAGEMENT DECISION — correct the demonstrated driver before committing the patient to another operation. Optimize topical anti-inflammatory delivery and phenotype-specific therapy; coordinate dental source control, host-factor treatment, AERD/CRSwNP strategy or other disease-specific care when those mechanisms dominate. If prior sinus openings are patent and the remaining symptoms are not explained by objective sinonasal disease, do not revise normal/patent anatomy simply because the patient has had ESS before. Revision is appropriate when a defined surgically correctable target remains and the expected benefit outweighs the added risk of scarred anatomy."
)

OPERATE_ADD = (
    " SENIOR OPERATIVE DECISION — make revision surgery HYPOTHESIS-DRIVEN and anatomy-specific. Preserve working prior openings and remove only the residual/scarred partitions or diseased tissue needed to restore the intended drainage pathway, topical access and disease control. For maxillary recirculation, connect the accessory/prior opening to the TRUE natural ostium rather than enlarging the wrong window. In frontal, ethmoid and sphenoid revision, use the preoperative CT as an active surgical map because normal landmarks may be absent or distorted; re-establish reliable landmarks before advancing through scar. Altered lamina, skull base, optic/carotid relationships, prior turbinate loss, osteitis and dehiscence lower the threshold for image guidance and for changing the corridor or extent. DANGER-ZONE / BAILOUT RULE: if orientation becomes uncertain near orbit, skull base, carotid, optic nerve or a suspected dehiscence, STOP dissection, control bleeding, re-localize using fixed landmarks plus imaging/navigation and angled visualization, and defer unsafe tissue removal rather than converting uncertainty into a CSF, orbital or vascular injury."
)

TEACH_ADD = (
    " Chief rule: A GOOD REVISION OPERATION STARTS WITH A NEW HYPOTHESIS. Ask whether the problem is residual anatomy, scar/stenosis/recirculation, recurrent inflammatory biology, an untreated focal/host source, poor topical access/adherence, or a non-sinus diagnosis. Endoscopy plus fine-cut CT define the correctable target; prior records explain how the anatomy got there. Preserve what works, fix only what is causally wrong, and treat loss of orientation in scarred danger zones as a reason to stop and re-map—not as a reason to dissect harder. After revision, longitudinal topical therapy and 3–12 month symptom/QOL plus endoscopic outcome assessment remain part of the operation's success."
)


def _append(row, field, text):
    existing = str(row.get(field) or "")
    if text not in existing:
        row[field] = existing + text


def apply_rhinology_revision_fess_depth_v362(data_module, app_module=None):
    rows = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    by_topic = {str(r.get("topic") or ""): r for r in rows}
    if len(rows) != 42 or len(by_topic) != 42:
        raise RuntimeError(f"v36.2 requires exact 42-topic Rhinology inventory; got rows={len(rows)} unique={len(by_topic)}")
    if TOPIC not in by_topic:
        raise RuntimeError(f"v36.2 missing exact canonical target: {TOPIC!r}")

    row = by_topic[TOPIC]
    if row.get("source_grounded_v362"):
        return {"patched": [], "already_applied": [TOPIC]}

    _append(row, "recognize", FOUNDATION_ADD)
    _append(row, "workup", WORKUP_ADD)
    _append(row, "manage", MANAGE_ADD)
    _append(row, "operate", OPERATE_ADD)
    _append(row, "teach", TEACH_ADD)

    source_basis = list(row.get("source_basis") or [])
    for source in SOURCES_V362:
        if source not in source_basis:
            source_basis.append(source)
    row["source_basis"] = source_basis
    row["source_grounded_v362"] = True
    row["source_metadata_v362"] = {
        "canonical_link": {"domain": DOMAIN, "topic": TOPIC},
        "textbook_drive_ids": {
            "cummings_7e": "18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t",
            "pasha_6e": "14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52",
            "kj_lee_12e": "112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR",
        },
        "preserved_ladder_ids": ["v136_rhi_23", "v142_rhi_04", "v209_rhi_revision_snr"],
        "guideline_pmids": ["40424072", "40437675"],
        "revision_anatomy_pmids": ["28107148", "37442058"],
    }
    row["deliberate_review_v362"] = {
        "foundation": "separate true surgical/anatomic failure from recurrent inflammatory, focal/host-factor and nonrhinogenic causes",
        "application": "reconstruct prior surgery and map exact revision targets with endoscopy, prior records and fine-cut CT",
        "senior_decision": "hypothesis-driven limited-to-needed revision with explicit altered-landmark orbit/skull-base/vascular stop-and-reorient bailout",
        "traps": [
            "assuming any postoperative symptom means the original operation failed",
            "repeating a technically patent operation without a new mechanism",
            "missing maxillary recirculation because the natural ostium was not incorporated",
            "ignoring residual uncinate or retained ethmoid/frontal partitions",
            "overlooking middle-turbinate lateralization, synechiae or stenosis",
            "treating recurrent type-2 inflammatory biology as anatomy alone",
            "missing odontogenic, fungal, neoplastic or host-factor disease",
            "operating on facial pain/headache discordant with objective disease",
            "planning extent from CT opacity alone rather than disease and anatomy",
            "continuing scar dissection after reliable landmarks are lost",
        ],
    }

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": [TOPIC], "canonical_id": data_module._v6_item_id(DOMAIN, TOPIC)}
