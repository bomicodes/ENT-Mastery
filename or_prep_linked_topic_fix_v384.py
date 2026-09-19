"""v38.4: Replace legacy OR-prep linked_topic values with canonical deep-curriculum topics.

Only replace known legacy values; preserve previously edited entries. Entries with no
verified curriculum equivalent are deliberately excluded from the mapping.
"""

FIXES = {
    "parathyroidectomy": ("Parathyroid", "Primary Hyperparathyroidism"),
    "endoscopic-sinus-surgery": ("sinonasal-endoscopy", "Ethmoidectomy"),
    "tympanostomy-tubes": ("tympanostomy_tubes", "Tympanostomy Tube Indications"),
    "tonsillectomy-adenoidectomy": ("pediatric_tonsillectomy", "Pediatric OSA / Adenotonsillar Disease"),
    "tympanoplasty": ("tympanoplasty", "Tympanic Membrane Perforation"),
    "direct-laryngoscopy-bronchoscopy": ("airway_stenosis", "Pediatric Subglottic Stenosis"),
    "thyroid-lobectomy": ("thyroidectomy", "Differentiated Thyroid Cancer"),
    "total-thyroidectomy": ("thyroidectomy", "Differentiated Thyroid Cancer"),
    "parotidectomy": ("parotidectomy", "Pleomorphic Adenoma / Warthin Tumor"),
    "mastoidectomy": ("mastoidectomy", "Chronic Otitis Media / Cholesteatoma"),
    "septoplasty": ("septoplasty", "Septal Deviation"),
    "tracheostomy": ("tracheostomy", "Tracheostomy Emergency"),
    "stapedotomy": ("stapedotomy", "Otosclerosis / Stapes Fixation"),
    "cochlear-implant": ("cochlear-implant", "Cochlear Implant Surgery"),
    "DLB": ("DLB", "Pediatric Subglottic Stenosis"),
    "airway-dilation": ("airway-dilation", "Subglottic / Tracheal Stenosis"),
    "zenker": ("zenker", "Zenker Diverticulum"),
    "tonsillectomy": ("tonsillectomy", "Recurrent Tonsillitis Decision-Making"),
    "adenoidectomy": ("adenoidectomy", "Pediatric OSA / Adenotonsillar Disease"),
    "thyroglossal": ("thyroglossal", "Thyroglossal Duct Cyst"),
    "branchial": ("branchial", "Branchial Cleft Anomalies"),
    "orbital-floor": ("orbital-floor", "ZMC / Orbital Trauma"),
    "mandible-orif": ("mandible-orif", "Mandible Fracture"),
    "zmc-orif": ("zmc-orif", "ZMC / Orbital Trauma"),
    "hypoglossal-stimulator": ("hypoglossal-stimulator", "Hypoglossal Nerve Stimulation"),
    "ossiculoplasty": ("ossiculoplasty", "Ossicular Discontinuity"),
    "tegmen-repair": ("tegmen-repair", "CSF Otorrhea / Temporal Encephalocele"),
    "draf": ("draf", "Frontal Sinusotomy / Draf Procedures"),
    "spa-ligation": ("spa-ligation", "Epistaxis Surgical Control"),
    "orbital-abscess": ("orbital-abscess", "Orbital Complications of Sinusitis"),
    "tors": ("tors", "Tonsil SCC"),
    "oral-composite": ("oral-composite", "Floor of Mouth SCC"),
    "tep": ("tep", "TEP and Alaryngeal Speech"),
    "reop-thyroid": ("reop-thyroid", "Reoperative Thyroid Surgery"),
    "reop-parathyroid": ("Parathyroid", "Reoperative Hyperparathyroidism"),
    "parotid-total": ("parotid-total", "Salivary Gland Malignancy"),
    "peds-ltr": ("peds-ltr", "Laryngotracheal Reconstruction"),
    "ctr": ("ctr", "Subglottic / Tracheal Stenosis"),
    "tracheal-resection": ("tracheal-resection", "Subglottic / Tracheal Stenosis"),
    "arytenoid-adduction": ("arytenoid-adduction", "Arytenoid Adduction / Reinnervation"),
    "cp-myotomy": ("cp-myotomy", "Cricopharyngeal Dysfunction"),
    "laryngeal-botox": ("laryngeal-botox", "Spasmodic Dysphonia"),
    "septorhino": ("septorhino", "Functional Nasal Obstruction"),
    "forehead-flap": ("forehead-flap", "Forehead Flap / Nasal Reconstruction"),
    "microflap": ("microflap", "Microlaryngoscopy"),
    "rrp-debridement": ("rrp-debridement", "Recurrent Respiratory Papillomatosis"),
    "reconstructive-palate": ("reconstructive-palate", "Palatal Surgery"),
    "lingual-tonsillectomy": ("lingual-tonsillectomy", "Lingual Tonsil / Tongue-Base Obstruction"),
    "hyoid-genioglossus": ("hyoid-genioglossus", "Tongue Base Surgery"),
    "closed-nasal-reduction": ("closed-nasal-reduction", "Nasal Fracture"),
    "noe-orif": ("noe-orif", "NOE Fracture"),
    "frontal-sinus-trauma": ("frontal-sinus-trauma", "Frontal Sinus Fracture"),
    "melolabial-flap": ("melolabial-flap", "Local Flap Reconstruction"),
    "skin-graft-face": ("skin-graft-face", "Mohs Defect Reconstruction"),
    "free-flap-basics": ("free-flap-basics", "Reconstruction Selection After Head & Neck Ablation"),
    "pharyngocutaneous-fistula": ("pharyngocutaneous-fistula", "Total Laryngectomy"),
    "pta-drainage": ("pta-drainage", "Peritonsillar Abscess"),
    "airway-fb": ("airway-fb", "Pediatric Airway Foreign Body"),
    "esophageal-fb": ("esophageal-fb", "Esophageal Foreign Body"),
    "button-battery": ("button-battery", "Button Battery Ingestion"),
    "submandibular-gland": ("submandibular-gland", "Submandibular Gland Excision"),
    "medialization": ("medialization", "Medialization Thyroplasty"),
    "maxillary-antrostomy": ("maxillary-antrostomy", "Endoscopic Maxillary Antrostomy"),
    "csf-nasoseptal": ("csf-nasoseptal", "Endoscopic CSF Leak Repair / Nasoseptal Flap"),
    "central-neck": ("central-neck", "Central Neck Dissection"),
    "four-gland": ("Parathyroid", "Four-Gland Parathyroid Exploration"),
    "cordotomy": ("cordotomy", "Posterior Cordotomy / Arytenoidectomy"),
    "deep-neck-drain": ("deep-neck-drain", "Deep Neck Abscess Drainage"),
}

KNOWN_UNRESOLVED = ["canalplasty", "laryngeal-fracture"]


def apply_or_prep_linked_topic_fix_v384(registry):
    if not registry:
        raise RuntimeError("v38.4: OR_PREP_REGISTRY not found")
    patched = []
    skipped_already_edited = []
    missing_slugs = []
    for slug, (old_value, new_topic) in FIXES.items():
        entry = registry.get(slug)
        if entry is None:
            missing_slugs.append(slug)
            continue
        current = (entry.get("linked_topic") or "").strip()
        if current == old_value:
            entry["linked_topic"] = new_topic
            patched.append(slug)
        elif current == new_topic:
            pass
        else:
            skipped_already_edited.append(slug)
    if missing_slugs:
        raise RuntimeError(f"v38.4: expected OR-prep slug(s) not found: {missing_slugs}")
    return {"patched": patched, "count": len(patched), "skipped_already_edited": skipped_already_edited, "known_unresolved": KNOWN_UNRESOLVED}
