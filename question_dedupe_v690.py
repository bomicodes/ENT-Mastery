"""v69.0: retire duplicate questions from the main banks.

A duplicate sweep (stem overlap, same answer within or across topics, then a reviewer read
of every candidate pair) found questions that repeat another one in different words, and
free-response concept checks whose text is identical to another (the "recognize" check reused
the "manage" text). The retired ones are removed from the live question lists, so practice
sets, search, Pasha and new flashcard picks show each question once; the kept question is the
better-written one (usually the vignette). Retired questions still open by direct link.
Map: retired id -> kept id.
"""

RETIRED_V690 = {
 "cc:cc-v112-mgt-general-ent-emergencies-cranial-nerve-examination-skull-base-localization": "challenge:v490-general-ent-1-91",
 "cc:cc-v112-mgt-general-ent-emergencies-lemierre-syndrome": "challenge:v490-general-ent-1-6",
 "cc:cc-v112-mgt-head-neck-oncology-head-neck-cancer-surveillance-second-primaries": "challenge:v490-head-neck-2-50",
 "cc:cc-v112-mgt-head-neck-oncology-sinonasal-malignancies": "challenge:v490-head-neck-2-53",
 "cc:cc-v112-mgt-laryngology-voice-swallowing-arytenoid-adduction-reinnervation": "challenge:v138_lar_02",
 "cc:cc-v112-mgt-otology-neurotology-lateral-skull-base-tumor-framework": "challenge:v490-otology-1-23",
 "cc:cc-v112-mgt-otology-neurotology-petrous-apex-lesions": "challenge:v175_oto_petrous_app",
 "cc:cc-v112-mgt-pediatric-otolaryngology-pediatric-osa-adenotonsillar-disease": "challenge:v490-pediatric-1-5",
 "cc:cc-v112-mgt-pediatric-otolaryngology-pediatric-vestibular-disorders": "challenge:v490-pediatric-2-50",
 "cc:cc-v112-mgt-rhinology-allergy-skull-base-immunodeficiency-associated-chronic-rhinosinusitis": "challenge:v490-rhinology-2-94",
 "cc:cc-v112-mgt-sleep-surgery-positional-osa": "challenge:v11_sleep_04",
 "cc:cc-v112-mgt-thyroid-parathyroid-salivary-first-bite-syndrome": "challenge:v490-thyroid-2-6",
 "cc:cc-v112-rec-facial-plastics-trauma-aesthetic-facial-analysis": "cc:cc-v112-mgt-facial-plastics-trauma-aesthetic-facial-analysis",
 "cc:cc-v112-rec-facial-plastics-trauma-auricular-reconstruction": "cc:cc-v112-mgt-facial-plastics-trauma-auricular-reconstruction",
 "cc:cc-v112-rec-facial-plastics-trauma-bilobed-flap": "cc:cc-v112-mgt-facial-plastics-trauma-bilobed-flap",
 "cc:cc-v112-rec-facial-plastics-trauma-dynamic-facial-reanimation": "cc:cc-v112-rec-facial-plastics-trauma-facial-nerve-reanimation",
 "cc:cc-v112-rec-facial-plastics-trauma-frontal-sinus-fracture-decision-model": "cc:cc-v112-rec-facial-plastics-trauma-frontal-sinus-fracture",
 "cc:cc-v112-rec-facial-plastics-trauma-hair-restoration-fundamentals": "cc:cc-v112-mgt-facial-plastics-trauma-hair-restoration-fundamentals",
 "cc:cc-v112-rec-facial-plastics-trauma-mohs-defect-reconstruction": "cc:cc-v112-mgt-facial-plastics-trauma-mohs-defect-reconstruction",
 "cc:cc-v112-rec-facial-plastics-trauma-noe-fracture-mechanics": "cc:cc-v112-rec-facial-plastics-trauma-noe-fracture",
 "cc:cc-v112-rec-facial-plastics-trauma-periocular-reconstruction": "cc:cc-v112-mgt-facial-plastics-trauma-periocular-reconstruction",
 "cc:cc-v112-rec-facial-plastics-trauma-static-facial-reanimation": "cc:cc-v112-rec-facial-plastics-trauma-facial-nerve-reanimation",
 "cc:cc-v112-rec-head-neck-oncology-radiation-therapy-principles-for-head-neck-surgeons": "cc:cc-v112-mgt-head-neck-oncology-radiation-therapy-principles-for-head-neck-surgeons",
 "cc:cc-v112-rec-head-neck-oncology-salvage-surgery-after-radiation-chemoradiation": "cc:cc-v112-mgt-head-neck-oncology-salvage-surgery-after-radiation-chemoradiation",
 "cc:cc-v112-rec-laryngology-voice-swallowing-leukoplakia-laryngeal-dysplasia": "cc:cc-v112-mgt-laryngology-voice-swallowing-leukoplakia-laryngeal-dysplasia",
 "cc:cc-v112-rec-otology-neurotology-autoimmune-inner-ear-disease": "cc:cc-v112-mgt-otology-neurotology-autoimmune-inner-ear-disease",
 "cc:cc-v112-rec-otology-neurotology-bppv": "cc:cc-v112-mgt-otology-neurotology-bppv",
 "cc:cc-v112-rec-otology-neurotology-m-ni-re-disease": "cc:cc-v112-mgt-otology-neurotology-m-ni-re-disease",
 "cc:cc-v112-rec-otology-neurotology-vestibular-neuritis": "cc:cc-v112-mgt-otology-neurotology-vestibular-neuritis",
 "cc:cc-v112-rec-pediatric-otolaryngology-congenital-hearing-loss-genetics": "cc:cc-v112-mgt-pediatric-otolaryngology-congenital-hearing-loss-genetics",
 "cc:cc-v112-rec-pediatric-otolaryngology-microtia-aural-atresia": "cc:cc-v112-mgt-pediatric-otolaryngology-microtia-aural-atresia",
 "cc:cc-v112-rec-rhinology-allergy-skull-base-csf-rhinorrhea": "cc:cc-v112-mgt-rhinology-allergy-skull-base-csf-rhinorrhea",
 "cc:cc-v112-rec-rhinology-allergy-skull-base-nasal-anatomy-for-endoscopy": "cc:cc-v112-mgt-rhinology-allergy-skull-base-nasal-anatomy-for-endoscopy",
 "cc:cc-v112-rec-sleep-surgery-hns-troubleshooting-nonresponse": "cc:cc-v112-mgt-sleep-surgery-hns-troubleshooting-nonresponse",
 "cc:cc-v112-rec-thyroid-parathyroid-salivary-primary-hyperparathyroidism": "cc:cc-v112-mgt-thyroid-parathyroid-salivary-primary-hyperparathyroidism",
 "challenge:v113-lar-02": "challenge:v244_ped_rrp_fnd",
 "challenge:v116-end-02": "challenge:v137_tps_05",
 "challenge:v119-allergy-01": "challenge:v212_rhi_ar_found",
 "challenge:v119-allergy-05": "challenge:v218_rhi_aerd_fnd",
 "challenge:v11_ped_03": "challenge:v269_gen_afb_app",
 "challenge:v11_ped_05": "challenge:v241_ped_tgdc_fnd",
 "challenge:v124_oto_01": "challenge:v154_oto_fnd",
 "challenge:v128_lar_02": "challenge:v254_lar_polycyst_fnd",
 "challenge:v139_gen_15": "challenge:v11_rhi_02",
 "challenge:v139_ped_16": "challenge:v146_ped_15",
 "challenge:v145_hn_15": "challenge:v140_hn_07",
 "challenge:v145_lar_02": "challenge:v138_lar_02",
 "challenge:v146_tps_04": "challenge:v233_tps_php_snr",
 "challenge:v490-facial-plastics-1-41": "challenge:v490-rhinology-1-46",
 "challenge:v490-facial-plastics-1-93": "challenge:v139_gen_19",
 "challenge:v490-general-ent-1-92": "challenge:v490-rhinology-5-76",
 "challenge:v490-general-ent-1-96": "challenge:v175_oto_petrous_app",
 "challenge:v490-head-neck-1-77": "challenge:v490-thyroid-2-6",
 "challenge:v490-head-neck-2-38": "challenge:v490-thyroid-1-15",
 "challenge:v490-head-neck-2-97": "challenge:v490-thyroid-2-6",
 "challenge:v490-otology-1-109": "challenge:v490-pediatric-1-21",
 "challenge:v490-otology-2-101": "challenge:v490-otology-1-38",
 "challenge:v490-otology-2-25": "challenge:v490-otology-1-31",
 "challenge:v490-otology-3-23": "challenge:v490-otology-2-5",
 "challenge:v490-otology-3-45": "challenge:v490-otology-1-20",
 "challenge:v490-pediatric-1-38": "challenge:v244_ped_bca_fnd",
 "challenge:v490-pediatric-1-71": "challenge:v490-general-ent-1-6",
 "challenge:v490-pediatric-2-20": "challenge:v248_ped_jrp_fnd",
 "challenge:v490-pediatric-3-49": "challenge:v490-sleep-1-86",
 "challenge:v490-pediatric-3-63": "challenge:v490-pediatric-1-11",
 "challenge:v490-rhinology-1-35": "challenge:v490-facial-plastics-1-5",
 "challenge:v490-rhinology-1-89": "challenge:v490-head-neck-2-53",
 "challenge:v490-rhinology-2-104": "challenge:v490-facial-plastics-1-40",
 "challenge:v490-rhinology-2-76": "challenge:v490-rhinology-1-61",
 "challenge:v490-rhinology-2-81": "challenge:v490-rhinology-1-10",
 "challenge:v490-rhinology-3-16": "challenge:v490-topup-general-29",
 "challenge:v490-rhinology-5-74": "challenge:v490-rhinology-4-63",
 "challenge:v490-rhinology-5-77": "challenge:v490-rhinology-1-74",
 "challenge:v490-thyroid-2-17": "challenge:v490-thyroid-1-69",
 "challenge:v490-topup-facial-31": "challenge:v490-gap-fill-1-46",
 "challenge:v490-topup-general-1": "challenge:v490-general-ent-1-1",
 "challenge:v490-topup-thyroid-18": "challenge:v490-thyroid-1-5"
}


