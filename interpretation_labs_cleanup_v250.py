"""Interpretation Atlas hard cleanup and PSG case-bank rebuild.

This module is applied once during production startup, before users hit the lab routes.
It removes retired lab records from the live registry, strips Open Anatomy / SPL
resources from every interpretation lab, and replaces the legacy PSG entry with a
case-based polysomnography interpretation lab.

The PSG cases are synthetic teaching studies. They are intentionally structured around
signal interpretation (airflow, thoracoabdominal effort, oxygenation, CO2, stage and
position) rather than diagnosis-by-label.
"""

from copy import deepcopy
import re


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _retired_lab(slug, lab):
    text = _norm(" ".join([
        slug,
        lab.get("title", ""),
        lab.get("subtitle", ""),
        lab.get("source_note", ""),
    ]))
    # Retire the two requested lab experiences, not merely their cards.
    if "upmc" in text and ("digital slide" in text or "slide viewer" in text or "pathology" in text):
        return True
    if "sinonasal" in text and ("fess" in text or "navigation" in text or "endoscopy" in text):
        return True
    if "fess navigation" in text or "sinus navigation lab" in text:
        return True
    return False


def _is_open_anatomy_spl(resource):
    text = _norm(" ".join([
        resource.get("name", ""),
        resource.get("note", ""),
        resource.get("url", ""),
    ]))
    return (
        "open anatomy" in text
        or "openanatomy" in text
        or "surgical planning laboratory" in text
        or "spl anatomy" in text
        or (" spl " in f" {text} " and "anatom" in text)
    )


def _case(case_id, level, title, visual, summary, prompt, answer, why,
          reason_prompt, reason_answer, follow, teach_prompt, teach_answer,
          teach_follow_answer, track="core"):
    return {
        "id": case_id,
        "concept_id": "psg-interpretation",
        "variant_type": "interpret",
        "level": level,
        "track": track,
        "visual": visual,
        "visual_note": title,
        "study_summary": summary,
        "prompt": prompt,
        "answer": answer,
        "why": why,
        "reason_prompt": reason_prompt,
        "reason_answer": reason_answer,
        "follow": follow,
        "teach_prompt": teach_prompt,
        "teach_answer": teach_answer,
        "teach_follow_answer": teach_follow_answer,
    }


