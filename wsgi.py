import re
import data
from curveballs_v123 import ORIGINAL_V11_CURVEBALLS_V123
from vignettes_v124 import VIGNETTES_V124
from recognize_stage_v127 import apply_recognize_blind_reveal_v127

# ENT Mastery v12.4 production runtime integration.
# Build adaptive items from the final topic registry while preserving the schema
# expected by Daily Path.
_original_get_adaptive_items_v120 = data.get_adaptive_items_v120

def _get_adaptive_items_v123():
    items = _original_get_adaptive_items_v120()
    stage_level = {"recognize": 1, "localize": 2, "workup": 3, "manage": 4, "operate": 5, "teach": 6}
    for item in items:
        item.setdefault("level", stage_level.get(item.get("stage"), 1))
        item.setdefault("tags", sorted(set(re.findall(r"[a-z0-9]+", ((item.get("domain") or "") + " " + (item.get("topic") or "")).lower()))))
    apply_recognize_blind_reveal_v127(items)
    return items

data.get_adaptive_items_v120 = _get_adaptive_items_v123

# Static swallow-study frames are intentionally removed from the Interpretation
# Atlas. VFSS/MBS and FEES are dynamic studies and cannot be meaningfully trained
# with the site's 2-D still-frame schematics. Swallowing concepts/cases remain.
data.INTERPRETATION_LABS.pop("swallowing-imaging", None)
for _name in ("LAB_PARENT_TOPIC_V98", "LAB_PARENT_CONCEPT_V98", "_GENERIC_FOLLOW_BY_LAB_V91", "INTERPRETATION_V118_COLLAPSED"):
    _mapping = getattr(data, _name, None)
    if isinstance(_mapping, dict):
        _mapping.pop("swallowing-imaging", None)

# Complete the original flagship vignette set with a true attending-style
# escalation step. The one already-authored curveball is preserved.
for _bank_name in ("CLINICAL_CHALLENGES_V11", "CLINICAL_CHALLENGES_V112", "CLINICAL_CHALLENGES_V115", "CLINICAL_CHALLENGES_V116", "CLINICAL_CHALLENGES_V119"):
    _bank = getattr(data, _bank_name, None)
    if not isinstance(_bank, list):
        continue
    for _q in _bank:
        _qid = _q.get("id")
        if _qid in ORIGINAL_V11_CURVEBALLS_V123 and not (_q.get("curveball") or "").strip():
            _q["curveball"] = ORIGINAL_V11_CURVEBALLS_V123[_qid]

# v12.4: weight vignette expansion toward the two domains with the lowest
# coverage relative to topic count: Otology / Neurotology and Pediatric ENT.
# Assign concept IDs from the final topic registry, then append only new IDs so
# repeated process imports cannot duplicate questions.
_existing_vignette_ids = {q.get("id") for q in data.CLINICAL_CHALLENGES_V119}
for _q_src in VIGNETTES_V124:
    if _q_src.get("id") in _existing_vignette_ids:
        continue
    _q = dict(_q_src)
    _q["concept_id"] = data._v6_item_id(_q["domain"], _q["topic"])
    data.CLINICAL_CHALLENGES_V119.append(_q)
    _existing_vignette_ids.add(_q["id"])
# Keep the live direct-lookup index synchronized with the expanded list.
data.CLINICAL_CHALLENGE_BY_ID_V119 = {q["id"]: q for q in data.CLINICAL_CHALLENGES_V119}

# v12.6: close targeted Interpretation Atlas depth gaps without forking the
# generated registry. These additions mutate the final live INTERPRETATION_LABS
# object before Flask imports it, use stable IDs, and are idempotent.
def _lab_text_v126(slug, lab):
    bits = [slug, lab.get("title", ""), lab.get("subtitle", ""), " ".join(lab.get("framework") or [])]
    for c in lab.get("cases") or []:
        bits.extend(str(c.get(k, "") or "") for k in
                    ("id", "prompt", "answer", "why", "reason_prompt", "reason_answer", "follow", "teach_prompt", "teach_answer"))
    return " ".join(bits).lower()


