"""v76.0: real indications for the 20 OR cards that still carried a generic placeholder.

These cards came from the v9.1 gap-closure batch, whose indications line read "Use when the
disease-specific indication is established and the anatomy, alternatives, functional goals,
and rescue plan have been reviewed." Each now states when the operation is done.
"""

PLACEHOLDER = "Use when the disease-specific indication is established"

INDICATIONS_V760 = {
    "airway-fb": (
        'Suspected airway foreign body: a choking or witnessed aspiration event with cough, wheeze, unilateral '
        'decreased breath sounds, or radiographic air trapping, atelectasis or a radiopaque object. Rigid bronchoscopy '
        'is both diagnostic and therapeutic and is done promptly even with normal films when the history is convincing; '
        'complete obstruction is an emergency. A low-suspicion case may be clarified first with CT or flexible '
        'bronchoscopy.'
    ),
    "bilobed-flap": (
        'Small skin defects up to about 1.5 cm of the lower third of the nose (tip, ala, lower sidewall), at least '
        'about 5 mm from the alar rim, usually after Mohs surgery, where primary closure would distort the tip or ala '
        'and nearby upper-nasal skin can be borrowed. Larger, deeper or rim-involving defects usually need a forehead '
        'or melolabial flap or a composite repair.'
    ),
    "cervicofacial-flap": (
        'Large cheek defects, typically over about 3-4 cm of the medial or lateral cheek or preauricular skin after '
        'tumor or Mohs excision, that are too big for a local flap or primary closure and where matching cheek and neck '
        'skin can be rotated and advanced. Also used to cover a parotidectomy or temporal bone resection skin defect.'
    ),
    "closed-nasal-reduction": (
        'A displaced nasal bone fracture with cosmetic deformity or nasal obstruction, without a major septal fracture- '
        'dislocation (a septal hematoma must be ruled out and drained urgently first), done either within the first few '
        'hours or after swelling settles at about 3 to 10 days (sooner in children). Severe septal deviation, an open '
        'injury or a deformity present for weeks favors open reduction or delayed septorhinoplasty.'
    ),
    "esophageal-fb": (
        'An impacted esophageal foreign body or food bolus. Emergent removal for a button battery, sharp or pointed '
        'object, magnets, complete obstruction with inability to handle secretions, or signs of perforation; urgent '
        'removal (within about 24 hours) for other retained objects. An asymptomatic mid or distal esophageal coin may '
        'be watched for 12-24 hours with a repeat film; remove sooner for a proximal coin, symptoms or an unknown '
        'ingestion time. Always check the film for a button battery (double ring or step-off), and biopsy for '
        'eosinophilic esophagitis at food bolus removal.'
    ),
    "facial-nerve-reanimation": (
        'Facial nerve transection or a resected segment (trauma, tumor or surgery): primary end-to-end repair when ends '
        'meet without tension, ideally within about 72 hours, while distal branches still respond to stimulation; cable '
        'grafting (great auricular or sural nerve) for a gap; and nerve transfer (for example masseteric or '
        'hypoglossal) when the proximal stump is unavailable but the facial muscles are still viable, ideally within '
        'about 12 months (fibrosis starts at about 12-18 months). Beyond about 2 years or with atrophied muscle, free '
        'muscle transfer (gracilis) or static procedures are used.'
    ),
    "free-flap-basics": (
        'Head and neck defects that local or regional flaps cannot reconstruct well: segmental mandible or maxilla '
        'defects (fibula, scapula, iliac crest), large through-and-through or pharyngeal defects, near-total '
        'glossectomy, salvage surgery in irradiated fields, and defects needing well-vascularized tissue to protect the '
        'carotid or close a fistula. Requires suitable recipient vessels and a patient fit for a longer operation.'
    ),
    "hyoid-genioglossus": (
        'Moderate to severe obstructive sleep apnea with retrolingual or hypopharyngeal collapse in a patient who '
        'cannot tolerate CPAP, usually as part of multilevel surgery after sleep endoscopy. Genioglossus advancement '
        'pulls the tongue base forward; hyoid suspension stabilizes the hypopharynx. Severe obesity (BMI over about '
        '32-35) or a better candidacy for hypoglossal nerve stimulation or maxillomandibular advancement argue against '
        'it.'
    ),
    "laryngeal-fracture": (
        'External laryngeal trauma with a displaced or unstable thyroid or cricoid fracture, exposed cartilage, large '
        'or deep mucosal lacerations, disruption of the anterior commissure, vocal fold immobility from arytenoid '
        'dislocation, or airway compromise (Schaefer groups III-V), ideally repaired within 24 hours after securing the '
        'airway (awake tracheotomy under local is preferred when the airway is compromised). Group I (minor hematoma, '
        'no fracture) is observed with medical care; group II (edema, minor tears, nondisplaced fracture) needs direct '
        'laryngoscopy and esophagoscopy and often a tracheotomy, but usually no open repair.'
    ),
    "lingual-tonsillectomy": (
        'Obstructive sleep apnea with retrolingual obstruction from lingual tonsil hypertrophy or tongue-base bulk on '
        'sleep endoscopy or imaging, especially persistent OSA after adenotonsillectomy in children (including Down '
        'syndrome) or adult multilevel surgery; also recurrent lingual tonsillitis or a lingual tonsil mass needing '
        'tissue.'
    ),
    "melolabial-flap": (
        'Defects of the nasal ala, sidewall or upper lip (and the columella with an interpolated design) where cheek '
        'skin of similar color and texture can be borrowed: a one-stage transposition for sidewall defects or a two- '
        'stage interpolated flap for full alar subunit defects, often combined with cartilage grafts for alar support.'
    ),
    "microflap": (
        'Benign vocal fold lesions that cause dysphonia and persist despite voice therapy and reflux and phonotrauma '
        'management, such as polyps, cysts, Reinke edema and selected nodules, and lesions needing tissue diagnosis '
        '(leukoplakia or a suspicious lesion). Nodules rarely need surgery after adequate voice therapy, and smokers '
        'with Reinke edema should stop smoking first. The microflap removes the lesion while preserving the superficial '
        'lamina propria and the mucosal wave.'
    ),
    "noe-orif": (
        'Displaced naso-orbito-ethmoid fractures with telecanthus, loss of nasal dorsal height or support, or an '
        'unstable or comminuted central fragment (Markowitz-Manson types I-III; in type III the medial canthal tendon '
        'is avulsed and needs transnasal canthopexy). Nondisplaced, stable fractures without telecanthus are observed. '
        'Repair restores intercanthal width and nasal projection, ideally before swelling and scar make reduction '
        'harder.'
    ),
    "pharyngocutaneous-fistula": (
        'A salivary leak or pharyngocutaneous fistula after laryngectomy or pharyngeal surgery. Most are managed '
        'conservatively first (nothing by mouth, wound care, antibiotics for infection, nutrition, correcting '
        'hypothyroidism). Operative repair, usually with vascularized tissue such as a pectoralis major or free flap, '
        'is for fistulas that fail to close, are large, expose or threaten the carotid, or occur in a heavily '
        'irradiated field.'
    ),
    "pta-drainage": (
        'A peritonsillar abscess confirmed on exam (trismus, uvular deviation, bulging soft palate) or by imaging or '
        'needle aspiration: needle aspiration or incision and drainage plus antibiotics. Quinsy (immediate) '
        'tonsillectomy is for recurrent peritonsillar abscess, a history meeting criteria for tonsillectomy, failed '
        'drainage, airway compromise, sepsis or parapharyngeal spread, or a child who needs general anesthesia for '
        'drainage anyway.'
    ),
    "reconstructive-palate": (
        'Obstructive sleep apnea with velopharyngeal (palatal) obstruction on exam or sleep endoscopy in a patient who '
        'cannot tolerate or refuses CPAP, alone or as part of multilevel surgery: for example expansion sphincter '
        'pharyngoplasty or other modern uvulopalatopharyngoplasty variants, ideally with favorable anatomy (large '
        'tonsils, lower BMI, lateral or anteroposterior rather than complete concentric collapse).'
    ),
    "rrp-debridement": (
        'Recurrent respiratory papillomatosis causing dysphonia or airway narrowing: repeated debulking (microdebrider, '
        'cold instruments or laser), timed by symptoms and airway rather than a fixed schedule, aiming to preserve '
        'normal tissue and avoid webbing. Adjuvant therapy is considered for more than 4 procedures a year, rapid '
        'regrowth with airway compromise, or distal multisite spread: bevacizumab, HPV vaccination and, in adults, '
        'zopapogene imadenovec (Papzimeos, FDA-approved 2025).'
    ),
    "frontal-sinus-trauma": (
        'Frontal sinus fractures with displaced anterior table causing contour deformity, frontal sinus outflow tract '
        'injury, posterior table displacement (more than about one table width) or comminution, or a persistent CSF '
        'leak. Options range from endoscopic or open repair of the anterior table and outflow tract, through '
        'observation with serial CT for selected outflow injuries, to cranialization or obliteration for severe '
        'posterior table or outflow injury; current practice favors outflow preservation with endoscopic management and '
        'serial CT over obliteration where safe. A CSF leak lasting more than about 7 days is also an indication. '
        'Nondisplaced or minimally displaced anterior table fractures (under about 2-4 mm) with a patent outflow tract '
        'are observed.'
    ),
    "button-battery": (
        'Any suspected or confirmed esophageal button battery: an emergency needing removal as soon as possible, '
        'ideally within about 2 hours, because injury starts within minutes, even if the child looks well. A battery '
        'past the esophagus in an asymptomatic child is usually allowed to pass, with stool checks and a repeat film at '
        '7-14 days. Endoscopic removal is indicated for symptoms, a co-ingested magnet, a battery still in the stomach '
        'on the repeat film, a battery of 15 mm or more still in the stomach after 4 days in a child under 6, or '
        'diagnosis more than 12 hours after ingestion (then also check the esophagus for injury and consider CT '
        'angiography). While removal is arranged, give honey (age 12 months or older, within 12 hours, 10 mL every 10 '
        'minutes, up to 6 doses) or sucralfate, but never delay removal for it.'
    ),
    "skin-graft-face": (
        'Facial defects that cannot close primarily or with a local flap, or where a flap would distort nearby '
        'structures. Full-thickness grafts (from preauricular, postauricular or supraclavicular skin) suit nasal tip, '
        'ala, eyelid and ear defects for better color and less contraction; split-thickness grafts suit large scalp or '
        'temporal defects, cavities needing surveillance, and poor-donor-site situations. The bed must be vascular '
        '(perichondrium or periosteum intact).'
    ),
}


def install_or_indications_v760(data, app_mod=None):
    registry = data.OR_PREP_REGISTRY
    fixed, still_generic = [], []
    for slug, card in registry.items():
        text = card.get("indications")
        text = " ".join(text) if isinstance(text, list) else str(text or "")
        if PLACEHOLDER in text or not text.strip():
            if slug in INDICATIONS_V760:
                card["indications"] = INDICATIONS_V760[slug]
                fixed.append(slug)
            else:
                still_generic.append(slug)
    return {"fixed": fixed, "still_generic": still_generic}
