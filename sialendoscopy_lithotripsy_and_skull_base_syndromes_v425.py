"""v42.5: sialendoscopy lithotripsy depth + skull-base eponymous syndrome coverage.

Continuation of the sialolithiasis/lithotripsy deep dive and skull-base syndrome
coverage check requested 2026-09-21. The gland-specific sialolithiasis content
(parotid vs. submandibular, why open sialolithotomy is a poor choice for parotid
stones) is already merged into the live "Sialolithiasis" topic by
sialolithiasis_consolidation_v424.py. Two pieces of that original request were
not yet covered on this tree:

1. The "Sialendoscopy" topic itself never got explicit lithotripsy indications
   (intracorporeal laser/pneumatic vs. the largely-supplanted ESWL) -- this adds
   them to its manage/teach fields.
2. A user-attached quiz screenshot (discriminating Orbital apex syndrome / Vernet
   syndrome / Lemierre syndrome / Villaret syndrome / Gradenigo syndrome) prompted
   a coverage check. Lemierre Syndrome already existed (General ENT /
   Emergencies). The other four did not exist anywhere as named topics -- the
   closest existing content, "Cranial Nerve Examination / Skull Base
   Localization", names the anatomic patterns (jugular foramen IX-XI, orbital
   apex/cavernous sinus, parapharyngeal IX-XII + sympathetic chain) but never the
   eponyms or the discriminating features between them. This adds all four as new
   topics, each cross-referencing the "syndrome ladder" (Vernet -> Collet-Sicard
   -> Villaret) and the orbital apex vs. cavernous sinus vs. Gradenigo
   distinction, plus Clinical Challenge vignettes that quiz the discrimination
   directly (including one mirroring the screenshot's 5-option format).

Net topic-count effect: 344 -> 348 (Otology/Neurotology 51 -> 53,
Rhinology/Allergy/Skull Base 45 -> 46, Head & Neck Oncology 42 -> 43;
Thyroid/Parathyroid/Salivary unchanged since Sialendoscopy already exists).
"""

from copy import deepcopy
import re


DOMAIN_SOURCES = {
    "Rhinology / Allergy / Skull Base": (
        "Pasha & Golub, 6e (2022), Ch 1 Allergy and Rhinology, pp 1-74.",
        "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 3, Ch 26-34, pp 479-611.",
    ),
    "Otology / Neurotology": (
        "Pasha & Golub, 6e (2022), Ch 7 Otology and Neurotology, pp 333-436.",
        "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 2, Ch 13-23, pp 234-478.",
    ),
    "Head & Neck Oncology": (
        "Pasha & Golub, 6e (2022), Ch 6 Head and Neck Cancer, pp 249-332.",
        "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 4, Ch 35-49, pp 612-878.",
    ),
}


def _card(topic, domain, recognize, localize, workup, manage, operate, teach, tags, claim_source):
    return {
        "topic": topic,
        "primary_domain": domain,
        "recognize": recognize,
        "localize": localize,
        "workup": workup,
        "manage": manage,
        "operate": operate,
        "teach": teach,
        "tags": tags,
        "source_basis": [
            claim_source,
            "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021), relevant domain chapter and index.",
            *DOMAIN_SOURCES[domain],
        ],
        "evidence_calibrated": "v42.5-review-2026",
        "source_metadata_v408": {
            "canonical_domain": domain,
            "canonical_topic": topic,
            "scope": "verified domain/chapter textbook locator; not a claim-level citation. Time-sensitive or numeric claims require the attached topic-specific guideline/source.",
            "locator_level": "domain-foundational",
            "reviewed_after": "v42.5",
        },
    }


