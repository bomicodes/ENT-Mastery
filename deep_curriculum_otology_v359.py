"""v35.9 — source-grounded Chronic Otitis Media / Cholesteatoma depth and provenance.

Targets exactly one live canonical Otology concept by exact title. This patch preserves the
existing ladder and adds resident/board/OR decision depth plus visible textbook/current-evidence
source metadata. Ambiguity or canonical drift fails closed.
"""

DOMAIN = "Otology / Neurotology"
TOPIC = "Chronic Otitis Media / Cholesteatoma"

SOURCE_BASIS_V359 = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — chronic otitis media/cholesteatoma pathogenesis, temporal-bone anatomy, tympanomastoid surgical principles, complications, ossicular reconstruction and surveillance. Connected Google Drive source: CUMMINGS OTOLARYNGOLOGY–HEAD AND NECK 7th Ed 2021_compressed.pdf, file id 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t; split-volume copies also present.",
    "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e (2022), Otology/Neurotology chapter — infections/noninfectious temporal-bone disease and operative otology framework. Connected Google Drive file id 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "K.J. Lee's Essential Otolaryngology, 12e — chronic middle-ear disease, cholesteatoma, mastoid surgery, complications and hearing reconstruction. Connected Google Drive file id 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
    "EAONO/JOS Joint Consensus Statements on the Definitions, Classification and Staging of Middle Ear Cholesteatoma. J Int Adv Otol. 2017;13(1):1-8. doi:10.5152/iao.2017.3363 — durable consensus terminology, classification and staging framework.",
    "Patel TA et al. Cost-Effectiveness of Diffusion Weighted MRI Versus Planned Second-Look Surgery for Cholesteatoma. Ann Otol Rhinol Laryngol. 2024. doi:10.1177/00034894241250253 — non-EPI DWI surveillance and planned second-look surgery are both viable follow-up strategies; selection is individualized.",
    "Current evidence distinction (rechecked 2026-09-11): non-EPI diffusion-weighted MRI is a surveillance tool for residual/recurrent cholesteatoma and does not replace operative judgment when disease, complications, anatomy, hearing goals, or inability to ensure follow-up favor surgery."
]

DEPTH_APPEND_V359 = {
    "recognize": " FOUNDATION REFINEMENT — cholesteatoma is keratinizing squamous epithelium in the middle ear/mastoid with destructive behavior; a pars flaccida or pars tensa retraction pocket containing keratin, persistent focal otorrhea, scutum/ossicular erosion, or a white mass behind an intact drum should trigger the diagnosis. Distinguish unsafe keratinizing disease from a chronically draining but non-cholesteatomatous perforation because the operative goals differ.",
    "localize": " APPLICATION REFINEMENT — localize the matrix and its route of spread before choosing exposure: epitympanum/Prussak space, posterior mesotympanum/sinus tympani, facial recess, mastoid, hypotympanum, protympanum and tegmen/labyrinth/facial-nerve relationships determine residual-disease risk. Conductive loss does not measure extent; a small attic pocket can hide substantial posterior or mastoid disease.",
    "workup": " SENIOR DIAGNOSTIC REFINEMENT — microscopy/endoscopy plus audiometry define the clinical problem; high-resolution temporal-bone CT is most useful for anatomy, bony erosion, complications and operative planning but cannot reliably distinguish every soft-tissue substrate. MRI with non-EPI DWI is especially useful for suspected residual/recurrent disease and selected diagnostic uncertainty. New vertigo, facial weakness, severe headache/neurologic findings or systemic toxicity should trigger evaluation for labyrinthine, facial-nerve, intracranial or other complicated disease rather than routine elective workup.",
    "manage": " SENIOR MANAGEMENT REFINEMENT — definitive management is driven by eradication of unsafe disease and creation of a safe, dry, surveillable ear; hearing restoration is important but subordinate when those goals conflict. Canal-wall-up versus canal-wall-down is not a board-style ideology: choose the approach from disease extent, anatomy, ventilation, contralateral hearing, reliability of follow-up, prior surgery and the ability to inspect likely residual sites. A poorly followable ear is a different risk problem from an ear with dependable serial endoscopy/non-EPI DWI.",
    "operate": " OR DECISION REFINEMENT — follow matrix deliberately and preserve landmarks; anticipate ossicular erosion, facial-nerve dehiscence, lateral semicircular-canal fistula, low tegmen/dural exposure and sigmoid/jugular variants. Do not avulse matrix blindly from a suspected labyrinthine fistula or dehiscent facial nerve. If safe complete removal cannot be achieved through the planned exposure, enlarge exposure or convert the strategy rather than leaving occult disease for the sake of the original approach. Reconstruction is staged or limited when infection, mucosal disease, uncertain clearance, poor middle-ear environment or surveillance needs make immediate hearing reconstruction unsafe. Residual/recurrent surveillance must be planned at the index operation; non-EPI DWI can replace some routine second-look operations, but second-look surgery remains appropriate when anatomy, reconstruction, disease risk or follow-up uncertainty warrants it.",
    "teach": " CHIEF FRAMEWORK — 1) diagnose unsafe keratinizing disease; 2) map hidden spaces and complication anatomy; 3) make a disease-eradication/surveillance plan before a hearing-reconstruction plan; 4) choose CWU/CWD from the ear and patient rather than dogma; 5) know facial nerve, labyrinth, tegmen and vascular danger zones; 6) decide explicitly how residual disease will be detected. Durable operative anatomy comes from core texts; terminology/staging and surveillance evidence are tracked separately as current evidence."
}


