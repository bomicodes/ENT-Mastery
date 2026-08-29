"""v27.7 — source-grounded salivary obstruction Concept Hub rebuild.

Rebuilds the canonical Submandibular Sialolithiasis and Sialendoscopy cards as
six clinically distinct resident-level layers.  The intent is to teach a usable
diagnostic/management progression rather than repeat a stone/scope pearl in
multiple boxes.
"""

DOMAIN = "Thyroid / Parathyroid / Salivary"


def _norm(value):
    import re
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _find_module(data, candidates):
    modules = data.DEEP_MODULES_V6.get(DOMAIN, [])
    wanted = {_norm(x) for x in candidates}
    return next((m for m in modules if _norm(m.get("topic")) in wanted), None)


SIALOLITHIASIS = {
    "recognize": (
        "Recognize salivary duct obstruction from the history before reaching for imaging. The classic presentation is "
        "recurrent unilateral submandibular swelling and colicky pain that begins or worsens with meals as stimulated "
        "saliva backs up behind an obstruction. Examine the floor of mouth and Wharton duct for a palpable stone, reduced "
        "salivary flow, or turbid/purulent saliva. Fever, persistent tenderness, erythema, or pus suggests secondary acute "
        "bacterial sialadenitis on top of the obstruction rather than uncomplicated stone disease."
    ),
    "localize": (
        "Localize the obstruction by gland, duct segment, and cause. Submandibular stones are especially common because "
        "Wharton duct is long and ascends against gravity and submandibular saliva is relatively mucinous and mineral rich. "
        "Anterior/distal duct stones may be palpable in the floor of mouth; hilar/proximal stones sit near the posterior "
        "mylohyoid border and gland. Not every obstructed gland contains a stone: duct stenosis, mucus plugs, scar, or less "
        "commonly a mass can produce the same meal-provoked physiology."
    ),
    "workup": (
        "Evaluate the duct and gland deliberately: inspect the papilla, bimanually palpate the entire floor of mouth, and "
        "massage the gland while observing the quantity and quality of saliva. Ultrasound is a useful radiation-free first "
        "study for many stones and gland inflammation; thin-cut noncontrast CT is highly sensitive for calcified stones and "
        "helps when the stone is deep, proximal, multiple, or the diagnosis is uncertain. Contrast CT is favored when abscess "
        "or deep-space infection is a concern. Persistent obstructive symptoms with negative stone imaging should prompt "
        "consideration of stenosis or another ductal lesion, often evaluated directly with sialendoscopy."
    ),
    "manage": (
        "Match treatment to obstruction and infection rather than excising the gland by habit. During uncomplicated episodes, "
        "hydration, gland massage, warm compresses, analgesia, and sialogogues can improve flow. Superimposed suppurative "
        "sialadenitis needs appropriate antibiotics and drainage/source control if an abscess forms. Definitive treatment is "
        "gland-preserving whenever feasible: distal palpable submandibular stones are often removed transorally; mobile small "
        "duct stones may be retrieved endoscopically; proximal/hilar disease may require sialendoscopy-assisted or combined "
        "transoral approaches."
    ),
    "operate": (
        "Choose the operative corridor from stone location and duct anatomy. For transoral submandibular duct surgery, identify "
        "the duct and remember that the lingual nerve loops beneath/around Wharton duct in the posterior floor of mouth; proximal "
        "dissection therefore carries lingual-nerve risk. Sialendoscopy can dilate stenoses, retrieve selected stones, and guide "
        "combined approaches while preserving the gland. Submandibular gland excision is reserved for selected irretrievable "
        "intraparenchymal/proximal disease, severely damaged glands, or recurrent disease not amenable to gland-preserving care; "
        "its risks include marginal mandibular, lingual, and hypoglossal nerve injury."
    ),
    "teach": (
        "Boards/chief framework: MEAL-RELATED swelling means think obstruction; PUS means obstruction may now be infected. First "
        "localize distal versus hilar/proximal disease, then choose the least destructive route that clears the obstruction. "
        "Modern management is gland-preserving: a submandibular stone is not synonymous with submandibular gland excision. "
        "A negative CT for stone does not end the workup when the history is convincingly obstructive—stenosis and noncalcified "
        "duct pathology remain possibilities."
    ),
    "tags": ["sialolithiasis", "Wharton duct", "submandibular gland", "meal-related swelling", "duct obstruction", "lingual nerve", "sialendoscopy"],
    "source_basis": ["Cummings 7e", "K.J. Lee 12e", "Pasha 6e"],
    "source_grounded_v277": True,
}