def _find_lab_v126(preferred_terms=(), evidence_terms=(), expected_size=None):
    scored = []
    for slug, lab in (data.INTERPRETATION_LABS or {}).items():
        text = _lab_text_v126(slug, lab)
        score = 0
        for term in preferred_terms:
            if term.lower() in (slug + " " + str(lab.get("title", ""))).lower():
                score += 8
            elif term.lower() in text:
                score += 2
        for term in evidence_terms:
            if term.lower() in text:
                score += 5
        if expected_size is not None and len(lab.get("cases") or []) == expected_size:
            score += 3
        if score:
            scored.append((score, slug, lab))
    if not scored:
        return None, None
    scored.sort(key=lambda x: (-x[0], x[1]))
    return scored[0][1], scored[0][2]


def _append_unique_cases_v126(lab, cases, before_terms=()):
    if not lab:
        return []
    bank = lab.setdefault("cases", [])
    existing = {c.get("id") for c in bank}
    new_cases = [dict(c) for c in cases if c.get("id") not in existing]
    if not new_cases:
        return []
    insert_at = len(bank)
    if before_terms:
        for i, c in enumerate(bank):
            hay = " ".join(str(c.get(k, "") or "") for k in
                           ("prompt", "answer", "why", "reason_prompt", "reason_answer", "follow", "teach_prompt", "teach_answer")).lower()
            if any(term.lower() in hay for term in before_terms):
                insert_at = i
                break
    bank[insert_at:insert_at] = new_cases
    return [c["id"] for c in new_cases]


_audio_slug_v126, _audio_lab_v126 = _find_lab_v126(
    preferred_terms=("audiogram", "audiology", "hearing"),
    evidence_terms=("carhart", "tympan", "otoacoustic", "auditory neuropathy"),
    expected_size=24,
)
_audio_added_v126 = _append_unique_cases_v126(_audio_lab_v126, [
    {
        "id": "audio-v126-masking-cross-hearing",
        "concept_id": "audiology-masking-cross-hearing",
        "variant_type": "interpret",
        "level": 3,
        "prompt": "A patient has a large asymmetric air-conduction threshold difference. Before accepting the poorer-ear threshold as real, what technical problem must you consider, and what should you do next?",
        "answer": "Consider cross-hearing by the non-test ear. If the test-ear signal can reach the opposite cochlea at an audible level after interaural attenuation, obtain masked thresholds before calling the asymmetry true. Air-conduction interaural attenuation depends on the transducer; bone-conduction interaural attenuation is effectively 0 dB, so unmasked bone thresholds do not establish which cochlea responded.",
        "why": "An apparently severe unilateral loss can be a shadow curve from the better cochlea. Masking is not an optional refinement when cross-hearing is possible; it is what makes the threshold ear-specific.",
        "reason_prompt": "Why can you not use one universal interaural-attenuation number for every air-conduction test, and why is bone conduction different?",
        "reason_answer": "Interaural attenuation varies with the transducer and patient, with insert earphones generally providing more attenuation than supra-aural phones. Bone vibration reaches both cochleae with essentially no clinically useful interaural attenuation, so masking is often required to assign a bone threshold to one ear.",
        "follow": "On boards, separate the questions: first ask whether cross-hearing is possible; then decide whether masking can create an ear-specific threshold without overmasking.",
        "teach_prompt": "Teach a junior the one-sentence reason masking exists in pure-tone audiometry.",
        "teach_answer": "Masking keeps the non-test cochlea busy so the response can be attributed to the ear you are actually trying to measure, rather than to a crossed-over signal heard by the better ear."
    },
    {
        "id": "audio-v126-masking-dilemma",
        "concept_id": "audiology-masking-dilemma",
        "variant_type": "interpret",
        "level": 4,
        "prompt": "A patient with large bilateral conductive components needs masked bone thresholds, but increasing masking noise in the non-test ear reaches the test cochlea before a stable masking plateau can be established. What is happening?",
        "answer": "This is the masking dilemma: there is no usable masking plateau because the amount of masking needed to prevent cross-hearing approaches or exceeds the level that itself crosses over and overmasks the test ear. It is classically problematic with large bilateral air-bone gaps.",
        "why": "The key error is to force a numeric masked threshold when the test conditions cannot isolate one cochlea. Recognizing an indeterminate masked threshold is better than reporting false precision.",
        "reason_prompt": "What practical strategies can reduce the problem, and what should you avoid claiming if no plateau exists?",
        "reason_answer": "Use a transducer with greater interaural attenuation when appropriate, optimize masking with accepted plateau methods, and integrate immittance and objective tests when needed. If a true plateau cannot be obtained, document the limitation rather than inventing an ear-specific bone threshold.",
        "follow": "The dilemma is a physics/testing limitation, not proof that the underlying hearing loss is functional.",
        "teach_prompt": "Contrast undermasking, adequate masking, and overmasking in 20 seconds.",
        "teach_answer": "Undermasking lets the non-test ear answer; adequate masking suppresses that ear while leaving the test cochlea unaffected; overmasking is loud enough to cross back to the test cochlea and contaminate the measurement."
    },
    {
        "id": "audio-v126-stenger-functional",
        "concept_id": "audiology-stenger-functional-hearing-loss",
        "variant_type": "interpret",
        "level": 4,
        "prompt": "A patient reports profound unilateral hearing loss, but behavioral responses are internally inconsistent. During a Stenger test, the same-frequency tone is presented to both ears, louder to the reported poorer ear and at an audible level to the better ear. The patient gives no response. Interpret this result.",
        "answer": "That is a positive Stenger response and supports a nonorganic/functional component to the claimed unilateral loss. With simultaneous identical tones, the percept is dominated by the louder presentation; a patient with true profound loss in the poorer ear should still hear and respond through the better ear, whereas withholding a response when the louder percept lateralizes to the claimed poorer ear raises concern that the behavioral threshold is not valid.",
        "why": "Stenger testing is a classic oral-boards discriminator for unilateral or markedly asymmetric functional hearing loss, but it tests response validity rather than motive.",
        "reason_prompt": "Does a positive Stenger prove malingering, and how would you corroborate the true auditory function?",
        "reason_answer": "No. It supports an invalid or exaggerated behavioral response pattern but does not establish intent or cause. Recheck behavioral consistency and use objective physiologic data such as OAEs and/or ABR when clinically appropriate to estimate peripheral and neural auditory function.",
        "follow": "Use neutral language: functional/nonorganic or invalid behavioral thresholds. Do not equate the test result with deliberate deception.",
        "teach_prompt": "Explain the Stenger principle without memorizing the name of the test.",
        "teach_answer": "Two simultaneous tones of the same frequency are perceived as one sound, biased toward the ear receiving the louder tone; that perceptual rule lets you test whether a claimed unilateral loss behaves physiologically."
    }
])