NEW_TOPICS = [
    _card(
        "Orbital Apex Syndrome",
        "Rhinology / Allergy / Skull Base",
        "Ophthalmoplegia (CN III, IV, VI), visual acuity loss or a relative afferent pupillary defect (CN II), "
        "and V1 (± V2) hypesthesia together define orbital apex syndrome. Vision loss is the key discriminator "
        "from a pure superior orbital fissure or cavernous sinus syndrome. In an immunocompromised or "
        "diabetic-ketoacidosis patient with facial pain and eye findings, think invasive fungal sinusitis "
        "(mucormycosis or aspergillosis) until proven otherwise; also consider extension of aggressive "
        "bacterial sinusitis, skull-base tumor, or trauma.",
        "The orbital apex is the narrow confluence where the optic canal (CN II) and superior orbital fissure "
        "(CN III, IV, VI, V1, sympathetic fibers) converge. Compressive or invasive disease here affects both "
        "vision and extraocular motility, unlike superior orbital fissure syndrome (motility and sensory "
        "deficits with preserved vision, since the optic nerve runs through the separate optic canal) or "
        "cavernous sinus syndrome (CN III, IV, VI, V1, V2 ± Horner, typically vision-sparing unless disease "
        "extends posteriorly).",
        "This is an emergency: obtain urgent contrast-enhanced CT and MRI of the orbits/sinuses/skull base, "
        "check glucose/ketones and immune status, and perform immediate bedside nasal endoscopy with biopsy of "
        "any nonviable, dusky, or black-appearing mucosa (especially turbinate) for frozen section and fungal "
        "stain when invasive fungal disease is suspected. Involve ophthalmology for formal visual assessment.",
        "Treat the cause emergently rather than observing. Invasive fungal sinusitis requires immediate "
        "correction of the underlying immunocompromise (e.g., DKA correction), systemic antifungal therapy, "
        "and urgent surgical debridement; bacterial sinusitis needs broad-spectrum IV antibiotics and source "
        "control; tumor causes need urgent oncologic workup. New vision loss is a surgical emergency, not an "
        "indication to wait for further imaging.",
        "Endoscopic (± open) debridement of necrotic or infected tissue for invasive fungal disease, with "
        "orbital decompression when indicated and biopsy for suspected tumor; manage jointly with "
        "ophthalmology, neurosurgery, and infectious disease, and expect serial debridement in fulminant "
        "fungal disease.",
        "Boards pearl: vision loss plus ophthalmoplegia plus V1 numbness localizes to the orbital apex, not "
        "just the cavernous sinus, because the optic canal only shares this exact anatomic bottleneck at the "
        "apex. In a DKA patient with new facial pain or vision change, biopsy for fungal invasion emergently "
        "rather than waiting on imaging alone.",
        ["orbital apex syndrome", "mucormycosis", "invasive fungal sinusitis", "cranial neuropathy", "skull base emergency"],
        "Cummings 7e — orbital apex syndrome anatomy, invasive fungal sinusitis, and emergent multidisciplinary management.",
    ),
    _card(
        "Vernet Syndrome (Jugular Foramen Syndrome)",
        "Otology / Neurotology",
        "Ipsilateral CN IX, X, and XI palsy: loss of gag reflex and posterior-tongue taste (IX), hoarseness, "
        "vocal-fold paralysis, and dysphagia (X), and shoulder droop with weak head-turn to the opposite side "
        "from trapezius/sternocleidomastoid weakness (XI). CN XII (tongue) is spared -- its involvement instead "
        "defines Collet-Sicard syndrome.",
        "The lesion sits at the jugular foramen itself, where IX, X, and XI exit the skull base together; CN "
        "XII exits separately through the hypoglossal canal. Adding hypoglossal (XII) involvement to this "
        "picture is Collet-Sicard syndrome; further extension into the retroparotid/parapharyngeal space with "
        "injury to the adjacent cervical sympathetic chain (producing Horner syndrome) is Villaret syndrome. "
        "Typical causes are glomus jugulare paraganglioma, lower-cranial-nerve schwannoma, metastasis, or "
        "skull-base meningioma.",
        "Contrast MRI/MRA/CTA of the skull base characterizes the jugular foramen mass and its vascularity; "
        "paraganglioma workup includes catheter angiography and embolization planning when appropriate. Add "
        "direct laryngoscopy to confirm vocal-fold mobility and a formal swallow evaluation.",
        "Decide between observation (favored for small, asymptomatic, slow-growing lesions, especially in "
        "older or comorbid patients, since resection risks worsening existing lower-cranial-neuropathy), "
        "stereotactic radiosurgery, or surgical resection based on lesion type, growth, and symptom burden.",
        "Vascular imaging is mandatory before biopsying a suspected paraganglioma given its hypervascularity. "
        "Approach and exposure depend on the specific lesion (e.g., infratemporal fossa approaches for jugular "
        "foramen tumors); protect the remaining lower cranial nerves and the jugular bulb/sigmoid sinus, and "
        "plan for perioperative airway/aspiration management (possible vocal-fold medialization, feeding plan) "
        "since resection can worsen voice and swallow function.",
        "Boards pearl: build the lower-cranial-nerve 'syndrome ladder.' IX + X + XI at the jugular foramen = "
        "Vernet. Add XII (hypoglossal canal) = Collet-Sicard. Add Horner syndrome from sympathetic-chain "
        "involvement in the retroparotid space = Villaret. This ladder is a classic oral-board discrimination "
        "question.",
        ["vernet syndrome", "jugular foramen syndrome", "lower cranial nerves", "paraganglioma", "glomus jugulare"],
        "Cummings 7e — jugular foramen syndrome, lower cranial nerve tumors, and the Vernet/Collet-Sicard/"
        "Villaret discrimination.",
    ),
    _card(
        "Villaret Syndrome (Retroparotid Space Syndrome)",
        "Head & Neck Oncology",
        "Ipsilateral CN IX, X, XI, and XII palsy PLUS Horner syndrome (ptosis, miosis, anhidrosis). This is "
        "Collet-Sicard syndrome (IX-XII) with the added finding of sympathetic-chain injury, which localizes "
        "the lesion to the retroparotid space rather than the jugular foramen or skull base alone.",
        "The retroparotid (retrostyloid/poststyloid parapharyngeal) space contains the carotid sheath (ICA, "
        "IJV), cranial nerves IX-XII as they course extracranially, and the cervical sympathetic chain, all in "
        "close proximity immediately behind the parotid gland. A mass here -- a vagal or sympathetic-chain "
        "schwannoma, paraganglioma, or nodal/malignant disease extending posteriorly -- can compress all of "
        "these structures at once, which is what distinguishes Villaret from Vernet (jugular foramen only, no "
        "XII, no Horner) and from Collet-Sicard (skull base, no Horner).",
        "Cross-sectional imaging characterizes the prestyloid versus poststyloid parapharyngeal compartment "
        "(see Parapharyngeal Space Tumor) together with vascular imaging when a vascular lesion is suspected; "
        "add laryngoscopy and swallow evaluation to document baseline lower-cranial-nerve function.",
        "Management follows the same logic as other parapharyngeal space tumors: observe, irradiate, or resect "
        "based on diagnosis, growth, and symptoms, always characterizing vascularity before any needle biopsy "
        "of a suspected vascular lesion.",
        "Resection is tailored to the compartment and diagnosis; expect and counsel for potential permanent "
        "multi-nerve deficits (voice, swallow, shoulder function, and oculosympathetic findings) and plan "
        "functional rehabilitation proactively rather than reactively.",
        "Boards pearl: Horner syndrome is the key discriminator that elevates a lower-cranial-nerve syndrome "
        "from Collet-Sicard to Villaret, because it means the sympathetic chain in the retroparotid space is "
        "also involved -- localize to that space, not the skull base foramina.",
        ["villaret syndrome", "retroparotid space", "parapharyngeal space", "Horner syndrome", "lower cranial nerves"],
        "Cummings 7e — parapharyngeal/retroparotid space anatomy and the Collet-Sicard/Villaret cranial nerve "
        "syndrome spectrum.",
    ),
    _card(
        "Gradenigo Syndrome (Petrous Apicitis)",
        "Otology / Neurotology",
        "Classic triad: otorrhea/otitis media, retro-orbital or facial pain in a trigeminal (V1) distribution, "
        "and ipsilateral CN VI (abducens) palsy causing diplopia and an inability to abduct the eye. It "
        "typically arises as a complication of acute otitis media or mastoiditis extending to the petrous "
        "apex.",
        "Infection tracks from the middle ear/mastoid into the petrous apex (petrous apicitis, whether the "
        "apex is well pneumatized or not). CN VI travels through Dorello canal beneath the petroclinoid "
        "ligament immediately adjacent to the petrous apex, so inflammation there compresses/irritates the "
        "abducens nerve; adjacent trigeminal ganglion/Meckel cave involvement produces the facial pain.",
        "Temporal bone CT assesses petrous apex opacification or erosion; contrast MRI assesses dural "
        "enhancement, venous sinus involvement, and excludes abscess or further intracranial extension. "
        "Ophthalmology helps characterize the diplopia.",
        "Start IV antibiotics targeting the causative otitis media/mastoiditis organism and obtain source "
        "control with myringotomy and tube placement for drainage and culture. A well-aerated petrous apex "
        "system may resolve with medical management and close monitoring; failure to improve, abscess, or "
        "significant apicitis warrants surgical drainage.",
        "Cross-reference Acute Mastoiditis / Petrous Apicitis for the general operative approach; petrous "
        "apicectomy corridors (retrolabyrinthine, infralabyrinthine, or translabyrinthine in an already-deaf "
        "ear) are chosen based on hearing status and pneumatization pattern, protecting the labyrinth, facial "
        "nerve, carotid artery, and jugular bulb.",
        "Boards pearl: otorrhea + retro-orbital (V1) pain + isolated CN VI palsy after otitis media/mastoiditis "
        "= Gradenigo syndrome. It is specifically the abducens nerve, not the whole cavernous sinus or orbital "
        "apex, because Dorello canal at the petrous apex is the anatomic bottleneck -- this is exactly the kind "
        "of discriminator boards use against orbital apex syndrome (which also affects vision and CN III/IV/V1) "
        "and cavernous sinus syndrome.",
        ["gradenigo syndrome", "petrous apicitis", "abducens palsy", "Dorello canal", "mastoiditis complication"],
        "Cummings 7e — petrous apicitis, Gradenigo syndrome, and petrous apex surgical approaches.",
    ),
]