SIALENDOSCOPY = {
    "recognize": (
        "Recognize sialendoscopy as a diagnostic and gland-preserving therapeutic platform for obstructive salivary disease, "
        "not simply a camera used after a stone is already proven. Appropriate problems include recurrent meal-related gland "
        "swelling from mobile duct stones, duct stenosis/scar, mucus/debris, and selected recurrent inflammatory obstruction. "
        "The important preoperative question is whether the disease is intraductal and endoscopically accessible versus a large, "
        "fixed hilar/intraparenchymal stone or a gland/mass process that requires a different approach."
    ),
    "localize": (
        "Think in a duct map. The papilla and distal duct are the entry corridor; branching secondary/tertiary ducts become "
        "progressively smaller and more fragile. In the submandibular system, posterior duct work occurs near the lingual nerve; "
        "in the parotid system, Stensen duct traverses the masseter then turns medially through buccinator. Stone size, mobility, "
        "impaction, duct caliber, and distance from the papilla determine whether pure endoscopic extraction is realistic or a "
        "combined approach is safer."
    ),
    "workup": (
        "Before endoscopy, confirm that the symptom pattern is truly obstructive and review ultrasound/CT when they will change "
        "planning. Define stone number, size, location, mobility, duct dilation/stenosis, and active infection. Sialendoscopy itself "
        "can diagnose stenosis, mucus plugs, inflammatory debris, or small stones missed on imaging. Avoid turning an acutely "
        "infected, edematous duct into an elective instrumentation problem; treat significant acute suppurative infection first "
        "unless urgent drainage/source control is otherwise required."
    ),
    "manage": (
        "Use the least invasive technique that restores durable flow. Small mobile stones can be removed with endoscopic baskets "
        "or forceps; stenoses may be dilated and selected inflammatory narrowing treated with irrigation/local therapy according "
        "to the clinical setting. Larger impacted stones often need endoscopic localization plus a limited transoral or transfacial "
        "combined approach rather than repeated traumatic attempts at basket extraction. Failure of pure endoscopy should trigger "
        "a change in strategy, not reflex gland sacrifice."
    ),
    "operate": (
        "Cannulate and progressively dilate the papilla gently, maintain continuous irrigation for visualization, and advance under "
        "direct vision rather than forcing the scope against resistance. Protect the duct wall from perforation, false passage, "
        "basket entrapment, and avulsion. When combining endoscopy with an incision, use the illuminated/localized stone to minimize "
        "dissection and preserve the duct and nearby nerves. Counsel about postoperative edema, duct perforation/stenosis, infection, "
        "retained/recurrent stones, temporary tongue/floor-of-mouth symptoms, and the possibility that a second or combined procedure "
        "may be needed."
    ),
    "teach": (
        "Boards/chief framework: sialendoscopy is both DIAGNOSTIC and THERAPEUTIC. It is strongest for intraductal obstruction and "
        "gland preservation, but it is not a mandate to remove every stone endoscopically. Small/mobile/intraductal favors pure "
        "endoscopy; large/impacted/hilar disease often favors a combined approach; inaccessible intraparenchymal disease may still "
        "require gland surgery. The endpoint is restored salivary flow with the least morbidity, not successful deployment of a scope."
    ),
    "tags": ["sialendoscopy", "salivary duct", "stone retrieval", "duct stenosis", "gland preservation", "combined approach"],
    "source_basis": ["Cummings 7e", "K.J. Lee 12e", "Pasha 6e"],
    "source_grounded_v277": True,
}


def apply_salivary_obstruction_rebuild_v277(data):
    repaired = []
    targets = [
        (("Submandibular Sialolithiasis",), SIALOLITHIASIS),
        (("Sialendoscopy",), SIALENDOSCOPY),
    ]
    for candidates, fields in targets:
        module = _find_module(data, candidates)
        if module is None:
            continue
        module.update(fields)
        repaired.append(module.get("topic"))
    return {"repaired": repaired, "count": len(repaired)}