def _psg_cases():
    return [
        _case(
            "psg-normal-primary-snoring", 1, "Case 1 · Primary snoring / no clinically important apnea",
            "lab_assets/sleep_psg.svg",
            [
                ["Patient", "7-year-old with nightly snoring"],
                ["TST", "420 min"], ["AHI", "0.8/h"], ["OAHI", "0.5/h"], ["CAI", "0.3/h"],
                ["SpO₂ nadir", "94%"], ["CO₂", "No sustained elevation"],
            ],
            "Start with the raw study rather than the referral diagnosis. Is this PSG normal, obstructive, central, or mixed—and which numbers actually support your call?",
            "This study does not show a meaningful obstructive or central apnea burden. Snoring alone does not make the PSG obstructive sleep apnea; the event indices, oxygenation, CO₂ pattern, sleep time, and signal quality must agree.",
            "A useful PSG read begins by separating symptoms from scored physiology. A child can snore without having a pathologic apnea index on the recorded night.",
            "If you saw a few short pauses in airflow near sleep onset, what would stop you from automatically calling them central sleep apnea?",
            "Central events must be interpreted in context. In children, short central pauses can occur normally; a scored pediatric central apnea requires absent inspiratory effort and the applicable duration/physiologic consequence criteria. A low CAI with no important gas-exchange effect is not synonymous with a central sleep apnea syndrome.",
            "Before finalizing, confirm total sleep time, REM representation, body position, airflow/effort signal integrity, and whether the night plausibly sampled the child's usual symptoms.",
            "Teach a junior the difference between snoring, an isolated central pause, and a sleep apnea syndrome.",
            "Snoring is a sound. An apnea is a scored respiratory event. A syndrome requires the overall PSG pattern plus clinical context; do not turn one central-looking pause or a symptom label into the diagnosis.",
            "This prevents overcalling incidental central events and prevents undercalling a technically limited study.",
        ),
        _case(
            "psg-pediatric-obstructive", 2, "Case 2 · Classic pediatric obstructive apnea",
            "lab_assets/adult_psg_moderate.svg",
            [
                ["Patient", "6-year-old with snoring, witnessed pauses, 3+ tonsils"],
                ["TST", "405 min"], ["AHI", "11.4/h"], ["OAHI", "10.8/h"], ["CAI", "0.6/h"],
                ["SpO₂ nadir", "86%"], ["Pattern", "REM-predominant obstructive events"],
            ],
            "During repeated events, airflow becomes absent while thoracic and abdominal effort continues and often increases. What type of apnea is this, and what should you report beyond the total AHI?",
            "These are obstructive events: airflow is absent or markedly reduced while respiratory effort persists. The study is dominated by obstruction, so report the obstructive burden (OAHI), oxygenation, CO₂, REM/position dependence, and clinically relevant event clustering—not just total AHI.",
            "The single most useful obstructive-versus-central discriminator on PSG is respiratory effort during the airflow loss. Ongoing effort means the respiratory drive is present but the upper airway is not transmitting airflow.",
            "Why can an obstructive event show paradoxical chest/abdominal motion or increasing effort as the event continues?",
            "The patient continues trying to breathe against an occluded or critically narrowed upper airway. Negative intrathoracic pressure can increase and thoracoabdominal motion may become paradoxical, reinforcing an obstructive mechanism.",
            "Then check whether obstruction is worse in REM or supine sleep and whether CO₂ retention accompanies partial obstruction; those findings can change severity assessment and perioperative planning.",
            "Give the 20-second PSG explanation you would use when counseling a family before adenotonsillectomy.",
            "The study shows repeated upper-airway obstruction during sleep: breathing effort continues, but airflow repeatedly falls away, with associated oxygen disturbance. The obstructive index—not the presence of a few central events—is the dominant physiology.",
            "For ENT, the PSG should feed into airway anatomy, comorbidity, severity, postoperative monitoring risk, and the likelihood of residual disease rather than functioning as a stand-alone number.",
        ),
        _case(
            "psg-central-apnea", 2, "Case 3 · Central apnea physiology",
            "lab_assets/adult_central.svg",
            [
                ["Patient", "10-year-old referred for pauses without prominent snoring"],
                ["TST", "390 min"], ["AHI", "7.2/h"], ["OAHI", "0.9/h"], ["CAI", "6.3/h"],
                ["SpO₂ nadir", "89%"], ["Event signal", "Airflow absent AND thoracoabdominal effort absent"],
            ],
            "Airflow stops, and both thoracic and abdominal effort disappear for the same interval. How is that fundamentally different from the prior case?",
            "This is central apnea physiology: airflow and inspiratory effort are absent together. The elevated CAI and low obstructive index make central events the dominant respiratory abnormality in this teaching study.",
            "In obstruction, the brain/respiratory pump is still trying to breathe against a blocked airway. In a central event, inspiratory drive/effort is absent during the event, so there is no chest/abdominal effort to accompany the airflow pause.",
            "In a child, is every brief effort-free pause automatically scored as a central apnea?",
            "No. Pediatric scoring requires absent inspiratory effort throughout the event plus the applicable duration or physiologic-consequence criteria. Brief central pauses can occur in normal children, especially around sleep transitions, so morphology and context matter.",
            "A genuinely elevated central burden should trigger a different differential from routine adenotonsillar OSA: neurologic/brainstem disease, medication effects, altitude, cardiopulmonary disease, congenital ventilatory disorders, and other causes depend on age and context.",
            "Teach the signal-level distinction between obstructive and central apnea without using the words 'blocked airway' or 'brain problem.'",
            "Obstructive: airflow disappears but inspiratory effort continues. Central: airflow disappears and inspiratory effort disappears with it. Mixed: the same event contains both effort-free and effort-present portions.",
            "That signal-first framework is more reliable than guessing from desaturation depth, snoring, or the total AHI.",
        ),
        _case(
            "psg-mixed-apnea", 3, "Case 4 · Mixed apnea: one event, two physiologies",
            "lab_assets/adult_central.svg",
            [
                ["Patient", "8-year-old with complex sleep-disordered breathing"],
                ["Event", "Airflow absent throughout"], ["Early event", "No thoracoabdominal effort"],
                ["Late event", "Effort resumes while airflow remains absent"], ["SpO₂", "92% → 87%"],
            ],
            "The event begins with no airflow and no effort; effort then resumes before airflow returns. Central, obstructive, or mixed? Walk through the tracing in time rather than naming it from the first five seconds.",
            "This is a mixed apnea: the event contains a central component (no airflow, no inspiratory effort) and an obstructive component (no airflow despite resumed effort).",
            "Mixed events expose why PSG must be read dynamically. Classification depends on how airflow and effort relate across the whole event, not a single screenshot or the oxygen nadir.",
            "What mistake happens if you classify the event only from its beginning? What if you classify it only from its end?",
            "Looking only at the beginning overcalls a purely central event; looking only at the end overcalls a purely obstructive event. The defining feature is the presence of both components within one apnea.",
            "When the study contains many mixed events, quantify the broader pattern rather than assuming that 'mixed' automatically means a primary central apnea disorder.",
            "Explain mixed apnea to a junior using airflow and effort as two separate channels.",
            "Track two questions in parallel: is air moving, and is the patient trying to breathe? In mixed apnea, airflow stays absent while the effort channel changes from absent to present, or vice versa, within the same event.",
            "This keeps mixed apnea from becoming a vague label and makes the interpretation reproducible.",
        ),
        _case(
            "psg-severe-pediatric-osa-gas-exchange", 4, "Case 5 · Severe obstruction plus gas-exchange abnormality",
            "lab_assets/adult_psg_moderate.svg",
            [
                ["Patient", "4-year-old with loud snoring, retractions, restless sleep"],
                ["TST", "410 min"], ["OAHI", "28.6/h"], ["CAI", "0.4/h"],
                ["SpO₂ nadir", "74%"], ["CO₂", "Sustained elevation during obstructed sleep"],
                ["Pattern", "Clusters in REM with partial obstruction between discrete apneas"],
            ],
            "Do not stop at 'AHI 29.' What additional PSG features make this a higher-risk ENT sleep study, and what physiology are they showing?",
            "The obstructive burden is high and is accompanied by major gas-exchange disturbance: deep desaturation and sustained CO₂ elevation during obstructed sleep. This is more clinically informative than the AHI alone and raises perioperative/postoperative respiratory risk.",
            "Children may have prolonged partial upper-airway obstruction and hypoventilation in addition to discrete apneas/hypopneas. Oxygen and CO₂ channels therefore matter, especially when deciding how worried to be after airway surgery.",
            "Why can a child with important obstructive physiology look worse than another child with a similar AHI?",
            "AHI counts event frequency, not the full physiologic cost. Event duration, clustering, baseline reserve, desaturation depth, CO₂ retention, REM concentration, arousal pattern, age, obesity, craniofacial/neuromuscular disease, and other comorbidities can make two identical AHIs clinically very different.",
            "For an ENT preoperative read, explicitly extract OAHI/AHI, oxygen nadir and burden, CO₂/hypoventilation pattern, REM/position effects, central burden, and relevant comorbidity—not just the severity label.",
            "Give an attending-level one-liner for this study that communicates risk rather than merely a number.",
            "Severe pediatric obstructive sleep apnea with REM-clustered upper-airway obstruction, marked oxygen desaturation, and associated nocturnal hypoventilation; central events are not the dominant process.",
            "That summary immediately tells the surgical team more than 'AHI 28.6' and supports postoperative monitoring decisions.",
        ),
        _case(
            "psg-rem-positional-osa", 3, "Case 6 · REM / positional dependence",
            "lab_assets/adult_positional.svg",
            [
                ["Patient", "15-year-old with intermittent symptoms"],
                ["Overall OAHI", "6.1/h"], ["REM OAHI", "18.4/h"], ["NREM OAHI", "2.2/h"],
                ["Supine OAHI", "14.0/h"], ["Nonsupine OAHI", "1.8/h"], ["CAI", "0.5/h"],
            ],
            "The overall number looks modest. What pattern would you miss if you read only the total OAHI, and why does adequate REM/supine sampling matter?",
            "Obstruction is concentrated in REM and supine sleep. The overall index averages together vulnerable and less-vulnerable periods, so insufficient REM or supine sleep can make the recorded night underestimate the patient's worst physiology.",
            "Sleep stage and body position are modifiers of upper-airway collapsibility. A study is not fully interpreted until you ask when the events occur, not only how many occurred across the whole night.",
            "How should a technically limited study with almost no REM affect your confidence when the clinical history is strongly suggestive of obstruction?",
            "It should lower confidence in a reassuring overall index because the study may not have sampled the state in which obstruction is worst. The response is not to invent a diagnosis, but to state the limitation and integrate the clinical picture.",
            "Also verify that position and stage denominators are large enough to interpret subgroup indices; tiny amounts of REM or supine sleep can make subgroup numbers unstable.",
            "Teach why 'overall AHI' is a summary, not the whole PSG.",
            "The total index is an average. PSG interpretation adds morphology, effort, oxygen/CO₂ consequences, sleep stage, position, arousals, and study adequacy so that the average is not mistaken for the entire disease pattern.",
            "This is particularly useful when symptoms and the headline AHI seem discordant.",
        ),
        _case(
            "psg-central-events-not-csa", 4, "Case 7 · Central events present ≠ central sleep apnea syndrome",
            "lab_assets/adult_central.svg",
            [
                ["Patient", "5-year-old with adenotonsillar hypertrophy and classic obstructive symptoms"],
                ["AHI", "14.2/h"], ["OAHI", "12.9/h"], ["CAI", "1.3/h"],
                ["Central pattern", "Scattered, often near arousal/sleep transition"], ["SpO₂ nadir", "84% with obstructive clusters"],
            ],
            "There are real scored central apneas on the report. Does that make the study 'central sleep apnea'? Build the interpretation from the relative burdens and event context.",
            "No. This study is dominated by obstructive physiology: OAHI 12.9/h versus CAI 1.3/h, with the important gas-exchange disturbance occurring during obstructive clusters. The presence of some central events should be reported but does not replace the dominant obstructive interpretation.",
            "A common learning error is binary thinking: 'central events exist, therefore CSA.' PSG interpretation asks whether central events are frequent, physiologically important, patterned, and clinically coherent enough to define the disorder rather than simply coexist with obstruction.",
            "What additional features would make the central component more concerning?",
            "A substantially higher central burden, prolonged or repetitive clinically significant central events, important desaturation/bradycardia where applicable, periodic breathing or other characteristic patterning, hypoventilation, neurologic/cardiopulmonary context, medication exposure, or persistent central abnormalities after the obstructive problem is addressed would all increase concern.",
            "Keep obstructive and central indices separate in the final read. Combining them into one headline AHI can obscure which physiology is actually driving treatment.",
            "Give the final one-sentence impression for this study.",
            "Predominantly obstructive pediatric sleep apnea with scattered central events that are not the dominant respiratory abnormality; correlate the central component with age, event morphology, and clinical context rather than labeling the study central by presence alone.",
            "This is the case that prevents the common mistake of equating any nonzero CAI with central sleep apnea syndrome.",
        ),
        _case(
            "psg-systematic-read", 5, "Case 8 · Full sleep-study sign-out",
            "lab_assets/adult_psg_moderate.svg",
            [
                ["Patient", "12-year-old with obesity and persistent snoring after prior adenotonsillectomy"],
                ["TST", "376 min; adequate REM and supine sleep"], ["AHI", "16.8/h"], ["OAHI", "15.9/h"], ["CAI", "0.9/h"],
                ["SpO₂ nadir", "82%"], ["CO₂", "Intermittently elevated, no sustained hypoventilation pattern in this teaching case"],
                ["Distribution", "REM > NREM; supine > lateral"],
            ],
            "Sign this study out from top to bottom. What sequence keeps you from anchoring on the AHI and missing study adequacy, event type, or gas exchange?",
            "A disciplined read is: (1) verify study quality and sleep opportunity, (2) review sleep architecture/REM and position sampling, (3) classify respiratory event morphology using airflow plus effort, (4) separate obstructive and central indices, (5) assess oxygenation and CO₂, (6) examine stage/position clustering and arousal burden, then (7) integrate anatomy, comorbidity, prior treatment, and the management question. Here the dominant finding is residual obstructive sleep apnea after adenotonsillectomy, not central apnea.",
            "A reproducible sequence prevents the headline index from becoming the diagnosis. It also makes the study actionable for ENT: persistent obstruction after surgery has a different next-step pathway from a central ventilatory disorder.",
            "What are your next localization questions in persistent pediatric OSA after adenotonsillectomy?",
            "Reassess nasal obstruction, adenoid regrowth when relevant, tongue base/lingual tonsils, craniofacial restriction, obesity-related collapsibility, and other sites or conditions suggested by exam. In selected patients, DISE or other targeted evaluation can help localize persistent collapse.",
            "Management depends on phenotype and severity: weight management where relevant, PAP, medical therapy for selected nasal disease, further airway evaluation/surgery in selected patients, and sleep-medicine involvement when physiology is complex.",
            "Teach your entire PSG reading algorithm in under 30 seconds.",
            "Quality and sampling first; then airflow plus effort to classify events; separate obstructive from central burden; check oxygen and CO₂; ask when events cluster by REM and position; finally connect the physiology to airway anatomy, comorbidity, prior treatment, and what decision the study needs to answer.",
            "If a trainee uses that sequence consistently, central-versus-obstructive discrimination becomes a signal-reading task rather than memorization.",
        ),
    ]


