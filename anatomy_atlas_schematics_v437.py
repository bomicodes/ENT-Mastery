"""v43.7: finish Anatomy Atlas image coverage (site audit, 2026-09-22/23).

The atlas template already had a `legacy_schematic` field on
ANATOMY_ATLAS_V97 (a locally hosted, purpose-built orientation SVG) that was
already set on 50 entries -- but the template itself had no rendering
branch for it, so all 50 silently fell through to the bare "no verified
anatomic image yet" text state despite the artwork already existing on
disk. Adding the `{% elif x.legacy_schematic %}` branch to
templates/anatomy_atlas.html (alongside this module) fixes those 50 "for
free," with no data.py change needed.

That left exactly 4 entries with no `legacy_schematic` at all -- every one
of them in Sleep Surgery: Palatal/Lateral Pharyngeal Wall, Tongue
Base/Hyoid/Suprahyoid, Hypoglossal Nerve/HNS, and Maxillomandibular
Skeletal Relationships/MMA. Four new schematics -- 51 through 54 -- were
authored from the existing 50 as a style reference (same CSS classes,
800x360 layout, 4 landmarks + 2 danger structures, orientation-disclaimer
sub-label), and this module wires their paths into the corresponding
ANATOMY_ATLAS_V97 entries.

Result: 54/54 Anatomy Atlas entries now have a `legacy_schematic` and will
render an in-house orientation schematic instead of the "no image yet"
placeholder.
"""

LEGACY_SCHEMATIC_MAP = {
    "Palatal / Lateral Pharyngeal Wall Anatomy for Sleep Surgery": "anatomy/51-palatal-lateral-pharyngeal-wall-sleep.svg",
    "Tongue Base / Hyoid / Suprahyoid Relationships": "anatomy/52-tongue-base-hyoid-suprahyoid.svg",
    "Hypoglossal Nerve / HNS Surgical Anatomy": "anatomy/53-hypoglossal-nerve-hns-anatomy.svg",
    "Maxillomandibular Skeletal Relationships / MMA": "anatomy/54-maxillomandibular-skeletal-relationships-mma.svg",
}


def apply_anatomy_atlas_schematics_v437(data_module, app_module=None):
    atlas = data_module.ANATOMY_ATLAS_V97
    set_count = 0
    missing_files = []
    import os
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    for entry in atlas:
        topic = entry.get("topic")
        if topic in LEGACY_SCHEMATIC_MAP and not entry.get("legacy_schematic"):
            rel = LEGACY_SCHEMATIC_MAP[topic]
            if not os.path.exists(os.path.join(static_dir, rel)):
                missing_files.append(rel)
                continue
            entry["legacy_schematic"] = rel
            set_count += 1
    if app_module is not None:
        app_module.ANATOMY_ATLAS_V97 = atlas
    if missing_files:
        raise RuntimeError(f"anatomy_atlas_schematics_v437: missing SVG file(s): {missing_files}")
    return {"legacy_schematic_set": set_count}
