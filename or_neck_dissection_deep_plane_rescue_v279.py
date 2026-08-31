"""v27.9 neck-dissection deep-plane sympathetic-chain/brachial-plexus rescue.

Adds chief-level posterior-boundary discipline, Horner recognition, and brachial-plexus
injury bailout while preserving oncologic judgment and avoiding unsupported mandates.
"""

DEEP_PLANE_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed.",
    "K. J. Lee's Essential Otolaryngology: Head and Neck Surgery, 12th ed.",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed.",
    "Moore EJ et al. Retropharyngeal lymph node dissection in oropharyngeal cancer treated with transoral robotic surgery. Laryngoscope. 2013;123:1676-1681.",
    "Punda A et al. Delayed Horner Syndrome and Accessory Nerve Weakness After Papillary Thyroid Carcinoma Surgery. Ear Nose Throat J. 2021;100(5 Suppl):735S-737S.",
    "Monteiro MJ et al. Injury to the brachial plexus in neck dissections. Br J Oral Maxillofac Surg. 2010;48(3):197-198.",
    "Garzaro M et al. A study of neck and shoulder morbidity following neck dissection: the benefits of cervical plexus preservation. Ear Nose Throat J. 2015;94:391-398.",
]

TARGETS = [{
    "slug": "neck-dissection",
    "title_terms": ("neck", "dissection"),
    "setup": [
        "Treat the prevertebral fascia as a posterior safety boundary during routine lateral-neck dissection. The cervical sympathetic trunk lies deep/posteromedial to the carotid sheath on the prevertebral musculature and may vary in relation to the sheath; the brachial plexus emerges between the scalene muscles and is deep to the prevertebral layer. Do not chase nodal tissue blindly through an intact deep fascial plane when the oncologic target does not require it.",
        "When dissecting posterior to or mobilizing the carotid sheath, or working in the retropharyngeal/deep level II-IV region, protect the sympathetic chain from traction, compression, and thermal spread. If a fusiform structure near the retropharyngeal packet could be superior sympathetic ganglion rather than nodal disease, stop and widen exposure to establish continuity/anatomy before dividing it; avoid monopolar energy immediately against a suspected sympathetic trunk.",
        "In low level IV/V, preserve a clearly uninvolved brachial plexus and cervical rootlets when oncologically feasible. If the dissection unexpectedly enters the scalene/interplexus plane or a major motor root/plexus element is injured, stop further traction or energy, define the injury under exposure, protect viable nerve ends/fascicles, and obtain peripheral-nerve/reconstructive expertise rather than extending an unplanned deep-plane injury simply to finish the packet. Deliberate oncologic sacrifice requires a different preplanned functional discussion than accidental injury.",
    ],
    "postop": [
        "New ipsilateral ptosis and miosis, with or without facial anhidrosis, after deep carotid-sheath/retropharyngeal dissection should be recognized as possible Horner syndrome and documented with a focused ocular/neurologic examination. Do not assume every postoperative Horner syndrome proves transection: traction, compression, hematoma, or neuropraxia can occur, so evaluate the operative context and exclude a compressive or other acute neurologic process when the presentation is atypical or evolving.",
        "New arm pain, weakness, sensory loss, or reflex change after level IV/V dissection should trigger a focused brachial-plexus examination rather than being labeled generic shoulder dysfunction. Distinguish plexopathy from isolated CN XI/trapezius weakness, positioning injury, cervical radiculopathy, and central neurologic causes; obtain early neurology/peripheral-nerve input and electrodiagnostic/imaging follow-up when a significant deficit persists or a structural injury is suspected.",
    ],
    "sources": DEEP_PLANE_SOURCES,
    "marker": "neck_dissection_deep_plane_rescue_v279",
}]


def _resolve(registry, target):
    reg = registry or {}
    if target["slug"] in reg:
        return target["slug"], reg[target["slug"]]
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in target["title_terms"]):
            return slug, op
    return None, None


def _prepend_unique(values, additions):
    out = list(values or []); changed = False
    for text in reversed(additions or []):
        marker = text[:72].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text); changed = True
    return out, changed


def _append_unique(values, additions):
    out = list(values or []); known = {str(x).strip().lower() for x in out}; changed = False
    for text in additions or []:
        key = str(text).strip().lower()
        if key and key not in known:
            out.append(text); known.add(key); changed = True
    return out, changed


def apply_or_neck_dissection_deep_plane_rescue_v279(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"]); continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target["setup"])
        op["postop"], c2 = _prepend_unique(op.get("postop"), target["postop"])
        op["sources"], c3 = _append_unique(op.get("sources"), target["sources"])
        op[target["marker"]] = True
        resolved.append(slug)
        if c1 or c2 or c3: changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