SIALENDOSCOPY_LITHOTRIPSY_MARKER = "intracorporeal"

SIALENDOSCOPY_MANAGE_ADDITION = (
    " LITHOTRIPSY INDICATIONS: reserve lithotripsy for stones too large or too adherent/impacted for intact "
    "basket capture rather than repeating traumatic basket attempts that risk duct avulsion. Intracorporeal "
    "lithotripsy (holmium or pulsed-dye laser fragmentation, or pneumatic lithotripsy) performed under direct "
    "endoscopic vision is now favored because it fragments the stone and allows retrieval of the pieces in the "
    "same setting; extracorporeal shock-wave lithotripsy (ESWL) is an older alternative that has largely been "
    "supplanted by intracorporeal technique for this reason."
)

SIALENDOSCOPY_TEACH_ADDITION = (
    " Best-case selection for sialendoscopy alone: small, mobile, distal-to-mid duct stones, or duct stenosis "
    "without a large fixed stone. Poor candidates for pure endoscopy: large, impacted, or hilar/intraparenchymal "
    "stones -- these need lithotripsy or a combined approach, not more forceful basket attempts."
)


def _v6_item_id(domain, topic):
    return "v6-" + re.sub(r"[^a-z0-9]+", "-", (domain + "-" + topic).lower()).strip("-")


