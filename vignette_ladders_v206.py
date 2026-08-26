"""v20.6 — deliberate learning-ladder curation, Rhinology pass 2.

Reviews the next five canonical Rhinology foundations. Existing strong v14.x
second-pass cases are reused as application layers for CRSwNP and endoscopic CSF
leak repair rather than duplicated. Only genuinely missing layers are added.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"


def _q(qid, topic, stage, stem, choices, answer, explanation, why_wrong,
       pearl, curveball, focus):
    return {
        "id": qid, "domain": DOMAIN, "topic": topic,
        "learning_stage": stage, "stem": stem, "choices": choices,
        "answer": answer, "explanation": explanation, "why_wrong": why_wrong,
        "board_pearl": pearl, "curveball": curveball,
        "tier": "Curated learning ladder", "mode": "Vignette",
        "focus": focus, "ladder_reviewed": True,
    }


REVIEWED_FOUNDATION_IDS_V206 = {
    "v136_rhi_06",  # CRSsNP
    "v136_rhi_07",  # CRSwNP
    "v136_rhi_08",  # Endoscopic CSF Leak Repair / Nasoseptal Flap
    "v136_rhi_09",  # Endoscopic Maxillary Antrostomy
    "v136_rhi_10",  # Ethmoidectomy
}

REUSED_APPLICATION_IDS_V206 = {
    "v141_rhi_03": "CRSwNP",
    "v142_rhi_01": "Endoscopic CSF Leak Repair / Nasoseptal Flap",
}


VIGNETTES_V206 = [
    _q(
        "v206_rhi_crssnp_app", "CRSsNP", "application",
        "A patient has 6 months of nasal obstruction and mucopurulent drainage with CT-confirmed bilateral ethmoid and maxillary inflammation but no polyps. Symptoms persist despite reliable saline irrigation and intranasal corticosteroid use. Before offering ESS, what is the best next principle?",
        [
            "Confirm that symptoms and objective disease still correlate, reassess modifiable drivers such as odontogenic disease or immune dysfunction, and use shared decision-making about surgery",
            "Require an arbitrary fixed number of antibiotic courses before surgery regardless of phenotype",
            "Start a biologic solely because CT shows inflammation without polyps",
            "Diagnose migraine because all facial symptoms with CRSsNP are nonrhinogenic",
        ], 0,
        "CRSsNP surgical candidacy is not defined by a universal medication checklist. Persistent symptom burden plus objective disease after individualized therapy should prompt reassessment of diagnosis, comorbid drivers, and goals before ESS; treatment should match the mechanism rather than satisfy an arbitrary duration rule.",
        [
            "Correct. The decision should connect objective disease, symptom burden, prior appropriate therapy, and correctable secondary causes.",
            "Rigid antibiotic quotas are not a substitute for individualized diagnosis and treatment response.",
            "Biologic therapy is not routinely indicated simply because nonpolypoid CRS persists on CT.",
            "Migraine can coexist or mimic sinonasal pain, but objective chronic inflammation with drainage and obstruction should not be dismissed wholesale.",
        ],
        "For CRSsNP, surgery treats persistent objective disease after individualized medical management; it is not earned by completing a medication checklist.",
        "What unilateral maxillary CT pattern would make dental source control part of the preoperative plan?",
        "boards",
    ),
    _q(
        "v206_rhi_crssnp_snr", "CRSsNP", "senior_decision",
        "A patient remains symptomatic after prior ESS. Endoscopy shows a patent maxillary antrostomy but purulence cycling between a retained natural maxillary ostium anteriorly and a separate surgical opening posteriorly. What is the best revision principle?",
        [
            "Enlarge only the posterior opening and leave the natural ostium separate",
            "Treat indefinitely with systemic steroids because the problem is inflammatory only",
            "Connect the natural ostium to the surgical antrostomy and eliminate the recirculation pathway while preserving healthy mucosa",
            "Perform a Draf III because maxillary recirculation is a frontal-sinus disorder",
        ], 2,
        "Maxillary recirculation occurs when mucus exits the natural ostium and is drawn back into a separate accessory or surgical opening. Revision should correct the defined anatomic failure by unifying the openings rather than simply enlarging the wrong aperture or escalating unrelated therapy.",
        [
            "A second larger posterior opening can preserve the same recirculation mechanism if the natural ostium remains separate.",
            "Steroids do not correct a mechanically separated drainage pathway causing mucus recirculation.",
            "Correct. Revision surgery should fix a specific failure mechanism rather than repeat nonspecific sinus enlargement.",
            "A Draf III addresses severe frontal outflow disease, not isolated maxillary recirculation.",
        ],
        "Revision ESS should be hypothesis-driven: identify the failure mechanism, then correct that mechanism and nothing more than necessary.",
        "Which endoscopic landmark helps ensure that the opening being incorporated is the true natural maxillary ostium rather than an accessory ostium?",
        "OR_prep",
    ),

    _q(
        "v206_rhi_crswnp_snr", "CRSwNP", "senior_decision",
        "A patient with severe CRSwNP, asthma, and prior adequate ESS remains highly symptomatic despite high-volume topical steroid irrigations and has required repeated systemic-steroid bursts. The sinuses are widely patent but polyps recur rapidly. What is the best senior-level next step?",
        [
            "Repeat the identical surgery immediately because any polyp recurrence proves insufficient tissue removal",
            "Assess type-2 inflammatory burden, adherence, AERD history and biologic eligibility, then use phenotype-directed escalation rather than reflexive reoperation",
            "Stop topical therapy because surgery should have made medication unnecessary",
            "Use long-term broad-spectrum antibiotics as the primary treatment for eosinophilic recurrent polyposis",
        ], 1,
        "When surgery has already established access and the dominant residual problem is recurrent type-2 inflammation, the next decision should target that biology. Biologics, AERD-directed therapy when relevant, and continued topical treatment may be more rational than repeating anatomically adequate surgery without a defined structural target.",
        [
            "More surgery without an anatomic failure target may add morbidity without controlling the inflammatory endotype driving recurrence.",
            "Correct. Senior management distinguishes failure of anatomy from failure of inflammatory control.",
            "ESS improves topical access; it does not eliminate the need for long-term anti-inflammatory treatment in severe polyp disease.",
            "Recurrent eosinophilic polyposis is not primarily a chronic bacterial-infection problem requiring indefinite antibiotics.",
        ],
        "In recurrent CRSwNP after adequate ESS, ask whether the failure is structural or biologic before scheduling another operation.",
        "How would NSAID-triggered respiratory reactions change the discussion of aspirin desensitization versus biologic therapy?",
        "boards",
    ),

    _q(
        "v206_rhi_csf_snr", "Endoscopic CSF Leak Repair / Nasoseptal Flap", "senior_decision",
        "During an expanded endonasal approach, a large high-flow skull-base defect is created. The patient previously had a posterior septectomy that sacrificed the ipsilateral nasoseptal flap pedicle. What is the best reconstructive principle?",
        [
            "Close with nasal packing alone because no vascularized option remains",
            "Use a single free mucosal graft regardless of defect size and flow",
            "Abandon endonasal reconstruction and leave a controlled CSF fistula",
            "Plan an alternative multilayer reconstruction using available vascularized regional tissue or other appropriate flap strategy based on defect location and prior surgery",
        ], 3,
        "High-flow reconstruction should be planned before exposure whenever possible, including review of prior septal surgery and tumor involvement that may eliminate the standard nasoseptal flap. When its pedicle is unavailable, the principle remains robust multilayer closure with the best viable vascularized option suited to the defect.",
        [
            "Packing does not replace an anatomic watertight reconstruction for a large high-flow skull-base defect.",
            "A small free graft alone may be inadequate when defect size and CSF flow demand vascularized coverage.",
            "An intentional persistent CSF fistula creates meningitis and wound-healing risk rather than solving the reconstruction problem.",
            "Correct. The flap name can change; the reconstructive principle of viable multilayer coverage does not.",
        ],
        "Before expanded skull-base surgery, reconstructive planning begins before the defect exists: know whether your intended pedicle is still available.",
        "Which alternative intranasal or regional vascularized flaps can be considered when a classic nasoseptal flap is unavailable?",
        "OR_prep",
    ),

    _q(
        "v206_rhi_max_app", "Endoscopic Maxillary Antrostomy", "application",
        "During uncinectomy, the surgeon sees an opening into the maxillary sinus posterior to the expected natural ostium. The natural ostium has not yet been clearly identified. What is the safest next step?",
        [
            "Assume the first opening is natural and enlarge it posteriorly only",
            "Identify the natural maxillary ostium using the uncinate/infundibular anatomy and incorporate it into a single antrostomy before enlarging the opening",
            "Extend superiorly into the orbit to improve visualization",
            "Stop because accessory ostia make maxillary antrostomy contraindicated",
        ], 1,
        "Accessory maxillary ostia are common and can be mistaken for the natural drainage pathway. A safe functional antrostomy identifies the true natural ostium and connects it to the surgical opening, avoiding persistent mucus recirculation and unnecessary orbital risk.",
        [
            "Enlarging an accessory opening while leaving the natural ostium separate can create or perpetuate recirculation.",
            "Correct. The natural ostium must be identified before the antrostomy is considered complete.",
            "Superior dissection without clear anatomy risks the orbital floor and does not help define the physiologic drainage pathway safely.",
            "An accessory ostium is an anatomic clue to interpret, not a contraindication to indicated surgery.",
        ],
        "The goal of maxillary antrostomy is not simply to make a hole; it is to incorporate the sinus's true drainage pathway.",
        "How can a Haller cell or lateralized uncinate distort the expected location of the infundibulum and natural ostium?",
        "OR_prep",
    ),
    _q(
        "v206_rhi_max_snr", "Endoscopic Maxillary Antrostomy", "senior_decision",
        "During revision maxillary surgery, the orbital floor is unusually low and the natural ostium is scarred. As the superior edge of the antrostomy is widened, orbital fat suddenly prolapses into the field. What is the best immediate response?",
        [
            "Stop powered instrumentation, protect the orbit, assess for extraocular injury or bleeding, re-establish landmarks, and limit further dissection according to the injury and surgical need",
            "Continue microdebrider use because orbital fat is expected during a complete antrostomy",
            "Pull the prolapsed fat to improve exposure",
            "Convert automatically to an external maxillectomy",
        ], 0,
        "Orbital fat exposure signals violation of the orbital boundary. The immediate priority is preventing conversion of a small defect into extraocular-muscle, globe, or orbital-hematoma injury by stopping the provoking maneuver, protecting tissue, and reassessing anatomy and function before deciding whether surgery can safely continue.",
        [
            "Correct. Recognition and damage limitation come before completing the planned antrostomy.",
            "Powered instrumentation near prolapsed orbital contents can rapidly injure extraocular muscle or other orbital structures.",
            "Traction on orbital fat can transmit force to orbital contents and worsen injury.",
            "An external approach is not automatically required for a limited orbital boundary violation; the response depends on the actual injury and remaining indication.",
        ],
        "Unexpected orbital fat is a stop sign, not a landmark to debride.",
        "What postoperative eye findings would mandate urgent ophthalmologic assessment for orbital hematoma or muscle injury?",
        "overnight_call",
    ),

    _q(
        "v206_rhi_eth_app", "Ethmoidectomy", "application",
        "Preoperative CT shows a markedly asymmetric low-lying right fovea ethmoidalis with a deep lateral lamella. How should this change the right ethmoid dissection?",
        [
            "It should not; skull-base height is sufficiently constant that CT asymmetry can be ignored",
            "Begin superior dissection blindly because the low skull base is easier to reach",
            "Use the contralateral skull-base height as the right-sided depth target",
            "Plan a more conservative, landmark-driven superior dissection and maintain deliberate awareness of the low skull base/lateral lamella throughout the case",
        ], 3,
        "Ethmoid roof height and Keros/lateral-lamella anatomy can be asymmetric. Preoperative recognition of a low skull base narrows the safe vertical corridor and should change the operative mental map; the contralateral side is not a reliable depth template.",
        [
            "Skull-base asymmetry is clinically important precisely because assuming symmetry can cause intracranial injury.",
            "Blind superior dissection increases risk where the vertical safety margin is already reduced.",
            "Using the opposite side as a depth target ignores patient-specific asymmetry demonstrated on the CT.",
            "Correct. CT review must alter the dissection strategy when the skull-base corridor is unusually narrow.",
        ],
        "The safest ethmoidectomy begins on the CT: know where the skull base is low before your instrument discovers it.",
        "Which relationship of the anterior ethmoid artery to the skull base becomes especially important in a low or dehiscent ethmoid roof?",
        "OR_prep",
    ),
    _q(
        "v206_rhi_eth_snr", "Ethmoidectomy", "senior_decision",
        "During ethmoidectomy, brisk arterial bleeding occurs high in the anterior ethmoid region and the vessel appears to retract laterally toward the orbit. What is the most important senior-level concern?",
        [
            "This is harmless mucosal bleeding and surgery should continue without orbital assessment",
            "An injured anterior ethmoid artery can retract into the orbit and produce a rapidly vision-threatening orbital hematoma, so bleeding control and immediate orbital/visual assessment take priority",
            "The only relevant complication is postoperative septal perforation",
            "Pack the sphenoid sinus because the anterior ethmoid artery arises there",
        ], 1,
        "Anterior ethmoid artery injury is dangerous not only because of blood loss but because the divided vessel can retract into the orbit, causing retrobulbar hemorrhage and optic-nerve ischemia. Prompt control, assessment of the orbit and vision, and decompression if an orbital compartment syndrome develops are time-critical.",
        [
            "High ethmoid arterial bleeding near the orbit can become a vision emergency and cannot be treated as routine mucosal oozing.",
            "Correct. The escalation threshold is orbital pressure or visual compromise, not simply the volume of intranasal blood.",
            "Septal perforation is unrelated to the immediate danger created by anterior ethmoid arterial injury.",
            "The anterior ethmoid artery traverses the anterior ethmoid roof/orbit relationship, not the sphenoid sinus.",
        ],
        "An anterior ethmoid artery injury can turn into an orbital-compartment emergency after the vessel retracts out of sight.",
        "Which bedside findings should trigger immediate lateral canthotomy/cantholysis or other orbital decompression rather than observation?",
        "overnight_call",
    ),
]


def apply_learning_ladders_v206(challenges, id_factory):
    by_id = {q.get("id"): q for q in challenges if q.get("id")}
    reviewed_foundations = 0
    for qid in REVIEWED_FOUNDATION_IDS_V206:
        q = by_id.get(qid)
        if q is None:
            raise RuntimeError(f"v20.6: reviewed foundation missing from live registry: {qid}")
        if q.get("domain") != DOMAIN:
            raise RuntimeError(f"v20.6: foundation domain mismatch: {qid}")
        q["learning_stage"] = "foundation"
        q["ladder_reviewed"] = True
        reviewed_foundations += 1

    reused_applications = 0
    for qid, topic in REUSED_APPLICATION_IDS_V206.items():
        q = by_id.get(qid)
        if q is None:
            raise RuntimeError(f"v20.6: reused application missing from live registry: {qid}")
        if q.get("domain") != DOMAIN or q.get("topic") != topic:
            raise RuntimeError(f"v20.6: reused application mapping mismatch: {qid}")
        q["learning_stage"] = "application"
        q["ladder_reviewed"] = True
        reused_applications += 1

    existing = {q.get("id") for q in challenges if q.get("id")}
    added = 0
    for source in VIGNETTES_V206:
        if source["id"] in existing:
            continue
        q = dict(source)
        q["concept_id"] = id_factory(q["domain"], q["topic"])
        challenges.append(q)
        existing.add(q["id"])
        added += 1

    return {
        "reviewed_foundations": reviewed_foundations,
        "reused_applications": reused_applications,
        "added_questions": added,
        "topics": sorted({q["topic"] for q in VIGNETTES_V206}),
    }