_vest_slug_v126, _vest_lab_v126 = _find_lab_v126(
    preferred_terms=("vestibular", "vestib"),
    evidence_terms=("caloric", "vhit", "vemp", "bppv"),
    expected_size=18,
)
_vest_added_v126 = _append_unique_cases_v126(_vest_lab_v126, [
    {
        "id": "vest-v126-bilateral-vestibulopathy",
        "concept_id": "vestibular-bilateral-vestibulopathy",
        "variant_type": "interpret",
        "level": 4,
        "prompt": "A patient develops chronic gait unsteadiness after vestibulotoxic exposure, reports oscillopsia while walking, and is much worse in darkness and on uneven ground. vHIT shows horizontal VOR gain below 0.6 bilaterally with corrective saccades; bithermal calorics are markedly reduced on both sides. What syndrome does this pattern establish?",
        "answer": "Bilateral vestibulopathy. The clinical pattern is a chronic vestibular syndrome with motion-induced visual blurring/oscillopsia and imbalance that worsens when visual or somatosensory substitution is reduced, combined with objectively reduced angular VOR function on both sides.",
        "why": "This is not a 'which ear is weak?' problem. The core diagnostic move is recognizing bilateral loss, where relative asymmetry can be small even though total vestibular function is profoundly reduced.",
        "reason_prompt": "What objective tests can satisfy the bilateral VOR requirement, and why can a normal-looking unilateral-weakness calculation be misleading?",
        "reason_answer": "Bilateral vestibulopathy can be documented with bilaterally abnormal vHIT, severely reduced bithermal caloric responses on each side, and/or appropriately abnormal rotational-chair VOR. A unilateral-weakness percentage compares the ears to each other, so two similarly weak ears can produce little asymmetry despite major bilateral hypofunction.",
        "follow": "Ask about oscillopsia, falls, darkness/uneven-ground dependence, ototoxic drugs, meningitis, bilateral Meniere disease, neuropathy/cerebellar features, and other causes of bilateral loss.",
        "teach_prompt": "Give the board-level distinction between unilateral vestibular hypofunction and bilateral vestibulopathy.",
        "teach_answer": "Unilateral disease is usually a side-to-side asymmetry problem; bilateral vestibulopathy is a total-gain problem, producing deficient gaze stabilization and sensory dependence even when the two ears are similarly impaired."
    },
    {
        "id": "vest-v126-rotational-chair",
        "concept_id": "vestibular-rotational-chair-testing",
        "variant_type": "interpret",
        "level": 4,
        "prompt": "A young child cannot cooperate with vHIT and cannot tolerate caloric irrigation. You still need quantitative information about horizontal VOR function, particularly because bilateral vestibular loss is suspected. Which laboratory test is most useful, and what does it add?",
        "answer": "Rotational-chair testing is a strong next test. En-bloc whole-body rotation measures the horizontal VOR over low-to-middle stimulus frequencies and can demonstrate residual or bilaterally reduced vestibular function when calorics or vHIT are unavailable, poorly tolerated, or difficult to interpret.",
        "why": "Rotational chair fills a frequency and feasibility gap in the vestibular test battery. It is especially useful for bilateral hypofunction, but because both labyrinths are stimulated together it is generally less effective than monaural calorics for lateralizing a unilateral lesion.",
        "reason_prompt": "How do calorics, rotational chair, and vHIT differ conceptually by stimulus frequency and laterality?",
        "reason_answer": "Calorics probe very low-frequency horizontal-canal function one ear at a time; rotational chair probes low-to-middle-frequency whole-body VOR with both labyrinths stimulated; vHIT probes high-frequency, high-acceleration VOR and can quantify each canal/side. Discordance can therefore be physiologic rather than contradictory.",
        "follow": "Interpret chair gain, phase, and time constant against the laboratory's validated norms and the clinical question; do not use a single chair metric in isolation to lateralize unilateral disease.",
        "teach_prompt": "When should rotational chair come to mind on oral boards?",
        "teach_answer": "Think rotational chair when bilateral vestibular hypofunction is suspected or when calorics/vHIT cannot be performed reliably, especially in children or patients with anatomic, tolerance, or cooperation limitations."
    }
])