def install_question_dedupe_v690(data):
    banks = {"cc": "CONCEPT_CHECKS_V112", "challenge": "CLINICAL_CHALLENGES_V119"}
    removed = {}
    for prefix, name in banks.items():
        rows = getattr(data, name, None)
        if not isinstance(rows, list):
            continue
        drop = {k.split(":", 1)[1] for k in RETIRED_V690 if k.startswith(prefix + ":")}
        keep = [q for q in rows if str(q.get("id")) not in drop]
        removed[name] = len(rows) - len(keep)
        rows[:] = keep
    return removed


def install_retired_redirects_v690(app):
    """Old links to a retired question open its kept twin (or the topic list)."""
    from flask import redirect, url_for
    endpoints = {"challenge": "clinical_challenge", "cc": "concept_check"}
    for prefix, ep in endpoints.items():
        view = app.view_functions.get(ep)
        if not view or getattr(view, "_retired_v690", False):
            continue

        def make(view=view, prefix=prefix, ep=ep):
            def wrapped(qid, *a, **kw):
                keep = RETIRED_V690.get(f"{prefix}:{qid}")
                if f"{prefix}:{qid}" in RETIRED_V690 and keep and keep.startswith(prefix + ":"):
                    return redirect(url_for(ep, qid=keep.split(":", 1)[1]))
                if f"{prefix}:{qid}" in RETIRED_V690 and keep:
                    other = "clinical_challenge" if keep.startswith("challenge:") else "concept_check"
                    return redirect(url_for(other, qid=keep.split(":", 1)[1]))
                return view(qid, *a, **kw)
            wrapped._retired_v690 = True
            return wrapped
        app.view_functions[ep] = make()
    return True
