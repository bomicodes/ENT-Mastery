"""v36.7 — connect CSF Rhinorrhea diagnosis to endoscopic skull-base repair decisions.

Preserves the exact 42-topic Rhinology inventory and the separate canonical ownership of
CSF Rhinorrhea versus Endoscopic CSF Leak Repair / Nasoseptal Flap. Adds only clinically
high-yield diagnostic -> operative handoff, recurrence/IIH reasoning, reconstruction
selection, and visible source provenance.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
DIAG_TOPIC = "CSF Rhinorrhea"
OP_TOPIC = "Endoscopic CSF Leak Repair / Nasoseptal Flap"

TEXTBOOKS = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — anterior skull-base CSF leak diagnosis, localization, spontaneous-leak/IIH framework, endoscopic repair and vascularized reconstruction principles. Connected Google Drive ID 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t.",
    "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e (2022) — CSF rhinorrhea differential, skull-base evaluation and resident-level repair principles. Connected Google Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "K.J. Lee's Essential Otolaryngology, 12e — CSF rhinorrhea, skull-base defects, encephaloceles and endoscopic repair principles. Connected Google Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
]
GUIDANCE = [
    "Georgalas C, et al. International Consensus Statement: Spontaneous Cerebrospinal Fluid Rhinorrhea. Int Forum Allergy Rhinol. 2021;11:794-803. PMID 33099888; doi:10.1002/alr.22704 — thin-slice CT/MRI localization, prompt closure, IIH assessment and recurrence prevention.",
    "Outcomes of Endoscopic Management of Spontaneous Cerebrospinal Fluid Rhinorrhea: A Meta-Analysis. 2025. PMID 40650638 — high endoscopic repair success; multilayer reconstruction favored numerically; routine lumbar drainage did not significantly improve success.",
]


def _append(row, field, addition, marker):
    current = str(row.get(field) or "")
    if marker.lower() not in current.lower():
        row[field] = (current.rstrip() + ("\n\n" if current.strip() else "") + addition).strip()


def _add_sources(row, metadata_key, scope):
    sources = list(row.get("source_basis") or [])
    for source in TEXTBOOKS + GUIDANCE:
        if source not in sources:
            sources.append(source)
    row["source_basis"] = sources
    row[metadata_key] = {
        "textbook_drive_ids": {
            "cummings_7e": "18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t",
            "pasha_6e": "14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52",
            "kj_lee_12e": "112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR",
        },
        "guidance": ["International spontaneous CSF rhinorrhea consensus PMID 33099888", "2025 endoscopic outcomes meta-analysis PMID 40650638"],
        "scope": scope,
    }


def apply_rhinology_csf_leak_v367(data_module, app_module=None):
    rows = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    by_topic = {str(row.get("topic") or ""): row for row in rows}
    if len(rows) != 42 or len(by_topic) != 42:
        raise RuntimeError(f"v36.7 requires exact 42-topic Rhinology inventory; got rows={len(rows)} unique={len(by_topic)}")
    for topic in (DIAG_TOPIC, OP_TOPIC):
        if topic not in by_topic:
            raise RuntimeError(f"v36.7 missing exact canonical target: {topic!r}")

    diag = by_topic[DIAG_TOPIC]
    _append(diag, "recognize", "FOUNDATION HANDOFF — CSF rhinorrhea (cerebrospinal fluid rhinorrhea, CSF leak, skull-base leak) should be suspected with persistent unilateral clear watery drainage that is positional or provoked by bending/straining, particularly after trauma or sinonasal/skull-base surgery, or when accompanied by a meningoencephalocele. Salty/metallic drainage is supportive but not diagnostic. Recurrent meningitis, pneumocephalus, severe headache, neurologic change or visual symptoms are danger features rather than routine-rhinitis findings.", "foundation handoff")
    _append(diag, "workup", "APPLICATION HANDOFF — confirm suspected nasal CSF with a CSF-specific laboratory marker such as beta-2 transferrin when fluid can be collected; do not diagnose a cranial leak from glucose testing or appearance alone. Use thin-slice high-resolution CT to map bony skull-base defects and add MRI with appropriate high-resolution fluid-sensitive sequences when an encephalocele/meningoencephalocele, soft-tissue lesion, multiple candidate defects or uncertain localization remains. Distinguish traumatic/iatrogenic from spontaneous leaks. In spontaneous CSF rhinorrhea, actively assess for coexisting idiopathic intracranial hypertension with headache, pulsatile tinnitus, visual symptoms, empty-sella/other imaging clues and neuro-ophthalmic evaluation when indicated; recurrence prevention requires attention to the pressure disorder rather than closure alone.", "application handoff")
    _append(diag, "manage", "MANAGEMENT HANDOFF — persistent confirmed cranial CSF rhinorrhea generally requires definitive skull-base closure because meningitis risk persists while the communication remains open. Measures aimed at intracranial pressure, including weight management, acetazolamide or CSF diversion in selected IIH patients, are adjuncts to a comprehensive plan and should not be used as a reflex substitute for repair of an established persistent defect. Coordinate urgent treatment when meningitis, intracranial infection, tension pneumocephalus or acute neurologic deterioration is present.", "management handoff")
    _append(diag, "teach", "Teaching bridge: diagnosis is CONFIRM FLUID -> LOCALIZE DEFECT -> IDENTIFY ETIOLOGY/PRESSURE DRIVER -> HAND OFF TO REPAIR. A technically successful closure without recognizing spontaneous-leak/IIH biology can leave recurrence risk untreated; conversely, empiric ICP treatment without establishing and repairing a persistent cranial communication is incomplete management.", "confirm fluid")
    _add_sources(diag, "source_metadata_v367", "diagnosis/localization/etiology/IIH recurrence pathway")

    op = by_topic[OP_TOPIC]
    _append(op, "recognize", "OPERATIVE SELECTION — endoscopic CSF leak repair is not a single flap operation. Define defect site, size, flow, encephalocele, surrounding bone/dura quality, prior surgery/radiation, number of defects and suspected elevated ICP before choosing reconstruction. Searchable operative aliases include endoscopic skull-base leak repair, nasoseptal flap, Hadad-Bassagasteguy flap and vascularized septal flap.", "operative selection")
    _append(op, "operate", "SENIOR RECONSTRUCTION DECISION — expose the true margins of the defect without enlarging risk unnecessarily, reduce/resect nonviable encephalocele tissue when appropriate, and choose a reconstruction matched to defect and flow. Small low-flow defects may be closed with appropriately supported free graft/multilayer techniques; larger, high-flow, revision, irradiated or expanded skull-base defects more often justify vascularized tissue such as a pedicled nasoseptal flap. Preserve the posterior septal artery pedicle and consider a rescue-flap strategy when an expanded approach may ultimately require vascularized reconstruction. A lumbar drain is selective—not a mandatory component of every repair—and should be driven by leak/defect/pressure circumstances rather than ritual.", "senior reconstruction decision")
    _append(op, "manage", "POSTREPAIR / RECURRENCE — verify cessation of leak, counsel against early activities that markedly raise sinonasal pressure according to the operative plan, and investigate recurrent leakage rather than simply repacking the nose. In spontaneous leaks, coordinate IIH/ICP assessment and treatment because recurrence can represent persistent pressure biology or a new skull-base defect. Long-term success is closure plus control of the driver, not closure alone.", "postrepair / recurrence")
    _append(op, "teach", "OR bailout model: when the apparent defect does not match preoperative localization, the skull-base boundary is uncertain, or dissection approaches optic nerve/internal carotid/orbital danger anatomy without a safe landmark, stop and re-localize with imaging/navigation/anatomic landmarks rather than forcing exposure. A suspected vascular lesion is never a routine biopsy or leak-repair target. The operative endpoint is a watertight, appropriately supported reconstruction with preserved rescue options and a plan for the underlying etiology.", "or bailout model")
    _add_sources(op, "source_metadata_v367", "repair selection/multilayer closure/nasoseptal flap/rescue and recurrence pathway")

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": [DIAG_TOPIC, OP_TOPIC], "count": 2}