_mri_slug_v126, _mri_lab_v126 = _find_lab_v126(
    preferred_terms=("head", "neck", "imaging", "mri"),
    evidence_terms=("perineural", "parotid", "v3", "nasopharyn"),
)
_mri_added_v126 = _append_unique_cases_v126(_mri_lab_v126, [
    {
        "id": "hnimg-v126-mri-sequence-literacy",
        "concept_id": "head-neck-mri-sequence-literacy",
        "variant_type": "interpret",
        "level": 2,
        "prompt": "Before naming a lesion, orient yourself to the MRI sequence. Build the sequence map: what are T1, T2, STIR/fat-suppressed fluid-sensitive imaging, post-gadolinium T1 fat-sat, and DWI with ADC each trying to show you?",
        "answer": "T1 is anatomy-rich: fat is bright and simple fluid is relatively dark. T2 is fluid-sensitive: fluid and many edematous/pathologic tissues are bright. STIR suppresses fat and makes edema or fluid-rich abnormality conspicuous. Post-gadolinium T1 with fat suppression darkens background fat so true enhancement stands out. DWI must be interpreted with ADC: true restricted diffusion is bright on high-b-value DWI with corresponding low ADC rather than DWI brightness alone.",
        "why": "Sequence literacy prevents vignette pattern-matching. Perineural tumor spread, marrow replacement, abscess, hypercellular tumor, and keratin debris are recognized because of how tissue behaves on specific sequences, not because the stem tells you the diagnosis.",
        "reason_prompt": "Match the sequence to three ENT questions: suspected perineural spread, postoperative cholesteatoma, and a possible deep-neck abscess.",
        "reason_answer": "Perineural spread is best sought on contrast-enhanced T1 fat-suppressed imaging for abnormal nerve enhancement/enlargement and foraminal tracking. Cholesteatoma is characterized with diffusion-weighted imaging, particularly non-echo-planar DWI in temporal-bone practice. Purulent abscess contents often demonstrate true diffusion restriction, so confirm DWI hyperintensity with low ADC while also assessing rim enhancement and anatomy on the conventional sequences.",
        "follow": "For DWI, always ask 'what does the ADC map do?' to avoid mistaking T2 shine-through for true restriction. For enhancement, ask whether fat suppression is adequate so enhancing tumor is not hidden in bright skull-base or facial fat.",
        "teach_prompt": "Give a 20-second MRI sequence primer to a junior before showing a perineural-spread case.",
        "teach_answer": "T1 is your fat/anatomy map, T2 is your water map, fat-suppressed post-contrast T1 is your enhancement map, STIR is a fat-suppressed edema map, and DWI plus ADC is your restriction map. Identify the map before you interpret the lesion."
    }
], before_terms=("perineural", "parotid", "v3"))

