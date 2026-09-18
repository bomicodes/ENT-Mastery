"""v37.5: replace standalone DTC RAI/TSH stub with operational 2025 ATA criteria.
Keep distinct from parent DTC card and RAIR-DTC card. Idempotent.
Source: 2025 ATA adult differentiated thyroid cancer guideline, recommendations
28, 32, 43, 45-46 and Table 9: https://pmc.ncbi.nlm.nih.gov/articles/PMC13090833/
"""

TOPIC = "Radioactive Iodine and TSH Suppression in DTC"
MARKER = "2025 ATA FOUR-BAND RAI/TSH DECISION"

RECOGNIZE_V375 = (
    "2025 ATA FOUR-BAND RAI/TSH DECISION: RAI remnant ablation, adjuvant treatment of suspected "
    "microscopic cancer and treatment of known iodine-avid disease are different intents. RAI "
    "is administered following total or near-total thyroidectomy, not routinely after lobectomy; "
    "completion thyroidectomy may be considered when RAI is indicated. Neither RAI nor chronic "
    "TSH suppression is automatic after a DTC diagnosis. Appropriately selected low-risk "
    "papillary microcarcinoma may undergo active surveillance or surgery alone without RAI."
)
LOCALIZE_V375 = (
    "RAI treats iodine-avid remnant or tumor; thyroid hormone suppresses TSH-driven stimulation. "
    "Use four 2025 ATA recurrence-risk bands: LOW <10%, LOW-INTERMEDIATE 10-15%, "
    "INTERMEDIATE-HIGH 16-30%, HIGH >30%. Assign using histologic subtype, microscopic versus "
    "gross extrathyroidal extension, vascular invasion extent, aggressive histology, positive "
    "margins/residual tumor, number/size/extranodal spread of involved nodes, distant disease, "
    "and postoperative findings. An intrathyroidal well-differentiated tumor without important "
    "adverse features commonly belongs in low risk; gross extension, distant disease or bulky "
    "residual/nodal disease raise risk. Individual findings do not all map to one universal band: "
    "apply the histology-specific ATA table and distinguish recurrence risk from AJCC stage."
)
WORKUP_V375 = (
    "Before RAI decide the intent using final pathology, operative extent and residual disease, "
    "postoperative neck ultrasound, Tg with anti-Tg antibodies, imaging and iodine-avidity "
    "when relevant; interpret Tg in light of lobectomy versus total thyroidectomy and prior "
    "RAI. Reassess response longitudinally rather than waiting for an arbitrary 12-month cutoff. "
    "2025 ATA dynamic response after total thyroidectomy plus RAI: EXCELLENT = negative imaging "
    "and nonstimulated Tg <0.2 ng/mL or stimulated Tg <1 ng/mL; INDETERMINATE = nonspecific "
    "imaging, nonstimulated Tg 0.2-1 or stimulated Tg 1-10, or stable/declining TgAb; "
    "BIOCHEMICALLY INCOMPLETE = nonstimulated Tg >1 or stimulated Tg >10, or rising TgAb, "
    "without structural disease; STRUCTURALLY INCOMPLETE = persistent/new structural disease "
    "regardless of Tg. Without RAI, excellent-response nonstimulated Tg threshold is <2.5 ng/mL "
    "with negative imaging; after hemithyroidectomy, response classification differs and Tg "
    "cutoffs from total thyroidectomy must not be imported."
)
MANAGE_V375 = (
    "2025 ATA RAI CANDIDACY: after total thyroidectomy, do not routinely administer RAI "
    "for low-risk DTC; consider it for low-intermediate or intermediate-high risk according "
    "to histology, disease burden, postoperative Tg/imaging, likely benefit and preference; "
    "recommend it for high-risk disease and appropriate distant metastases. Distinguish "
    "adjuvant RAI from treatment of identified iodine-avid tumor and reevaluate utility for "
    "RAI-refractory disease. Counsel about sialadenitis/xerostomia, lacrimal injury, marrow "
    "effects and possible second malignancy. Pregnancy and breastfeeding preclude treatment; "
    "verify pregnancy status and ensure lactation has ceased for the guideline-recommended "
    "interval. Use low-iodine preparation and appropriate TSH stimulation with thyroid "
    "hormone withdrawal or recombinant human TSH based on indication. "
    "TSH GOALS (2025 ATA recommendations 45-46 and Table 9): individualize initial suppression "
    "based on recurrence risk, persistent disease and harms; do not prescribe fixed legacy "
    "targets (<0.1, 0.1-0.5 or 0.5-2 mIU/L) indiscriminately. An excellent or indeterminate "
    "response generally calls for TSH within the laboratory normal reference range; "
    "biochemically or structurally incomplete response may warrant TSH below that range, "
    "particularly with progressive disease. Long-term suppression is not suggested for "
    "low/intermediate-risk patients without biochemical or structural recurrence. Weigh "
    "atrial fibrillation, osteoporosis and other suppression harms, especially in older patients."
)
OPERATE_V375 = (
    "Choose lobectomy versus total thyroidectomy from primary tumor extent, nodal/distant "
    "disease, bilateral pathology, risk, functional morbidity and patient priorities, not "
    "solely to make RAI possible. For selected low-risk unilateral DTC, lobectomy may be "
    "definitive and does not require RAI. Consider completion thyroidectomy for residual "
    "cancer or when pathology and postoperative assessment establish a compelling RAI indication, "
    "not as a reflex to any incidental cancer diagnosis."
)
TEACH_V375 = (
    "BOARDS/CHIEF DECISION: specify RAI intent (remnant ablation versus adjuvant versus "
    "known disease), operation performed, four-band ATA recurrence risk and pathology, "
    "postoperative Tg/imaging, and dynamic response before selecting RAI and TSH strategy. "
    "Post-total-thyroidectomy-plus-RAI excellent Tg is <0.2 ng/mL unstimulated or <1 "
    "stimulated with negative imaging; without RAI use treatment-specific thresholds. "
    "Excellent/indeterminate response generally means TSH in the normal range; incomplete "
    "response may justify below-normal TSH. Older numeric suppression targets are historical "
    "rather than universal 2025 ATA mandates."
)


def apply_rai_tsh_dtc_criteria_v375(data_module, app_module=None):
    patched = []
    for modules in (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).values():
        for module in modules or []:
            if module.get("topic") != TOPIC:
                continue
            if MARKER not in (module.get("recognize") or ""):
                for key, value in (
                    ("recognize", RECOGNIZE_V375), ("localize", LOCALIZE_V375),
                    ("workup", WORKUP_V375), ("manage", MANAGE_V375),
                    ("operate", OPERATE_V375), ("teach", TEACH_V375),
                ):
                    module[key] = value
            tags = module.setdefault("tags", [])
            for tag in ("ATA four risk bands", "RAI candidacy", "TSH suppression targets", "dynamic risk response"):
                if tag not in tags:
                    tags.append(tag)
            patched.append(TOPIC)
    if not patched:
        raise RuntimeError("v37.5: could not find canonical Radioactive Iodine and TSH Suppression in DTC topic")
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
