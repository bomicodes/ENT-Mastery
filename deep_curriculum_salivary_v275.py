"""v27.5 — Source-grounded salivary Concept Hub repair.

Rebuilds the legacy "Acute Sialadenitis / Sjögren" card as a clinically coherent
parent salivary-inflammation concept.  The six stages are intentionally distinct:
recognize the syndrome -> classify the cause -> evaluate the phenotype -> manage by
cause -> escalate/procedural decisions -> board-level discriminators.

This patch is applied at runtime after the historical generated curriculum has loaded,
so it replaces (rather than visually hides) duplicated legacy teaching.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _is_target(topic):
    n = _norm(topic)
    # Historical title is "Acute Sialadenitis / Sjögren".  Keep matching robust to
    # punctuation/accent changes or a future small title normalization.
    return "sialadenitis" in n and ("sjogren" in n or "acute sialadenitis" in n)


SALIVARY_REBUILD_V275 = {
    "recognize": (
        "Recognize sialadenitis as a syndrome of salivary-gland inflammation or impaired drainage, then use the tempo and symptom pattern to decide what is driving it. "
        "Acute bacterial disease usually causes a tender, swollen gland with erythema, fever or systemic symptoms and may express purulence from Stensen or Wharton duct. "
        "Recurrent swelling and pain that predictably worsen with meals strongly suggest obstruction. Chronic xerostomia, difficulty swallowing dry food, needing water at night, dental caries or oral candidiasis together with gritty/burning dry eyes (keratoconjunctivitis sicca) should raise concern for Sjögren syndrome or another cause of salivary hypofunction rather than simple infection."
    ),
    "localize": (
        "Classify the process before ordering tests. Obstructive sialadenitis (stone, duct stenosis or mucus plug) is typically episodic and meal-related; submandibular stones are especially common. Acute suppurative bacterial sialadenitis is painful and inflammatory, often in a dehydrated, postoperative, frail or otherwise salivary-stasis patient. Viral disease more often produces diffuse or bilateral gland swelling without ductal pus. Autoimmune Sjögren disease produces chronic glandular hypofunction with oral and ocular sicca and may cause recurrent or persistent parotid enlargement. Also consider medication-related xerostomia, prior radiation or radioiodine, granulomatous disease and neoplasm when the pattern does not fit infection or obstruction. Localize the involved gland and duct on inspection, bimanual palpation and duct massage."
    ),
    "workup": (
        "Let the suspected cause determine the evaluation. Inspect the oral cavity and duct papillae, massage the gland for saliva or purulence, palpate the floor of mouth and gland, and culture expressed pus when it will guide antimicrobial therapy. Ultrasound is useful for gland inflammation, ductal dilation and many stones; CT is valuable when a deep abscess, complicated infection or a poorly visualized calculus is suspected. Persistent focal mass, asymmetric gland enlargement or unexplained adenopathy deserves a neoplasm-directed workup rather than repeated empiric antibiotics. For suspected Sjögren syndrome, review xerogenic medications and systemic features, obtain anti-SSA/Ro with appropriate rheumatologic laboratory assessment, and coordinate objective ocular and salivary testing. The 2016 ACR/EULAR *classification* framework weights anti-SSA/Ro and focal lymphocytic sialadenitis on labial biopsy most heavily, with ocular staining, Schirmer testing and unstimulated whole-saliva flow contributing additional points; classification criteria support, but do not replace, clinical diagnosis."
    ),
    "manage": (
        "Treat the cause, not the label. Acute uncomplicated bacterial sialadenitis is managed with hydration, warm compresses, gland massage, sialogogues, meticulous oral hygiene and antibiotics directed at typical oral flora/staphylococcal pathogens and local resistance patterns; drain a true abscess and escalate care for sepsis, airway/deep-neck extension or failure of medical therapy. Obstructive disease requires restoration of drainage—conservative measures for mild episodes, then stone extraction or sialendoscopy when obstruction persists or recurs. Viral disease is generally supportive unless a specific infection changes management. Sjögren care focuses on preserving ocular and oral function: frequent hydration, saliva substitutes/stimulation when appropriate, aggressive dental prevention/fluoride and candidiasis surveillance, ophthalmologic dry-eye therapy, avoidance of unnecessary xerogenic drugs, and rheumatology involvement for systemic disease."
    ),
    "operate": (
        "Escalate when anatomy or complications make conservative care inadequate. Recurrent obstructive symptoms, duct stenosis or accessible stones may be treated with gland-preserving sialendoscopy and/or transoral stone removal; gland excision is reserved for selected refractory disease after weighing nerve, scar and xerostomia consequences. Image and drain suppurative collections that do not resolve with antibiotics. In a patient with Sjögren syndrome, persistent unilateral/asymmetric major-gland enlargement, a discrete mass, firm nodes, constitutional symptoms or other concerning change is not 'just another flare'—evaluate for lymphoproliferative disease, because Sjögren carries a clinically important increased risk of B-cell non-Hodgkin lymphoma."
    ),
    "teach": (
        "Boards/rounds framework: MEALS = obstruction; PUS + acute tenderness/systemic inflammation = bacterial suppurative sialadenitis; BILATERAL/DIFUSE viral-pattern swelling = consider viral causes; SICCA = think salivary hypofunction/Sjögren after excluding common mimics such as medications and radiation. Sjögren sicca means more than 'dry mouth': ask about dry eyes, dry-food dysphagia, nighttime water use, dental decay and candidiasis, and remember extraglandular autoimmune disease. A nonzero antibody test alone does not make the diagnosis, and isolated anti-SSB/La is not part of the 2016 ACR/EULAR weighted criteria. The red-flag pearl is persistent asymmetric gland enlargement or adenopathy in Sjögren—work it up for lymphoma rather than repeatedly treating presumed sialadenitis."
    ),
    "source_basis": [
        "Cummings Otolaryngology—Head and Neck Surgery, 7e — inflammatory/obstructive salivary gland disease and Sjögren syndrome",
        "K.J. Lee's Essential Otolaryngology, 12e — salivary gland disorders",
        "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide — salivary gland disorders",
        "2016 ACR/EULAR Classification Criteria for Primary Sjögren Syndrome (Shiboski et al.)",
    ],
    "source_grounded_v275": True,
}


def apply_salivary_concept_rebuild_v275(data_module, app_module=None):
    domain_name = "Thyroid / Parathyroid / Salivary"
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(domain_name, [])
    patched = []
    for module in modules:
        if not _is_target(module.get("topic")):
            continue
        for field in FIELDS:
            module[field] = SALIVARY_REBUILD_V275[field]
        module["source_basis"] = list(SALIVARY_REBUILD_V275["source_basis"])
        module["source_grounded_v275"] = True
        patched.append(module.get("topic"))

    # app.py imported DEEP_MODULES_V6 by reference, but make the binding explicit
    # for deployments where a future loader swaps the dictionary object.
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6

    return {"patched": patched, "count": len(patched)}