def apply_cholesteatoma_source_depth_v359(data_module, app_module=None):
    rows = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    matches = [row for row in rows if row.get("topic") == TOPIC]
    if len(matches) != 1:
        raise RuntimeError(f"v35.9 requires exactly one exact live {DOMAIN} / {TOPIC!r}; found {len(matches)}")
    row = matches[0]
    for field, addition in DEPTH_APPEND_V359.items():
        current = str(row.get(field) or "").strip()
        if addition not in current:
            row[field] = (current + " " + addition).strip()
    row["source_basis"] = list(SOURCE_BASIS_V359)
    row["source_grounded_v359"] = True
    row["source_metadata_v359"] = {
        "canonical_link": {"domain": DOMAIN, "topic": TOPIC},
        "identity_rule": "exact live canonical domain/topic equality",
        "textbook_drive_ids": {
            "cummings_7e": "18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t",
            "pasha_6e": "14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52",
            "kj_lee_12e": "112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR",
        },
        "management_currency": "Durable anatomy/operative principles retained from core texts; consensus terminology and surveillance evidence rechecked 2026-09-11.",
    }
    row["deliberate_review_v359"] = {
        "foundation": "recognize unsafe keratinizing middle-ear disease and distinguish it from uncomplicated chronic perforation",
        "application": "map hidden spaces and complication anatomy, then choose imaging/exposure/surveillance for the actual disease pattern",
        "senior_decision": "prioritize a safe dry surveillable ear, choose CWU/CWD without dogma, protect facial nerve/labyrinth/tegmen, and precommit to residual-disease surveillance",
        "traps": [
            "equating degree of conductive loss with cholesteatoma extent",
            "using CT soft-tissue density as proof that all opacity is cholesteatoma",
            "choosing canal-wall-up or canal-wall-down by habit rather than disease/anatomy/follow-up",
            "avulsing matrix from a suspected labyrinthine fistula or dehiscent facial nerve",
            "prioritizing ossicular reconstruction over safe disease clearance",
            "failing to inspect posterior mesotympanum/sinus tympani and other hidden recesses",
            "assuming non-EPI DWI eliminates every indication for second-look surgery",
            "finishing the index operation without an explicit residual/recurrent surveillance plan",
        ],
    }
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": [TOPIC], "count": 1, "canonical_topic": TOPIC}
