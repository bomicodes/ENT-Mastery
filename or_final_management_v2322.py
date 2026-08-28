"""v23.22 final OR Tomorrow procedure-specific management review.

Closes the final five generic-only modules identified by the full production inventory:
laryngeal botulinum toxin injection, lingual tonsillectomy/tongue-base reduction,
pharyngocutaneous fistula management, reconstructive palatal OSA surgery, and
tracheoesophageal puncture. Existing operative/anatomic content remains intact.
"""

TARGETS = [
    {
        "slug": "laryngeal-botox",
        "title_terms": ("laryngeal", "botulinum"),
        "setup": [
            "Before laryngeal botulinum toxin injection, confirm the treated phenotype and target rather than using dysphonia alone as the indication. Distinguish adductor versus abductor laryngeal dystonia from essential voice tremor, muscle-tension dysphonia and structural/neurologic mimics, review prior injection site/dose/benefit/duration/adverse effects, and document baseline voice and swallowing because the desired weakening and the risk profile depend on the muscle being treated.",
            "Select the target muscle and dose according to phenotype and prior response, using EMG/endoscopic guidance as appropriate to the technique. In patients with baseline dysphagia, poor pulmonary reserve or prior excessive breathiness/aspiration, plan a conservative adjustment rather than simply repeating the previous dose; bilateral posterior-cricoarytenoid weakening carries a distinct airway risk and should be approached with particular caution.",
        ],
        "postop": [
            "After laryngeal botulinum toxin injection, expected temporary voice change should be distinguished from clinically important dysphagia/aspiration or respiratory compromise. Progressive dyspnea/stridor, inability to manage secretions, aspiration symptoms or pneumonia requires prompt laryngeal/swallow reassessment rather than reassurance that weakness is an intended effect.",
            "Track onset, peak benefit, duration and adverse effects after each cycle. An unexpectedly poor response should trigger reassessment of diagnosis, target accuracy, dose and competing voice disorders rather than automatic dose escalation at the next visit.",
        ],
        "marker": "laryngeal_botox_management_v2322",
    },
    {
        "slug": "lingual-tonsillectomy",
        "title_terms": ("lingual", "tonsillectomy"),
        "setup": [
            "Before lingual tonsillectomy/tongue-base reduction for sleep-disordered breathing, confirm that tongue-base/lingual-tonsil obstruction is a meaningful contributor using examination and sleep evaluation, with DISE or other localization when appropriate, rather than treating residual OSA as a single-level problem by default. Review prior adenotonsillectomy, obesity, craniofacial/neuromuscular disease, central-event burden and other collapse sites because multilevel disease changes both expected benefit and postoperative risk.",
            "Plan the airway, exposure and extent of reduction around the vallecula, epiglottis and tongue-base vasculature while preserving functional tongue base and avoiding unnecessary deep injury. Severe baseline OSA, difficult airway, significant comorbidity or extensive reduction should influence postoperative monitoring/disposition before the case begins.",
        ],
        "postop": [
            "After lingual tonsil/tongue-base surgery, progressive tongue-base edema, stridor, increased work of breathing, inability to manage secretions or recurrent desaturation is an airway concern and requires prompt reassessment. Brisk oral bleeding, repeated swallowing/hematemesis or hemodynamic change should be treated as a postoperative hemorrhage emergency rather than routine blood-tinged saliva.",
            "Assess hydration, pain and swallowing/aspiration before routine diet progression. Persistent OSA symptoms should be evaluated objectively after healing because residual multilevel collapse is common; lack of cure does not necessarily mean the tongue-base operation technically failed.",
        ],
        "marker": "lingual_tonsillectomy_management_v2322",
    },
    {
        "slug": "pharyngocutaneous-fistula",
        "title_terms": ("pharyngocutaneous", "fistula"),
        "setup": [
            "Before operative management of a pharyngocutaneous fistula/salivary leak, define timing, size, tissue quality, infection/abscess, prior radiation, nutritional status, thyroid status when relevant and whether major vessels or reconstruction hardware are exposed. Small controlled leaks in stable tissue may heal with drainage, wound care, salivary diversion and nutritional support, whereas uncontrolled sepsis, large defects, irradiated tissue, exposed carotid/hardware or failure of conservative management can require debridement and vascularized tissue reconstruction.",
            "Review imaging when deep collection, vascular proximity or an ill-defined tract is suspected and establish enteral nutrition away from the leak when appropriate. If the wound approaches the carotid, plan vessel protection as part of reconstruction rather than treating skin closure alone as definitive source control.",
        ],
        "postop": [
            "After fistula treatment, increasing neck erythema/swelling, fever, purulence, enlarging salivary output or systemic toxicity should prompt evaluation for persistent leak, deep infection or inadequate source control. Nutrition and wound care should continue until durable separation of the pharynx from the neck is demonstrated rather than advancing solely by elapsed postoperative days.",
            "Any sentinel oral or neck bleeding from an irradiated/infected fistula bed with carotid exposure risk must be treated as possible carotid blowout until proven otherwise. Escalate immediately for airway protection, hemorrhage control and endovascular/open vascular management; do not repeatedly probe or pack a threatened vessel at bedside without a definitive rescue plan.",
        ],
        "marker": "pharyngocutaneous_fistula_management_v2322",
    },
    {
        "slug": "reconstructive-palate",
        "title_terms": ("reconstructive", "palatal", "osa"),
        "setup": [
            "Before reconstructive palatal surgery for OSA, confirm objective sleep-disordered breathing, review PAP tolerance and localize retropalatal collapse within the full multilevel airway rather than selecting a palatal procedure from snoring alone. Tonsil size, lateral-wall versus anteroposterior collapse, prior palatal surgery, BMI/comorbidity and tongue-base/hypopharyngeal obstruction should determine whether palatal reconstruction is appropriate and which reconstructive vector is most rational.",
            "Counsel that the goal is to stabilize/enlarge the retropalatal airway while preserving swallowing and velopharyngeal function, not simply excise more palate. Baseline dysphagia, speech/velopharyngeal problems and scar from prior UPPP or tonsil surgery should alter technique and expectations; severe OSA or major comorbidity should change postoperative monitoring plans.",
        ],
        "postop": [
            "After reconstructive palate surgery, airway obstruction, progressive edema, recurrent desaturation or inability to manage secretions requires prompt airway assessment, and brisk oral bleeding/hematemesis is a hemorrhage emergency. Hydration and analgesia matter, but respiratory or bleeding deterioration should not be attributed to expected postoperative pain.",
            "Later persistent dysphagia, nasal regurgitation/hypernasality, nasopharyngeal stenosis or chronic globus requires functional examination rather than reassurance alone. OSA outcome should be assessed objectively after healing because symptom improvement or less snoring does not reliably establish physiologic resolution.",
        ],
        "marker": "reconstructive_palate_management_v2322",
    },
    {
        "slug": "tep",
        "title_terms": ("tracheoesophageal", "puncture"),
        "setup": [
            "Before tracheoesophageal puncture, determine whether primary or secondary TEP is appropriate from the oncologic/reconstructive course, pharyngeal healing, prior radiation, stoma anatomy, manual dexterity/cognition, pulmonary reserve, aspiration risk and access to speech-language pathology/prosthesis care. Confirm that the party wall and neopharyngeal lumen are suitable for safe puncture; a technically possible tract is not useful without a realistic rehabilitation and maintenance plan.",
            "For secondary TEP, evaluate for stenosis, fistula, recurrence or anatomy that makes rigid/flexible visualization difficult before puncture. Plan prosthesis size and tract management with the speech-language pathologist and distinguish voice rehabilitation goals from management of an existing leaking or dysfunctional prosthesis.",
        ],
        "postop": [
            "After TEP/prosthesis placement, distinguish leakage through the prosthesis from leakage around it because valve failure, sizing/fit, tract dilation, infection/granulation and high swallowing pressures require different solutions. Persistent aspiration through or around the prosthesis should be addressed promptly rather than accepted as the cost of speech rehabilitation.",
            "A missing/dislodged prosthesis should prompt evaluation for aspiration into the tracheobronchial tree and protection of the TEP tract from unwanted closure according to local protocol. Progressive stomal/TEP bleeding, inability to pass the prosthesis, new severe dysphagia, granulation or recurrent leakage also warrants evaluation for mechanical problems, stenosis, tissue breakdown or recurrent disease rather than repeated empiric resizing alone.",
        ],
        "marker": "tep_management_v2322",
    },
]


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
    out = list(values or [])
    changed = False
    for text in reversed(additions):
        marker = text[:72].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def apply_or_final_management_v2322(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target["setup"])
        op["postop"], c2 = _prepend_unique(op.get("postop"), target["postop"])
        op[target["marker"]] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
