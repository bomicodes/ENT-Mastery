"""v34.0 — clinically separate first-bite syndrome from Frey syndrome.

Bounded Concept Hub rebuild. These are both gustatory complications seen around parotid/
upper-neck surgery, but they test different anatomy, symptoms, workup, and botulinum-toxin
technique. The patch intentionally keeps them as distinct cards.
"""

import re


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _append_unique(module, key, text):
    current = str(module.get(key) or "").strip()
    module[key] = (current + " " + text).strip() if current else text


def apply_salivary_gustatory_syndromes_v340(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []

    for _domain, modules in deep_modules.items():
        for module in modules or []:
            topic = _norm(module.get("topic"))

            if topic == "first bite syndrome":
                module["definition"] = (
                    "A gustatory pain syndrome in which the first bite after a period of rest triggers sudden, "
                    "usually unilateral severe parotid/preauricular pain that rapidly lessens with subsequent bites. "
                    "Sweating and flushing are not the defining phenotype."
                )
                module["diagnose"] = (
                    "DIAGNOSIS IS PATTERN + CONTEXT. Ask whether pain is maximal with the first bite, fades as the meal "
                    "continues, and returns after a pause. In the classic postoperative setting, review deep-lobe parotid, "
                    "parapharyngeal-space, carotid-space, infratemporal-fossa, upper-neck, or skull-base surgery that could "
                    "have interrupted cervical sympathetic fibers or the sympathetic plexus around the external carotid artery. "
                    "Examine the parotid bed, deep neck and cranial nerves, and look for Horner findings, but Horner syndrome is "
                    "not required. A spontaneous, preoperative, delayed unexplained, progressive, or otherwise atypical first-bite "
                    "syndrome is a RED FLAG rather than an idiopathic diagnosis: obtain contrast-enhanced imaging of the deep "
                    "parotid/parapharyngeal-carotid space and skull base to exclude an occult tumor tracking near sympathetic pathways."
                )
                module["mechanism"] = (
                    "The leading model is loss of sympathetic input to the parotid after injury to cervical sympathetic/ECA "
                    "plexus fibers, producing denervation hypersensitivity and painful unopposed parasympathetic-driven "
                    "myoepithelial contraction at the onset of salivation. This is fundamentally different from Frey syndrome, "
                    "which is aberrant parasympathetic reinnervation of skin sweat glands and vessels."
                )
                module["manage"] = (
                    "Start with expectation-setting: postoperative first-bite syndrome may diminish spontaneously, and the evidence "
                    "base for medication is limited. Neuropathic-pain medications or other conservative measures can be tried when "
                    "symptoms warrant, but persistent meal-limiting pain should prompt consideration of ultrasound-guided INTRAPAROTID "
                    "botulinum toxin A. Inject the affected gland rather than the overlying skin; benefit can be incomplete or temporary "
                    "and repeat treatment may be needed. Do not let symptom treatment substitute for tumor evaluation when first-bite "
                    "syndrome arises without an explanatory operation."
                )
                module["teach"] = (
                    "BOARDS/CHIEF SPLIT: first-bite syndrome = PAIN on the first bite, sympathetic denervation physiology, and "
                    "intraparotid botulinum toxin when treatment is needed. Spontaneous first-bite syndrome can be a presenting sign "
                    "of deep parotid/parapharyngeal or skull-base disease and deserves an anatomic explanation."
                )
                module["tags"] = list(dict.fromkeys(list(module.get("tags") or []) + [
                    "first bite pain", "parapharyngeal space", "sympathetic denervation", "intraparotid botulinum toxin", "occult tumor red flag"
                ]))
                module["source_basis"] = list(dict.fromkeys(list(module.get("source_basis") or []) + [
                    "Cummings Otolaryngology, 7e — salivary/parotid and parapharyngeal-space anatomy and postoperative-complication framework",
                    "K.J. Lee's Essential Otolaryngology, 12e — parotid and deep-neck surgical anatomy/complication framework",
                    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — salivary/parotid surgical complication framework",
                    "Ang et al., J Laryngol Otol 2025 — systematic review of first-bite syndrome management; observation and repeated botulinum toxin are the best-supported contemporary strategies",
                    "Shaikh et al., Gland Surgery 2022 — systematic review of intraparotid botulinum toxin A for first-bite syndrome",
                    "Linkov et al., Laryngoscope 2011 / related case literature — spontaneous first-bite syndrome may present with parapharyngeal malignancy"
                ]))
                module["salivary_gustatory_syndromes_v340"] = True
                patched.append(module.get("topic"))

            elif topic == "frey syndrome":
                module["definition"] = (
                    "Auriculotemporal (Frey) syndrome is meal-triggered sweating, flushing, warmth, or erythema over the "
                    "preauricular/temporal/parotid skin, classically appearing months after parotid surgery or trauma. Pain with "
                    "the first bite is not the defining feature."
                )
                module["diagnose"] = (
                    "A classic postoperative history is usually diagnostic. If objective confirmation or treatment mapping is useful, "
                    "perform the Minor iodine-starch test: iodine is applied to the skin, starch is added after drying, and a gustatory "
                    "stimulus maps sweating as a dark color change. Routine tumor imaging is not required for otherwise typical "
                    "post-parotidectomy Frey syndrome; image only when the history/exam raises a separate concern for recurrence or another lesion."
                )
                module["mechanism"] = (
                    "After auriculotemporal/postganglionic parasympathetic fibers are disrupted during parotid surgery or trauma, regenerating "
                    "secretomotor fibers can be misdirected to denervated cutaneous sweat glands and superficial vessels. Gustatory stimulation "
                    "therefore produces sweating/flushing instead of only salivation. This is aberrant PARASYMPATHETIC reinnervation, not the "
                    "sympathetic-denervation pain mechanism taught in first-bite syndrome."
                )
                module["manage"] = (
                    "Treat the patient, not a positive starch test. Mild/nonbothersome symptoms can be observed; topical antiperspirant or "
                    "anticholinergic therapy may help selected patients. For bothersome disease, map the symptomatic field and inject botulinum "
                    "toxin A INTRADERMALLY in a grid over the involved skin. Response is typically strong but recurrence can require repeat injections. "
                    "At the index parotid operation, an interposition barrier such as SMAS/temporoparietal fascia, SCM, or acellular dermal material "
                    "may reduce Frey syndrome in selected reconstructions, but prevention must remain subordinate to oncologic margins, facial-nerve "
                    "safety, and reconstructive needs."
                )
                module["teach"] = (
                    "BOARDS/CHIEF SPLIT: Frey = gustatory SWEATING/FLUSHING, aberrant parasympathetic reinnervation, Minor test for mapping, and "
                    "intradermal botulinum toxin. First-bite syndrome = gustatory PAIN that is maximal on the first bite, a sympathetic-denervation "
                    "phenotype, and botulinum toxin delivered into the parotid gland rather than the skin."
                )
                module["tags"] = list(dict.fromkeys(list(module.get("tags") or []) + [
                    "gustatory sweating", "auriculotemporal syndrome", "Minor iodine starch test", "intradermal botulinum toxin", "parotidectomy complication"
                ]))
                module["source_basis"] = list(dict.fromkeys(list(module.get("source_basis") or []) + [
                    "Cummings Otolaryngology, 7e — parotid surgical anatomy and post-parotidectomy complication framework",
                    "K.J. Lee's Essential Otolaryngology, 12e — parotidectomy complication and salivary anatomy framework",
                    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — parotidectomy complication framework",
                    "Xie et al., Cancer Medicine 2015 — systematic review/meta-analysis supporting botulinum toxin A for symptomatic Frey syndrome",
                    "Liu et al., Oncology Letters 2013 — systematic review/meta-analysis of SCM interposition for Frey prevention; preventive barrier evidence is technique-dependent"
                ]))
                module["salivary_gustatory_syndromes_v340"] = True
                patched.append(module.get("topic"))

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