def _psg_lab():
    cases = _psg_cases()
    return {
        "title": "PSG / Sleep Study Interpretation Lab",
        "icon": "☾",
        "subtitle": "Work real-world synthetic PSG cases from signals → event type → indices → gas exchange → clinical interpretation.",
        "framework": [
            "Check study quality, total sleep time, REM and position sampling",
            "Read airflow and thoracoabdominal effort together",
            "Classify obstructive, central and mixed events before using the headline AHI",
            "Separate OAHI and CAI; then assess oxygenation and CO₂",
            "Look for REM/position clustering, arousals and hypoventilation",
            "State the dominant physiology and what it changes for the patient",
        ],
        "source_note": "Synthetic teaching cases based on standard polysomnographic signal logic and pediatric respiratory-event scoring principles. Use the current AASM scoring manual and local sleep-lab standards for formal clinical scoring.",
        "tracks": [
            {"id": "core", "name": "Core PSG cases"},
        ],
        "practice_update": "Do not diagnose central sleep apnea from a nonzero CAI alone. First verify event morphology (effort absent), frequency/pattern, physiologic consequence, and whether central events are actually the dominant abnormality.",
        "seed_case_count": len(cases),
        "cases": cases,
        "resources": [],
    }


def rebuild_interpretation_labs_v250(existing):
    """Return a new registry with retired labs/resources removed and PSG rebuilt."""
    clean = {}
    psg_slug = None

    for slug, original in (existing or {}).items():
        lab = deepcopy(original or {})
        if _retired_lab(str(slug), lab):
            continue

        text = _norm(" ".join([str(slug), lab.get("title", ""), lab.get("subtitle", "")]))
        if psg_slug is None and ("polysomnog" in text or " psg " in f" {text} " or "sleep study" in text):
            psg_slug = str(slug)
            continue

        resources = lab.get("resources") or []
        lab["resources"] = [r for r in resources if not _is_open_anatomy_spl(r or {})]
        clean[str(slug)] = lab

    # Preserve an existing public PSG URL if one existed; otherwise use a stable slug.
    clean[psg_slug or "psg-sleep"] = _psg_lab()
    return clean


def apply_interpretation_labs_cleanup_v250(data_module, app_module=None):
    rebuilt = rebuild_interpretation_labs_v250(getattr(data_module, "INTERPRETATION_LABS", {}))
    current = getattr(data_module, "INTERPRETATION_LABS", None)
    if isinstance(current, dict):
        current.clear()
        current.update(rebuilt)
    else:
        data_module.INTERPRETATION_LABS = rebuilt
    if app_module is not None:
        app_module.INTERPRETATION_LABS = data_module.INTERPRETATION_LABS
    return {
        "labs": len(data_module.INTERPRETATION_LABS),
        "psg_slug": next((s for s, l in data_module.INTERPRETATION_LABS.items() if l.get("title") == "PSG / Sleep Study Interpretation Lab"), None),
        "psg_cases": len(_psg_cases()),
    }
