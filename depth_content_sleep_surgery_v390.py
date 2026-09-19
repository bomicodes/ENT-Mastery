"""v39.0 -- Sleep Surgery depth repair (content-staleness sweep, batch 1/9).

Fixes two shallow-content defects flagged during a repo-wide scan:
  1. recognize/localize verbatim-duplicated across many topics.
  2. operate beginning with the unfilled generic authoring placeholder
     ("For operative/procedural cases, explicitly state..." /
     "State whether a procedure is indicated; if so, rehearse...") instead
     of real advanced-decision content.

Enriches existing canonical modules in place (pattern from
otitis_externa_depth_v157 / thyroglossal_duct_cyst_depth_v389); raises
loudly if an expected topic is missing so curriculum drift is caught.
"""

DOMAIN = "Sleep Surgery"

DEPTH_V390 = {
    "Tongue Base Surgery": {
        "recognize": (
            "Retroglossal/tongue-base obstruction is suspected when drug-induced sleep endoscopy "
            "(DISE) or exam shows lingual tonsil hypertrophy, posterior tongue-base collapse against "
            "the pharyngeal wall, or epiglottic collapse driven by the tongue base rather than the "
            "epiglottis itself, in a patient whose OSA has not responded to (or is not a candidate "
            "for) palatal surgery alone."
        ),
        "localize": (
            "The obstruction level is the retroglossal airway, bounded by the tongue base "
            "anteriorly, posterior pharyngeal wall posteriorly, and often complicated by lingual "
            "tonsil bulk or a low-lying/collapsing epiglottis; this is distinct from retropalatal "
            "(velum) or lateral pharyngeal wall obstruction, and multilevel disease is common, so "
            "DISE is used to confirm the tongue base is a real contributor before committing to a "
            "tongue-base-directed operation."
        ),
        "operate": (
            "Indication: DISE-confirmed retroglossal/tongue-base collapse contributing to "
            "moderate-severe OSA, most often after failed CPAP and often combined with palatal "
            "surgery when multilevel disease is present. Options are matched to phenotype: lingual "
            "tonsillectomy for lymphoid hypertrophy, midline glossectomy/tongue-base reduction "
            "(endoscopic or transoral robotic) for bulk, or genioglossus advancement/hyoid suspension "
            "for a skeletal-collapse pattern. Danger structures: lingual artery and hypoglossal "
            "nerve within the tongue base, and the airway itself -- tongue-base edema can progress "
            "over the first 24-48 hours after resection. Key steps: define the resection/suspension "
            "extent preoperatively from DISE findings rather than a fixed volume; preserve a safety "
            "margin from the vallecula/epiglottis to avoid destabilizing swallowing. Failure mode: "
            "under-treating a multilevel collapse (tongue base alone when the palate also contributes) "
            "or over-resecting tongue base tissue, which risks dysphagia. Postoperative plan: airway "
            "monitoring (occasionally overnight admission or planned tracheostomy avoidance protocol "
            "for extensive resections), analgesia, and staged advancement of oral intake as edema "
            "resolves; a postoperative sleep study is used to confirm response before assuming cure."
        ),
    },
    "HNS Activation / Programming": {
        "recognize": (
            "Hypoglossal nerve stimulator (HNS) implantation is only step one; the device must be "
            "activated after a healing interval (commonly around 4 weeks) and then progressively "
            "titrated, so a patient reporting persistent symptoms or discomfort in the first days "
            "after activation is not necessarily a treatment failure -- programming has not yet been "
            "optimized."
        ),
        "localize": (
            "Effect is generated at the hypoglossal nerve cuff (protrusor-selective stimulation of "
            "genioglossus, sparing retrusors) and expressed at the tongue-base/oropharyngeal airway; "
            "problems localize either to the device/lead (impedance, lead migration), the stimulation "
            "parameters (amplitude, pulse width, electrode configuration), or persistent collapse at "
            "a level the device does not address (e.g., unaddressed palatal or lateral wall collapse)."
        ),
        "operate": (
            "No further surgery is usually indicated once the device is implanted and healed; the "
            "'procedure' at this stage is programming, not the OR. Setup: home sleep testing or "
            "in-lab titration polysomnography to adjust amplitude and, if needed, electrode "
            "configuration while watching tongue protrusion and airway response on endoscopy or "
            "sleep study. Key steps: start amplitude low and advance gradually to the patient's "
            "comfortable functional threshold, address bothersome tongue motion, mouth/tooth "
            "discomfort or FOSTIM (functional obstructive) response before assuming device failure. "
            "Failure mode: judging success or failure from the incision or from the very first "
            "activation, or attributing residual events to the device when unaddressed multilevel "
            "or positional obstruction is the real driver. Postoperative plan: gradual outpatient "
            "advancement of stimulation settings, symptom and device-log review, and a follow-up "
            "sleep study to confirm the titrated settings actually reduce AHI before declaring success."
        ),
    },
    "Central Events / Hypoventilation": {
        "recognize": (
            "Central sleep apnea (repetitive cessation of respiratory effort, not just airflow) and "
            "sleep-related hypoventilation (sustained rise in CO2 during sleep) are driven by "
            "impaired respiratory drive or mechanics rather than mechanical upper-airway collapse, so "
            "they should be suspected when apneas occur without the effort/arousal pattern of "
            "obstruction, in patients with heart failure, opioid use, high-altitude exposure, "
            "neuromuscular disease, or severe obesity/restrictive chest disease."
        ),
        "localize": (
            "The abnormality is central (brainstem respiratory drive) or restrictive/neuromuscular "
            "(chest-wall or muscle mechanics), not the pharyngeal airway that upper-airway/sleep "
            "surgery is designed to treat; distinguishing this requires reading the polysomnogram's "
            "respiratory effort channels and CO2/oxygen trend, not just the total apnea-hypopnea "
            "index (AHI), since AHI is a sum of obstructive, central, and mixed events."
        ),
        "operate": (
            "Upper-airway surgery is not indicated for a predominantly central or hypoventilation "
            "pattern and should not be offered by default just because the AHI is elevated. Setup: "
            "confirm the event breakdown on polysomnography (central apnea index, Cheyne-Stokes "
            "pattern, transcutaneous/end-tidal CO2 trend) and review contributing medications "
            "(opioids), cardiac status (heart failure, ejection fraction), and neurologic/pulmonary "
            "disease. Key steps: route management to sleep medicine, pulmonology, and cardiology for "
            "etiology-directed care: CPAP, oxygen, acetazolamide, adaptive servo-ventilation "
            "in selected patients, or backup-rate/volume-assured ventilation when indicated "
            "for hypoventilation, alongside opioid reduction and treatment of underlying disease. "
            "In heart failure with reduced ejection fraction, ASV requires experienced-center "
            "selection and close monitoring under the 2025 AASM guidance; device-specific "
            "contraindications and ejection fraction must be checked. Failure mode: treating a "
            "mixed picture as purely obstructive and proceeding to upper-airway surgery, which will "
            "not correct the central or hypoventilation component and can delay appropriate "
            "cardiopulmonary management. Postoperative plan: not applicable to ENT surgery in the "
            "predominantly central/hypoventilation phenotype; the surgeon's role is recognizing the "
            "pattern and referring rather than operating."
        ),
    },
}


def apply_depth_content_sleep_surgery_v390(data_module):
    modules = {m.get("topic"): m for m in data_module.DEEP_MODULES_V6.get(DOMAIN, [])}
    missing = [t for t in DEPTH_V390 if t not in modules]
    if missing:
        raise RuntimeError(f"v39.0: expected {DOMAIN} topics not found: {missing}")
    for topic, fields in DEPTH_V390.items():
        modules[topic].update(fields)
    return {"enriched": list(DEPTH_V390.keys())}
