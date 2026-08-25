"""v15.9 — Second installment of duplicate-upgrade work from the
audit_content_depth_v155.py findings. Same pattern as vignette_upgrades_v156:
in-place field overwrite by existing ID, no new IDs for the upgraded items,
so the topic's total question count doesn't inflate.
"""

VIGNETTE_UPGRADES_V159 = {
    "v148_rh_02": {
        "stem": "A child with orbital complications of sinusitis has proptosis and limited extraocular movement but no visual acuity change and no radiographic evidence of a discrete abscess — imaging shows diffuse orbital fat stranding without a rim-enhancing collection. According to the Chandler classification, which stage is this, and why does the distinction matter?",
        "choices": [
            "Chandler stage I (preseptal cellulitis) — no orbital involvement, IV antibiotics alone are sufficient",
            "Chandler stage II-III (orbital cellulitis / subperiosteal abscess) — diffuse orbital involvement without a drainable collection typically allows a trial of IV antibiotics with close monitoring, reserving surgery for progression or a later-confirmed abscess",
            "Chandler stage V (cavernous sinus thrombosis) — this finding alone confirms cavernous sinus involvement",
            "The Chandler stage is irrelevant once any orbital sign is present; all cases require immediate surgery regardless of imaging"
        ],
        "answer": 1,
        "explanation": "The Chandler classification distinguishes preseptal cellulitis (I) from orbital cellulitis (II), subperiosteal abscess (III), orbital abscess (IV), and cavernous sinus thrombosis (V). Diffuse orbital involvement without a discrete, rim-enhancing collection generally does not mandate immediate surgery — many stage II/early III cases respond to IV antibiotics with close serial exams, reserving drainage for a confirmed abscess, visual compromise, or failure to improve. Proptosis and limited motility alone (without a drainable collection) do not automatically equal a surgical emergency.",
        "why_wrong": ["This vignette already has orbital signs (proptosis, restricted motility), which excludes preseptal-only disease.", "Correct.", "Cavernous sinus thrombosis is a distinct, more severe entity typically with bilateral signs, cranial neuropathies, or other specific findings — this case does not describe that.", "Ignoring the classification and treating every orbital sign identically overtreats many patients who will respond to medical therapy with close monitoring."],
        "board_pearl": "Chandler stage should directly inform your operative threshold — a discrete, rim-enhancing collection with mass effect (III/IV) is the finding that most changes the conversation toward drainage, not proptosis or motility restriction alone.",
        "curveball": "Serial exam 24 hours later shows worsening visual acuity despite antibiotics, still without a discrete abscess on repeat imaging. Does that change the decision to operate?",
        "learning_stage": "application",
        "focus": "boards",
    },
    "v124_ped_03": {
        "stem": "A child is diagnosed with a thyroglossal duct cyst and is being scheduled for a Sistrunk procedure. Before proceeding to the operating room, what should be confirmed, and why?",
        "choices": [
            "Nothing further is needed; proceed directly to excision",
            "Confirm the presence of a normal, orthotopic thyroid gland (by ultrasound or other imaging) — because in a small but important subset of patients the thyroglossal duct remnant IS the patient's only functioning thyroid tissue, and removing it without recognizing this would render the patient permanently hypothyroid",
            "Confirm the child's blood type in case of massive hemorrhage, which is the primary risk of this operation",
            "Obtain a CT of the chest to exclude mediastinal extension, which occurs in the majority of cases"
        ],
        "answer": 1,
        "explanation": "A small percentage of patients with an apparent thyroglossal duct cyst have ectopic thyroid tissue within the cyst/tract as their only functioning thyroid gland, with no normal orthotopic gland present. Confirming a normal thyroid gland exists (typically via ultrasound, sometimes with thyroid function tests) before excision is a standard preoperative step specifically to avoid inadvertently removing a patient's only thyroid tissue.",
        "why_wrong": ["Skipping this check risks an avoidable, permanent complication in a predictable subset of patients.", "Correct.", "Massive hemorrhage is not the defining risk that drives the specific preoperative imaging recommendation for this operation.", "Mediastinal extension is not a common or expected finding for a typical thyroglossal duct cyst and is not the reason for preoperative imaging here."],
        "board_pearl": "The Sistrunk procedure has a specific preoperative imaging step precisely because of the ectopic-thyroid risk — this is a classic 'know this or cause a real complication' board and practice point.",
        "curveball": "Ultrasound shows no normal orthotopic thyroid tissue — the cyst appears to contain the patient's only thyroid tissue. How does this change the surgical plan?",
        "learning_stage": "application",
        "focus": "OR_prep",
    },
    "v116-fprs-03": {
        "stem": "During open reduction of a confirmed unstable NOE fracture, the medial canthal tendon is found attached to a single, adequately sized bone fragment that can be anatomically repositioned. What is the preferred fixation approach, and why is it preferred over detaching and directly suturing the tendon itself?",
        "choices": [
            "Directly detach the medial canthal tendon from bone and resuture it to soft tissue, since bone fixation is unnecessary",
            "Preserve the tendon's bony attachment and rigidly fix the tendon-bearing fragment back into anatomic position (transnasal canthopexy/wiring when the fragment is inadequate) — because the tendon's pull vector and canthal position are best restored by repositioning the bone it's still attached to, rather than by reattaching a detached tendon to an arbitrary soft-tissue point",
            "Remove the fragment entirely and reconstruct the canthus with only a synthetic implant",
            "No fixation is needed if the telecanthus is mild"
        ],
        "answer": 1,
        "explanation": "When the medial canthal tendon remains attached to a bone fragment of adequate size, the preferred technique is to preserve that native attachment and rigidly reposition the fragment (often with transnasal wiring/canthopexy for reinforcement), since this best restores the tendon's natural three-dimensional vector and canthal position. Detaching an intact tendon-bone unit to resuture soft-tissue-to-soft-tissue sacrifices this natural relationship and more often produces a rounded, malpositioned canthus.",
        "why_wrong": ["Detaching a still-attached, adequately sized fragment discards a natural fixation point that is easier to use than recreating one from soft tissue alone.", "Correct.", "Removing a viable, adequately sized tendon-bearing fragment is unnecessary and abandons the best available fixation option.", "Even mild telecanthus reflects true tendon-bearing fragment displacement in a confirmed unstable NOE fracture and should not be left unaddressed, since it will not self-correct."],
        "board_pearl": "The operative principle in NOE repair is to work with the native canthal-bearing bone whenever it's adequate, rather than defaulting to detaching the tendon — this is the kind of nuance that separates a textbook-adequate repair from a genuinely good aesthetic and functional outcome.",
        "curveball": "The tendon-bearing fragment is severely comminuted into pieces too small to support fixation individually. What alternative canthal fixation strategy becomes necessary?",
        "learning_stage": "senior_decision",
        "focus": "OR_prep",
    },
}


def apply_vignette_upgrades_v159(challenges):
    by_id = {q["id"]: q for q in challenges}
    applied = []
    for qid, fields in VIGNETTE_UPGRADES_V159.items():
        target = by_id.get(qid)
        if target is not None:
            target.update(fields)
            applied.append(qid)
    return applied
