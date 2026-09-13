"""v36.4 — make Unilateral Sinonasal Disease connected-textbook provenance explicit.

The v35.6 clinical teaching is already appropriately deep and is preserved verbatim. This
bounded source-completeness successor adds explicit connected-Google-Drive identifiers for
Cummings 7e, Pasha 6e, and K.J. Lee 12e to the exact live canonical row so the learner-facing
source trail is traceable rather than title-only. No canonical topic is added, removed, or
renamed.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
TARGET = "Unilateral Sinonasal Disease"

CONNECTED_TEXTBOOKS = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — connected Google Drive full-volume copy ID 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t.",
    "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e (2022) — connected Google Drive file ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "K.J. Lee's Essential Otolaryngology, 12e — connected Google Drive file ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
]


def apply_rhinology_unilateral_source_trace_v364(data_module, app_module=None):
    rows = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    by_topic = {str(row.get("topic") or ""): row for row in rows}
    if len(rows) != 42 or len(by_topic) != 42:
        raise RuntimeError(
            f"v36.4 requires exact 42-topic Rhinology inventory; got rows={len(rows)} unique={len(by_topic)}"
        )
    if TARGET not in by_topic:
        raise RuntimeError(f"v36.4 missing exact canonical target: {TARGET!r}")

    row = by_topic[TARGET]
    sources = list(row.get("source_basis") or [])
    for source in CONNECTED_TEXTBOOKS:
        if source not in sources:
            sources.append(source)
    row["source_basis"] = sources
    row["source_grounded_v364"] = True
    row["source_metadata_v364"] = {
        "canonical_link": {"domain": DOMAIN, "topic": TARGET},
        "textbook_drive_ids": {
            "cummings_7e": "18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t",
            "pasha_6e": "14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52",
            "kj_lee_12e": "112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR",
        },
        "scope": "provenance-only successor; v35.6 unilateral clinical teaching remains authoritative",
    }

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": [TARGET], "count": 1}