CLINICAL_CHALLENGES_NEW = [
    {
        "id": "v425-sialolithiasis-parotid-open-01",
        "domain": "Thyroid / Parathyroid / Salivary",
        "topic": "Sialolithiasis",
        "stem": (
            "A 45-year-old has recurrent meal-provoked right cheek swelling. CT shows a 3 mm mobile stone in "
            "the mid Stensen duct. Sialendoscopy is attempted but the stone cannot be visualized due to "
            "technical difficulty, and the surgeon considers open sialolithotomy instead. What is the best "
            "reason to avoid open sialolithotomy as the next step for this parotid stone?"
        ),
        "choices": [
            "The buccal and zygomatic branches of the facial nerve cross directly over Stensen duct, so open "
            "dissection risks facial nerve injury that transoral Wharton duct surgery does not share",
            "Open sialolithotomy is never performed anywhere in the salivary system regardless of gland",
            "The parotid gland has no accessible duct segment at all, making any duct incision impossible",
            "Stensen duct stones dissolve spontaneously with hydration, so no procedure is ever indicated",
        ],
        "answer": 0,
        "explanation": (
            "The facial nerve's buccal and zygomatic branches interdigitate directly over and around the "
            "parotid gland and duct, so an open approach to the duct carries a real facial-nerve injury risk "
            "that does not exist to the same degree with transoral Wharton duct surgery, where only the "
            "lingual nerve is at risk (and only in the posterior floor of mouth). This is the key reason "
            "escalation for parotid stones favors repeat/adjunct sialendoscopy, intracorporeal lithotripsy, or "
            "a combined nerve-monitored approach over open sialolithotomy."
        ),
        "why_wrong": [
            "Correct.",
            "Sialolithotomy is an established option for accessible distal SUBMANDIBULAR (Wharton duct) "
            "stones -- the concern here is specific to parotid anatomy, not duct surgery in general.",
            "The distal Stensen duct is reachable at the buccal mucosa; the anatomic problem is what lies "
            "around it (facial nerve branches) for more proximal open access, not total inaccessibility.",
            "Small stones may pass or respond to conservative measures, but a stone causing recurrent "
            "obstructive symptoms after a failed endoscopic attempt still needs definitive treatment, not "
            "reassurance alone.",
        ],
        "board_pearl": "Parotid stones escalate to lithotripsy or a nerve-monitored combined approach before "
        "open sialolithotomy, because facial nerve branches cross Stensen duct in a way the lingual nerve "
        "does not cross Wharton duct.",
        "curveball": "If the stone were instead 6 mm and impacted at the duct hilum, how would management change?",
        "curveball_answer": (
            "A stone too large or too impacted for intact basket capture is an indication for intracorporeal "
            "lithotripsy (laser or pneumatic fragmentation under direct endoscopic vision) to break it into "
            "basket-retrievable pieces, or a combined endoscopic-assisted transfacial approach with facial "
            "nerve monitoring if lithotripsy fails -- not repeated forceful basket traction, which risks duct "
            "avulsion, and not reflexive open sialolithotomy or parotidectomy."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v425-sialolithiasis-lithotripsy-indication-01",
        "domain": "Thyroid / Parathyroid / Salivary",
        "topic": "Sialendoscopy",
        "stem": (
            "During sialendoscopy for a submandibular stone, the basket cannot be passed around a large, "
            "impacted stone despite gentle repeated attempts. What is the most appropriate next step?"
        ),
        "choices": [
            "Continue firmer basket traction until the stone releases",
            "Convert to intracorporeal lithotripsy (laser or pneumatic fragmentation) to break the stone into "
            "retrievable pieces",
            "Abandon the procedure and proceed directly to gland excision",
            "Leave the basket in place indefinitely as a permanent stent",
        ],
        "answer": 1,
        "explanation": (
            "A stone too large or too adherent for intact basket capture is the classic indication for "
            "intracorporeal lithotripsy under direct endoscopic vision, fragmenting the stone so the pieces can "
            "be retrieved in the same setting while preserving the gland."
        ),
        "why_wrong": [
            "Forcing basket traction on an impacted stone risks duct avulsion and lingual-nerve injury (for "
            "submandibular work) rather than achieving retrieval.",
            "Correct.",
            "Gland excision is reserved for truly irretrievable intraparenchymal disease or an end-stage "
            "nonfunctional gland, not the first response to a single impacted stone during an ongoing "
            "endoscopic attempt.",
            "A trapped basket is a recognized complication to manage and resolve, not an intended permanent "
            "device.",
        ],
        "board_pearl": "Basket impaction on an oversized or adherent stone is a lithotripsy indication, not a "
        "cue to escalate force or abandon gland preservation.",
        "curveball": "What historically limited ESWL's role compared to intracorporeal lithotripsy for salivary stones?",
        "curveball_answer": (
            "Extracorporeal shock-wave lithotripsy (ESWL) fragments stones without direct visualization or "
            "same-session fragment retrieval and has more variable efficacy and availability; intracorporeal "
            "(laser/pneumatic) lithotripsy performed under direct sialendoscopic vision allows the surgeon to "
            "confirm fragmentation and retrieve the pieces in one setting, which is why it has largely "
            "supplanted ESWL for salivary stones."
        ),
        "tier": "Curated board-style",
        "mode": "Reasoning",
    },
    {
        "id": "v425-skull-base-gradenigo-01",
        "domain": "Otology / Neurotology",
        "topic": "Gradenigo Syndrome (Petrous Apicitis)",
        "stem": (
            "A 7-year-old with a week of untreated otitis media develops right otorrhea, retro-orbital pain, "
            "and new diplopia. Exam shows the right eye fails to abduct past midline; pupil, eyelid, and "
            "facial movement are normal, and vision is intact. Which diagnosis best fits?"
        ),
        "choices": [
            "Orbital apex syndrome",
            "Vernet syndrome",
            "Lemierre syndrome",
            "Villaret syndrome",
            "Gradenigo syndrome",
        ],
        "answer": 4,
        "explanation": (
            "Otorrhea/otitis media, retro-orbital (V1) pain, and an isolated abducens (CN VI) palsy causing "
            "failure of abduction -- with normal vision, pupil, and facial nerve function -- is the classic "
            "Gradenigo syndrome triad from otogenic petrous apicitis, where inflammation compresses CN VI in "
            "Dorello canal at the petrous apex."
        ),
        "why_wrong": [
            "Orbital apex syndrome also affects vision (CN II) and typically more than one extraocular nerve, "
            "which are both preserved here.",
            "Vernet syndrome affects CN IX, X, and XI (swallow, voice, shoulder), not the abducens nerve, and "
            "has no otogenic/ophthalmic component.",
            "Lemierre syndrome is septic internal jugular vein thrombophlebitis from oropharyngeal infection "
            "with septic emboli, not an otogenic cranial neuropathy.",
            "Villaret syndrome adds Horner syndrome and CN IX-XII deficits from a retroparotid space process, "
            "not an isolated abducens palsy from otitis media.",
            "Correct.",
        ],
        "board_pearl": "Otorrhea + retro-orbital pain + isolated CN VI palsy after otitis media/mastoiditis = "
        "Gradenigo syndrome; the bottleneck is Dorello canal at the petrous apex.",
        "curveball": "What is the next diagnostic and therapeutic step?",
        "curveball_answer": (
            "Obtain temporal bone CT (petrous apex opacification/erosion) and contrast MRI (dural enhancement, "
            "venous sinus involvement, exclude abscess), start IV antibiotics targeting the causative organism, "
            "and perform myringotomy with tube placement for source control and culture; reserve petrous "
            "apicectomy for failure of medical management, abscess, or significant apicitis."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v425-skull-base-vernet-villaret-01",
        "domain": "Head & Neck Oncology",
        "topic": "Villaret Syndrome (Retroparotid Space Syndrome)",
        "stem": (
            "A patient with a poststyloid parapharyngeal mass has ipsilateral vocal-fold paralysis, absent gag "
            "reflex, weak shoulder shrug, tongue deviation toward the weak side, ptosis, and miosis. Which "
            "syndrome best describes this combination, and what does the ptosis/miosis add anatomically?"
        ),
        "choices": [
            "Vernet syndrome; the ptosis/miosis indicates additional facial nerve involvement",
            "Collet-Sicard syndrome; the ptosis/miosis is incidental and does not change the localization",
            "Villaret syndrome; the ptosis/miosis (Horner syndrome) indicates cervical sympathetic chain "
            "involvement, localizing the lesion to the retroparotid space",
            "Gradenigo syndrome; the ptosis/miosis reflects abducens nerve compression at the petrous apex",
        ],
        "answer": 2,
        "explanation": (
            "CN IX, X, XI, and XII deficits plus Horner syndrome (ptosis, miosis, anhidrosis) define Villaret "
            "syndrome. The Horner component specifically means the cervical sympathetic chain is also involved, "
            "which localizes the process to the retroparotid (poststyloid parapharyngeal) space rather than the "
            "jugular foramen or skull base alone."
        ),
        "why_wrong": [
            "Vernet syndrome involves only CN IX, X, and XI at the jugular foramen, with no CN XII and no "
            "Horner component; ptosis/miosis is Horner syndrome, not a facial nerve (CN VII) finding.",
            "Collet-Sicard syndrome is exactly this CN IX-XII picture WITHOUT Horner syndrome; adding Horner "
            "syndrome is precisely what redefines it as Villaret syndrome, so the ptosis/miosis is not incidental.",
            "Correct.",
            "Gradenigo syndrome is an otogenic CN VI palsy with retro-orbital pain and otorrhea, unrelated to "
            "a parapharyngeal mass or Horner syndrome.",
        ],
        "board_pearl": "Vernet (IX-XI, jugular foramen) -> Collet-Sicard (add XII, skull base) -> Villaret "
        "(add Horner syndrome, retroparotid space) is the lower-cranial-nerve syndrome ladder boards test.",
        "curveball": "What must be done before biopsying this mass, and why?",
        "curveball_answer": (
            "Obtain vascular imaging (CTA/MRA, sometimes catheter angiography) before any needle biopsy, "
            "because a poststyloid parapharyngeal mass causing this nerve/sympathetic pattern may be a vagal "
            "or sympathetic-chain schwannoma or a paraganglioma -- needling a hypervascular lesion risks "
            "significant hemorrhage and adds little diagnostic value when imaging already characterizes it."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
    {
        "id": "v425-skull-base-orbital-apex-01",
        "domain": "Rhinology / Allergy / Skull Base",
        "topic": "Orbital Apex Syndrome",
        "stem": (
            "A 58-year-old with diabetic ketoacidosis develops left facial pain, ophthalmoplegia, decreased "
            "visual acuity, and V1 hypesthesia. Nasal endoscopy shows dusky, nonviable-appearing inferior "
            "turbinate mucosa. What is the most appropriate immediate next step?"
        ),
        "choices": [
            "Discharge with oral antibiotics once the DKA resolves and reimage in one week",
            "Bedside biopsy of the nonviable mucosa for frozen section and fungal stain, with urgent DKA "
            "correction and antifungal therapy",
            "Observation alone, since orbital apex syndrome from sinus disease always resolves with glucose control",
            "Immediate radiation therapy without further diagnostic workup",
        ],
        "answer": 1,
        "explanation": (
            "Vision loss plus ophthalmoplegia plus V1 hypesthesia in a DKA patient with dusky/nonviable nasal "
            "mucosa is invasive fungal sinusitis (mucormycosis) until proven otherwise. This is a surgical and "
            "medical emergency requiring immediate bedside biopsy for fungal confirmation, correction of the "
            "underlying immunocompromise, systemic antifungal therapy, and urgent surgical debridement -- not "
            "observation or delay."
        ),
        "why_wrong": [
            "Delaying diagnosis and treatment in suspected invasive fungal sinusitis risks rapid progression "
            "to intracranial extension and death.",
            "Correct.",
            "Orbital apex syndrome from invasive fungal disease does not reliably resolve with glucose control "
            "alone and requires antifungal therapy and debridement.",
            "Radiation therapy has no role in acute invasive fungal sinusitis and would delay life-saving "
            "surgical debridement and antifungal treatment.",
        ],
        "board_pearl": "Vision loss + ophthalmoplegia + V1 numbness in an immunocompromised or DKA patient "
        "means orbital apex syndrome from invasive fungal sinusitis until biopsy proves otherwise -- biopsy "
        "and treat emergently, do not wait for imaging alone.",
        "curveball": "How does this differ anatomically from a pure cavernous sinus syndrome?",
        "curveball_answer": (
            "Cavernous sinus syndrome affects CN III, IV, VI, V1, and V2 (± Horner) but typically spares vision "
            "unless disease extends posteriorly, because the optic nerve travels through the separate optic "
            "canal rather than the cavernous sinus. Orbital apex syndrome specifically adds CN II involvement "
            "(vision loss/RAPD) because the optic canal and superior orbital fissure converge at the orbital "
            "apex."
        ),
        "tier": "Curated board-style",
        "mode": "Clinical discrimination",
    },
]


def apply_sialendoscopy_lithotripsy_and_skull_base_syndromes_v425(data_module, app_module=None):
    modules = data_module.DEEP_MODULES_V6
    result = {"topics_added": [], "sialendoscopy_deepened": False, "challenges_added": []}

    for card in NEW_TOPICS:
        domain = card["primary_domain"]
        bucket = modules.setdefault(domain, [])
        if not any(x.get("topic") == card["topic"] for x in bucket):
            bucket.append(deepcopy(card))
            result["topics_added"].append(card["topic"])

    salivary = modules.get("Thyroid / Parathyroid / Salivary", [])
    for row in salivary:
        if row.get("topic") == "Sialendoscopy":
            if SIALENDOSCOPY_LITHOTRIPSY_MARKER not in (row.get("manage") or ""):
                row["manage"] = (row.get("manage") or "").rstrip() + SIALENDOSCOPY_MANAGE_ADDITION
                row["teach"] = (row.get("teach") or "").rstrip() + SIALENDOSCOPY_TEACH_ADDITION
                for tag in ("lithotripsy", "intracorporeal lithotripsy"):
                    if tag not in row.get("tags", []):
                        row.setdefault("tags", []).append(tag)
                result["sialendoscopy_deepened"] = True
            break

    topic_domains = {
        card.get("topic"): domain
        for domain, cards in modules.items()
        for card in cards
        if card.get("topic")
    }

    challenges = data_module.CLINICAL_CHALLENGES_V119
    existing_ids = {q.get("id") for q in challenges}
    for q in CLINICAL_CHALLENGES_NEW:
        if q["id"] in existing_ids:
            continue
        row = dict(q)
        canonical_domain = topic_domains.get(row["topic"])
        if canonical_domain is None:
            raise RuntimeError(f"v42.5: challenge topic missing from curriculum: {row['topic']}")
        row["concept_id"] = _v6_item_id(canonical_domain, row["topic"])
        challenges.append(row)
        existing_ids.add(row["id"])
        result["challenges_added"].append(row["id"])

    data_module.CLINICAL_CHALLENGE_BY_ID_V119 = {q["id"]: q for q in challenges if q.get("id")}

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = modules
        app_module.CLINICAL_CHALLENGES_V119 = challenges
        app_module.CLINICAL_CHALLENGE_BY_ID_V119 = data_module.CLINICAL_CHALLENGE_BY_ID_V119
    return result
