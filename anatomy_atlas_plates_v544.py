"""v54.4: replace the 26 in-house orientation schematics in the Anatomy Atlas with real plates.

Every image below was found on Wikimedia Commons, its license read from the
file's Commons metadata, and the image itself viewed in Chrome against the
atlas card's landmarks (2026-11-01). 23 are public-domain plates from Gray's
Anatomy (1918, H. V. Carter); 3 are modern diagrams (CC0, CC BY 3.0, CC BY 4.0)
credited to their authors.

The in-house SVG stays as `legacy_schematic`, which the template uses only as
an onerror fallback if the plate fails to load.
"""

_C = "https://commons.wikimedia.org/wiki/"


def _gray(fig, what):
    f = f"Gray{fig}.png"
    return {
        "file": f,
        "credit": f"Gray's Anatomy (1918), Fig. {fig}: {what} · H. V. Carter · public domain",
    }


PLATES_V544 = {
    "Pterygopalatine / Infratemporal Spaces": _gray(778, "distribution of the maxillary and mandibular nerves"),
    "Pterygopalatine Fossa / Autonomic Pathways": _gray(780, "the sphenopalatine (pterygopalatine) ganglion and its branches"),
    "Infratemporal Fossa / Internal Maxillary Artery": _gray(510, "the internal maxillary artery and its branches"),
    "Neck Levels / Fascial Compartments": {
        "file": "Cervical lymph nodes and levels.png",
        "credit": "Cervical lymph nodes and neck levels I–VI · Mikael Häggström, M.D. · CC0",
    },
    "Parathyroid Embryology / Ectopic Map": _gray(1177, "parathyroid glands, posterior view with the inferior thyroid artery and recurrent laryngeal nerve (Halsted and Evans)"),
    "Facial Buttresses / Midface Trauma": {
        "file": "Clasificación de le fort.png",
        "credit": "Le Fort I, II and III fracture levels, frontal and lateral views · Chelepepino · CC BY 3.0",
    },
    "Superficial Face — Vessels / Facial Nerve / SMAS": _gray(790, "the nerves of the scalp, face and side of the neck"),
    "Scalp / Forehead Surgical Layers": _gray(1196, "layers of the scalp, skull and meninges"),
    "Orbit — Compartments / Canthi / Lacrimal System": _gray(896, "the lacrimal apparatus"),
    "Mandible / TMJ / Masticator Space": {
        "file": "Gray — musculus pterygoideus lateralis.png",
        "credit": "Gray's Anatomy: pterygoid muscles, mandible and TMJ (lateral pterygoid highlighted by User:Helgo13) · H. V. Carter · public domain",
    },
    "Jugular Foramen / Hypoglossal Canal / Lower Cranial Nerves": _gray(791, "plan of the glossopharyngeal, vagus and accessory nerves at and below the jugular foramen"),
    "Lateral Neck Triangles / CN XI / Brachial Plexus": _gray(512, "the triangles of the neck"),
    "Thoracic Inlet / Root of Neck": _gray(505, "the arch of the aorta and great vessels with the vagus, recurrent laryngeal and phrenic nerves and thoracic duct"),
    "Mediastinal Continuity of Deep Neck Spaces": {
        "file": "Infrahyoid deep neck spaces.webp",
        "credit": "Infrahyoid deep neck spaces and fascial layers, including the retropharyngeal and danger spaces · Nadezdha D. Kiriyak · CC BY 4.0",
    },
    "Vagus / Sympathetic Chain / Carotid Space": _gray(1031, "the pharynx from behind, with the carotid arteries, internal jugular veins, vagus nerves and sympathetic trunks"),
    "Free-Flap Recipient Vessels / Reconstructive Neck": _gray(520, "arteries and veins of the side of the neck"),
    "Middle Cranial Fossa Approach Corridor": _gray(193, "the cranial fossae, superior view"),
    "Translabyrinthine Approach Corridor": _gray(920, "the right osseous labyrinth, lateral view"),
    "Jugular Foramen / Infratemporal Approach Corridor": _gray(187, "base of the skull, external surface"),
    "Pharyngeal Constrictors / Superior Laryngeal Neurovascular Relationships": _gray(1030, "muscles of the pharynx and cheek (constrictors), lateral view"),
    "Cleft Palate Levator Sling / Tensor / Eustachian Tube": _gray(1028, "dissection of the muscles of the palate from behind"),
    "Auricular Framework / Microtia Reconstruction Anatomy": _gray(904, "the auricle, lateral surface"),
    "Palatal / Lateral Pharyngeal Wall Anatomy for Sleep Surgery": _gray(1014, "the mouth cavity, with the palatoglossal and palatopharyngeal arches and palatine tonsil"),
    "Tongue Base / Hyoid / Suprahyoid Relationships": _gray(1019, "extrinsic muscles of the tongue and the hyoid"),
    "Hypoglossal Nerve / HNS Surgical Anatomy": _gray(794, "the hypoglossal nerve, cervical plexus and their branches"),
    "Maxillomandibular Skeletal Relationships / MMA": _gray(188, "side view of the skull"),
}


def install_anatomy_atlas_plates_v544(data_module, app_module=None):
    atlas = data_module.ANATOMY_ATLAS_V97
    by_topic = {x.get("topic"): x for x in atlas}
    missing = [t for t in PLATES_V544 if t not in by_topic]
    if missing:
        raise RuntimeError(f"anatomy_atlas_plates_v544: unknown atlas topics {missing}")
    for topic, p in PLATES_V544.items():
        x = by_topic[topic]
        x["image_url"] = _C + "Special:Redirect/file/" + p["file"].replace(" ", "_")
        x["image_source"] = _C + "File:" + p["file"].replace(" ", "_")
        x["image_credit"] = p["credit"]
        x["anatomy_visual_status"] = "verified_classical_plate"
        x["plate_v544"] = True
    if app_module is not None and getattr(app_module, "ANATOMY_ATLAS_V97", None) is not atlas:
        app_module.ANATOMY_ATLAS_V97 = atlas
    remaining = [x["topic"] for x in atlas if not (
        x.get("anatomy_visual_status") in ("verified_classical_plate", "verified_open_access_photo") and x.get("image_url"))]
    data_module.ANATOMY_PLATES_V544 = {"replaced": len(PLATES_V544), "still_schematic": remaining}
    return data_module.ANATOMY_PLATES_V544
