"""v27.6 — source-grounded salivary complication Concept Hub repair.

Deepens First-Bite Syndrome and Frey Syndrome as separate, clinically coherent
post-parotid/parapharyngeal entities. Each ladder stage has a distinct purpose:
recognize -> localize mechanism -> evaluate -> manage -> advanced/procedural
strategy -> boards/teaching discrimination.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


FIRST_BITE_V276 = {
    "recognize": (
        "Recognize first-bite syndrome by its characteristic timing: sudden, severe cramping or electric pain in the parotid/preauricular region with the first bite of a meal, often maximal with sour or highly salivatory foods, followed by rapid diminution over subsequent bites. The history is often more diagnostic than the physical examination. It classically appears after surgery involving the deep parotid lobe, parapharyngeal space, upper cervical sympathetic chain, or external carotid artery region, but a similar pattern can occasionally herald an untreated parapharyngeal/deep-lobe lesion."
    ),
    "localize": (
        "Localize the problem to autonomic innervation of the parotid rather than the TMJ, teeth, trigeminal neuralgia, or recurrent suppurative sialadenitis. The leading mechanism is loss or disruption of sympathetic input to parotid myoepithelial cells with relatively unopposed parasympathetic stimulation when salivation begins. That physiology explains why pain peaks with the first salivary stimulus and then fades during the meal. Prior deep-lobe parotidectomy, parapharyngeal tumor resection, carotid-space surgery, or sympathetic chain injury makes the diagnosis especially likely."
    ),
    "workup": (
        "Diagnosis is usually clinical. Reconstruct the operative history and map the pain precisely: first-bite onset, parotid distribution, meal trigger, rapid within-meal adaptation, and absence of purulence or inflammatory gland swelling. Examine the parotid, oral cavity, dentition, TMJ and cranial nerves to exclude mimics. Imaging is not routinely required in a classic postoperative presentation, but new first-bite symptoms without a clear surgical cause, a palpable mass, cranial neuropathy, persistent pain between meals, or progressive asymmetry should prompt imaging of the parotid/parapharyngeal and upper neck spaces to exclude occult tumor or another structural process."
    ),
    "manage": (
        "Start by explaining the benign but often intrusive autonomic pain pattern and discussing observation because symptoms may lessen over time. Trigger modification and smaller/less salivatory first bites can help some patients. Neuropathic pain medications have inconsistent benefit. For persistent symptoms that impair eating or quality of life, intraparotid botulinum toxin is the most useful minimally invasive option in contemporary practice; it reduces cholinergic salivary stimulation and can substantially reduce attack severity or frequency, although repeat treatment may be needed."
    ),
    "operate": (
        "Do not reflexively reoperate on the gland for first-bite syndrome. The advanced decision is whether symptoms are severe enough to justify image-guided or anatomically targeted botulinum toxin treatment and whether the presentation is atypical enough to demand renewed tumor evaluation. Historical surgical denervation procedures and gland excision carry meaningful morbidity and inconsistent efficacy, so they are rarely preferred solely for this syndrome. Prevention centers on understanding the sympathetic structures at risk during deep parotid/parapharyngeal and carotid-space surgery, while recognizing that oncologic clearance takes priority over preserving a nerve pathway when the two conflict."
    ),
    "teach": (
        "Boards/rounds pearl: FIRST BITE = pain; FREY = sweating/flushing. First-bite syndrome is immediate meal-triggered parotid pain that is worst on the first bite and wanes as eating continues, usually after deep parotid/parapharyngeal or sympathetic-chain-region surgery. Think sympathetic denervation with unopposed parasympathetic salivary stimulation. A classic postoperative history usually needs no elaborate testing, but first-bite symptoms in a patient without prior surgery should make you look for a deep parotid/parapharyngeal lesion rather than simply labeling the pain idiopathic."
    ),
    "source_basis": [
        "Cummings Otolaryngology—Head and Neck Surgery, 7e — salivary gland surgery and postoperative complications",
        "K.J. Lee's Essential Otolaryngology, 12e — salivary/parotid disorders and syndromes",
        "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide — parotid and salivary gland complications",
        "Contemporary first-bite syndrome literature supporting intraparotid botulinum toxin for persistent symptoms",
    ],
    "source_grounded_v276": True,
}


FREY_V276 = {
    "recognize": (
        "Recognize Frey syndrome as gustatory sweating, warmth, flushing, or tingling over the preauricular/temporal skin during eating after parotid-region surgery or trauma. Symptoms often emerge months after parotidectomy rather than immediately postoperatively. Ask specifically about sweating or erythema triggered by chewing or salivatory foods; mild disease is commonly underreported unless the history is elicited."
    ),
    "localize": (
        "Localize the mechanism to aberrant autonomic reinnervation across the parotid bed. Postganglionic parasympathetic fibers that previously traveled with the auriculotemporal nerve toward the parotid can regenerate into denervated cutaneous sweat glands and superficial vessels. Salivatory stimulation is therefore misdirected into sweating and vasodilation of the overlying skin. This is fundamentally different from first-bite syndrome, which is a pain syndrome linked to altered sympathetic-parasympathetic balance rather than aberrant reinnervation of sweat glands."
    ),
    "workup": (
        "A characteristic history is usually sufficient for clinically significant Frey syndrome. Document the surface area and severity of gustatory sweating/flushing and how much it affects quality of life. The Minor starch-iodine test can objectively map the involved skin: iodine is applied and allowed to dry, starch is added, and gustatory stimulation produces a dark color change where sweating occurs. Routine imaging is unnecessary unless the examination or history raises a separate concern for recurrent disease or another structural problem."
    ),
    "manage": (
        "Treat only if symptoms are bothersome. Reassurance is appropriate for mild disease. Topical antiperspirant or anticholinergic strategies can help selected patients but are limited by irritation or systemic adverse effects. Intradermal botulinum toxin across the mapped symptomatic area is highly effective for clinically significant Frey syndrome and is the preferred nonsurgical treatment; benefit commonly lasts for months and repeat injections can be performed when symptoms recur."
    ),
    "operate": (
        "Prevention is more relevant surgically than late reoperation. During parotidectomy, interposition of tissue between the skin flap and parotid bed—such as a SMAS flap, temporoparietal fascia flap, sternocleidomastoid flap, dermal-fat graft, or other barrier in selected cases—can reduce aberrant parasympathetic reinnervation and may also improve contour. Choice depends on defect size, oncologic constraints, prior treatment, surgeon preference and donor-site tradeoffs. Once symptomatic Frey syndrome is established, botulinum toxin is generally favored over surgical attempts at denervation because it is effective and far less morbid."
    ),
    "teach": (
        "Boards/rounds framework: after parotidectomy, gustatory SWEATING/FLUSHING = Frey syndrome; severe PAROTID PAIN with the first bite = first-bite syndrome. Frey is caused by aberrant parasympathetic regeneration to sweat glands and cutaneous vessels, can be demonstrated with the Minor starch-iodine test, and is treated most reliably with intradermal botulinum toxin when symptomatic. Interposition barriers at the initial parotid operation are the key surgical prevention concept."
    ),
    "source_basis": [
        "Cummings Otolaryngology—Head and Neck Surgery, 7e — parotidectomy complications and reconstruction",
        "K.J. Lee's Essential Otolaryngology, 12e — Frey syndrome and salivary gland surgery",
        "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide — parotidectomy complications",
        "Contemporary evidence supporting botulinum toxin and interposition barriers for symptomatic/preventive management",
    ],
    "source_grounded_v276": True,
}


def _apply(module, rebuild):
    for field in FIELDS:
        module[field] = rebuild[field]
    module["source_basis"] = list(rebuild["source_basis"])
    module["source_grounded_v276"] = True


def apply_salivary_complication_rebuild_v276(data_module, app_module=None):
    domain = "Thyroid / Parathyroid / Salivary"
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(domain, [])
    patched = []
    for module in modules:
        topic = _norm(module.get("topic"))
        if topic == "first bite syndrome":
            _apply(module, FIRST_BITE_V276)
            patched.append(module.get("topic"))
        elif topic == "frey syndrome":
            _apply(module, FREY_V276)
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