_us_slug_v126, _us_lab_v126 = _find_lab_v126(
    preferred_terms=("thyroid", "ultrasound", "tirads", "ti-rads"),
    evidence_terms=("punctate", "taller-than-wide", "echogenic", "nodule"),
    expected_size=12,
)
_us_added_v126 = _append_unique_cases_v126(_us_lab_v126, [
    {
        "id": "thyus-v126-multinodular-biopsy-priority",
        "concept_id": "thyroid-ultrasound-multinodular-biopsy-priority",
        "variant_type": "interpret",
        "level": 4,
        "prompt": "A multinodular thyroid has three nodules that each meet ACR TI-RADS size criteria for FNA: a 3.0-cm TR3 nodule, a 1.6-cm TR4 nodule, and a 1.1-cm TR5 nodule. If you are selecting nodules for biopsy under ACR TI-RADS, which should be sampled first?",
        "answer": "Sample the TR5 and TR4 nodules, not simply the largest two. In a multinodular gland, ACR TI-RADS prioritizes the nodules with the highest TI-RADS grades that meet FNA criteria; when multiple nodules qualify, no more than two are generally sampled at one time.",
        "why": "The board trap is choosing the dominant or largest nodule. Size determines whether a nodule within a risk category crosses an action threshold, but relative size does not outrank sonographic risk category when deciding which qualifying nodules deserve biopsy.",
        "reason_prompt": "What are the ACR TI-RADS FNA size thresholds for TR3, TR4, and TR5, and does Doppler vascularity add TI-RADS points?",
        "reason_answer": "FNA thresholds are 2.5 cm for TR3, 1.5 cm for TR4, and 1.0 cm for TR5. Doppler vascularity is not an ACR TI-RADS scoring feature; scoring is based on composition, echogenicity, shape, margin, and echogenic foci.",
        "follow": "If two qualifying nodules have the same highest TI-RADS category, size can help prioritize within that category. Describe and follow other nodules according to the ACR framework rather than reflexively biopsying every nodule.",
        "teach_prompt": "Teach the one rule that prevents the common multinodular-goiter biopsy mistake.",
        "teach_answer": "Do not biopsy the biggest nodules just because they are biggest; first rank nodules by TI-RADS risk, then apply the category-specific size thresholds and biopsy the highest-risk qualifying nodules."
    }
])

# Lightweight runtime audit for future depth checks and regression debugging.
data.INTERPRETATION_DEPTH_V126_AUDIT = {
    "audiology": {"slug": _audio_slug_v126, "added": _audio_added_v126,
                  "bank_size": len((_audio_lab_v126 or {}).get("cases") or [])},
    "vestibular": {"slug": _vest_slug_v126, "added": _vest_added_v126,
                   "bank_size": len((_vest_lab_v126 or {}).get("cases") or [])},
    "mri_sequence_literacy": {"slug": _mri_slug_v126, "added": _mri_added_v126,
                              "bank_size": len((_mri_lab_v126 or {}).get("cases") or [])},
    "thyroid_ultrasound": {"slug": _us_slug_v126, "added": _us_added_v126,
                           "bank_size": len((_us_lab_v126 or {}).get("cases") or [])},
}

# Do not expose leftover historical atlas links on cards that explicitly require
# a modern surgical-anatomy source. Keep intentional Open Anatomy links.
for _entry in data.ANATOMY_ATLAS_V97:
    if _entry.get("anatomy_visual_status") == "modern_source_needed":
        _src = (_entry.get("image_source") or "").lower()
        if "openanatomy.org" not in _src:
            _entry["image_source"] = None
            _entry["image_credit"] = "Modern topic-specific source not yet curated"

# Import Flask only after the registries above are corrected so all routes see
# the final production state.
import app as _app_module

# Correct two stale aliases still referenced by app.py without rewriting the
# large application file in this hotfix.
_app_module.CLINICAL_CHALLENGES_V111 = data.CLINICAL_CHALLENGES_V119
_app_module.CURRICULUM_V5 = data.get_curriculum_v120()

app = _app_module.app
