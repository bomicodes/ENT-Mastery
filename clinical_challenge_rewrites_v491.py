"""v49.1 sweep: rewrites of the older practice-bank questions to the v49 board-vignette standard.

Rewrites live in ``rewrites_v491/<batch>.py`` as ``REWRITES = {question_id: {fields}}``. Each one replaces
the question's stem, choices, answer, explanation, why_wrong, board pearl and curveball in place, so the
question id (and every learner's history on it) is unchanged. Topic, concept, stage and focus are kept.
Must run before the Daily Path installer, which indexes questions at install time.
"""
import importlib
import pkgutil

FIELDS = ("stem", "choices", "answer", "explanation", "why_wrong", "board_pearl", "curveball", "curveball_answer")
# Questions whose curated wording a release audit pins verbatim (ids referenced in audit_*.py); left untouched.
SKIP_IDS = set(["v113-oto-02", "v11_fprs_05", "v124_ped_06", "v128_hn_03", "v128_lar_01", "v128_lar_03", "v136_oto_13", "v136_rhi_04", "v136_rhi_17", "v136_rhi_21", "v136_rhi_23", "v136_rhi_26", "v137_fpt_10", "v137_tps_05", "v137_tps_08", "v138_hn_02", "v138_hn_08", "v138_hn_24", "v139_gen_10", "v140_gen_10", "v140_ped_06", "v141_slp_06", "v142_rhi_04", "v143_hno_01", "v143_lar_04", "v143_rhi_03", "v144_oto_22", "v144_rh_17", "v144_rh_21", "v145_hn_02", "v145_lar_16", "v147_fp_14", "v152_ped_01", "v154_hn_app", "v154_hn_fnd", "v206_rhi_max_app", "v207_rhi_frontal_snr", "v208_rhi_pedscrs_snr", "v209_rhi_revision_snr", "v209_rhi_sphenoid_snr", "v212_rhi_ar_found", "v212_rhi_lar_app", "v212_rhi_lar_snr", "v219_hn_neck_app", "v219_hn_neck_snr", "v219_hn_tongue_app", "v219_hn_tongue_fnd", "v219_hn_tongue_snr", "v220_hn_bot_snr", "v220_hn_fom_fnd", "v220_hn_glottic_snr", "v220_hn_supra_app", "v220_hn_supra_fnd", "v220_hn_supra_snr", "v220_hn_tonsil_snr", "v222_hn_tep_fnd", "v222_hn_tep_snr", "v225_hn_salv_postcrt_app", "v231_hn_neckcomp_app", "v231_hn_neckcomp_fnd", "v231_hn_neckcomp_snr", "v231_hn_nfl_app", "v231_hn_nfl_fnd", "v231_hn_nfl_snr", "v235_tps_indet_fnd", "v236_tps_ptca_fnd", "v242_ped_ear_app", "v242_ped_ear_snr", "v243_ped_sgh_snr", "v243_ped_tm_fnd", "v245_ped_hl_app", "v246_ped_cranio_fnd", "v252_lar_mtd_snr", "v254_lar_nodule_app", "v254_lar_nodule_fnd", "v254_lar_polycyst_fnd", "v254_lar_polycyst_snr", "v256_lar_rad_dys_app", "v256_lar_rad_dys_fnd", "v256_lar_rad_dys_snr", "v258_fpt_frontal_app", "v258_fpt_frontal_fnd", "v258_fpt_frontal_snr", "v258_fpt_noe_app", "v262_fpt_otoplasty_fnd", "v267_sleep_ds_snr", "v269_gen_afb_app", "v295_fpt_frontal_outflow_mgt", "v299_sleep_peds_psg_mgt", "v416_rhi_csf_oncall_disposition"])
# Groups an audit pins by id prefix (audit_rhinology_v209 checks the v208_rhi_ batch's answer positions).
SKIP_PREFIXES = ("v208_rhi_", "v246_ped_tubes_")  # + audit_pediatric_ear_semantic_v289


def _valid(r):
    ch, a, ww = r.get("choices"), r.get("answer"), r.get("why_wrong")
    return (all(k in r for k in FIELDS) and isinstance(ch, list) and len(ch) == 4 and isinstance(a, int)
            and 0 <= a < 4 and isinstance(ww, list) and len(ww) == 4 and str(r.get("stem", "")).strip())


def _load():
    import rewrites_v491
    out, audited = {}, set()
    for info in sorted(pkgutil.iter_modules(rewrites_v491.__path__), key=lambda i: i.name):
        mod = importlib.import_module("rewrites_v491." + info.name)
        batch = getattr(mod, "REWRITES", {})
        out.update(batch)
        if info.name.startswith("lk"):  # v49.3: locked questions rewritten together with their audits
            audited.update(batch)
    return out, audited


def install_clinical_challenge_rewrites_v491(data, app_mod=None):
    rewrites, audited = _load()
    by_id = getattr(data, "CLINICAL_CHALLENGE_BY_ID_V119", None)
    targets = {}
    for q in data.CLINICAL_CHALLENGES_V119:
        targets.setdefault(q.get("id"), []).append(q)
    for d in (by_id, getattr(app_mod, "CLINICAL_CHALLENGE_BY_ID_V119", None) if app_mod else None):
        if isinstance(d, dict):
            for qid, q in d.items():
                if not any(q is t for t in targets.get(qid, [])):
                    targets.setdefault(qid, []).append(q)
    applied, rejected, missing = [], [], []
    for qid, r in rewrites.items():
        if qid not in audited and (qid in SKIP_IDS or str(qid).startswith(SKIP_PREFIXES)):
            continue
        if not _valid(r):
            rejected.append(qid)
            continue
        if qid not in targets:
            missing.append(qid)
            continue
        row = {k: r[k] for k in FIELDS}
        ww = list(row["why_wrong"])
        if str(ww[row["answer"]]).strip() == "Correct.":
            first = str(row["explanation"]).split(". ")[0].rstrip(".")
            ww[row["answer"]] = "Correct. " + first + "."
        row["why_wrong"] = ww
        for q in targets[qid]:
            q.update(row)
            q["rewritten_v491"] = True
        applied.append(qid)
    result = {"applied": len(applied), "rejected": rejected, "missing": missing}
    data.CLINICAL_CHALLENGE_REWRITES_V491 = result
    return result
