"""v36.3 — make AR/LAR connected-textbook provenance explicit at the live learner boundary.

The clinical teaching for Allergic Rhinitis and Local Allergic Rhinitis is already strong and is
preserved verbatim. This bounded source-completeness pass adds explicit connected-Google-Drive
identifiers for Cummings 7e, Pasha 6e and K.J. Lee 12e to the two exact canonical rows so the
learner-facing source trail is traceable rather than title-only. No canonical topic is added,
removed or renamed.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
TARGETS = ("Allergic Rhinitis", "Local Allergic Rhinitis")

CONNECTED_TEXTBOOKS = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — connected Google Drive split Part 1, pages 1–659, file ID 1Dl2D7ARIi_uLdG0q7QdE0CEuWrX6LVND (inspectable Allergy/Rhinology source section).",
    "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e (2022) — connected Google Drive file ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "K.J. Lee's Essential Otolaryngology, 12e — connected Google Drive file ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
]


def apply_rhinology_allergy_source_trace_v363(data_module, app_module=None):
    rows = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    by_topic = {str(row.get("topic") or ""): row for row in rows}
    if len(rows) != 42 or len(by_topic) != 42:
        raise RuntimeError(
            f"v36.3 requires exact 42-topic Rhinology inventory; got rows={len(rows)} unique={len(by_topic)}"
        )
    missing = [topic for topic in TARGETS if topic not in by_topic]
    if missing:
        raise RuntimeError(f"v36.3 missing exact canonical target(s): {missing}")

    patched = []
    for topic in TARGETS:
        row = by_topic[topic]
        sources = list(row.get("source_basis") or [])
        for source in CONNECTED_TEXTBOOKS:
            if source not in sources:
                sources.append(source)
        row["source_basis"] = sources
        row["source_grounded_v363"] = True
        row["source_metadata_v363"] = {
            "canonical_link": {"domain": DOMAIN, "topic": topic},
            "textbook_drive_ids": {
                "cummings_7e": "1Dl2D7ARIi_uLdG0q7QdE0CEuWrX6LVND",
                "pasha_6e": "14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52",
                "kj_lee_12e": "112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR",
            },
            "scope": "provenance-only successor; existing AR/LAR clinical teaching remains authoritative",
        }
        patched.append(topic)

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
