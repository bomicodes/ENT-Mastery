"""v53.0 Interpretation Atlas repairs.

1. Draws the studies cases ask learners to read (audiograms, tympanograms,
   vHIT, calorics, ABR) via lab_figures_v530.
2. Folds the generic "Reason backward…" / "Teach this case…" copies back into
   the Reason and Teach stages of the case they came from, so a lab no longer
   lists one study three times.
3. Moves recall-only items ("What does stroboscopy assess?") out of the case
   list into a Fundamentals panel on the same page.
4. Gives the allergy cases difficulty levels so the L1–L5 filter works.
5. Replaces the third-party CT slice-viewer link with Radiopaedia's annotated
   scrollable neck CT (rID 74853).
"""
import re
from lab_figures_v530 import figures_for

ALLERGY_LEVELS = {"allergy1": 1, "allergy2": 2, "allergy3": 2, "allergy4": 2,
                  "allergy5": 3, "allergy6": 3, "allergy7": 3, "allergy8": 4}
RADIOPAEDIA_NECK_CT = "https://radiopaedia.org/cases/74853"

_FUND_RE = re.compile(
    r"^(what (does|do|are|is|can|makes|changes)|how (is|should|are)|compare |match |distinguish |"
    r"when should|why does|give a systematic|interpret jerger)", re.I)


def _is_fundamental(c):
    if c.get("study_summary") or c.get("image_url") or c.get("visual") or c.get("external"):
        return False
    if c.get("id", "") in {"audfund9", "audfund10"}:
        return True
    return bool(_FUND_RE.match(c.get("prompt", "").strip()))


def install_interpretation_atlas_v530(data):
    labs = data.INTERPRETATION_LABS
    report = {"folded": 0, "fundamentals": 0, "figures": 0, "levels_set": 0, "per_lab": {}}
    for slug, lab in labs.items():
        cases = lab.get("cases", [])
        by_id = {c.get("id"): c for c in cases}
        kept, folded = [], 0
        for c in cases:
            vt = c.get("variant_type")
            cid = c.get("id", "")
            if vt in ("reason", "teach") and cid.endswith("_" + vt):
                base = by_id.get(cid[: -len(vt) - 1])
                if base is not None:
                    if vt == "reason" and not base.get("reason_prompt"):
                        base["reason_prompt"] = c.get("prompt")
                        base["reason_answer"] = " ".join(x for x in (c.get("answer"), c.get("why")) if x)
                    if vt == "teach" and not base.get("teach_prompt"):
                        base["teach_prompt"] = c.get("prompt")
                        base["teach_answer"] = c.get("answer")
                        if c.get("follow_answer") and not base.get("teach_follow_answer"):
                            base["teach_follow_answer"] = c.get("follow_answer")
                    folded += 1
                    continue
            kept.append(c)

        fundamentals = [c for c in kept if _is_fundamental(c)]
        studies = [c for c in kept if not _is_fundamental(c)]

        for c in studies:
            if slug == "allergy-testing" and c.get("level") is None and c.get("id") in ALLERGY_LEVELS:
                c["level"] = ALLERGY_LEVELS[c["id"]]
                report["levels_set"] += 1
            if c.get("external", "").find("chatgpt.site") >= 0:
                c["external"] = RADIOPAEDIA_NECK_CT
                c["prompt"] = ("Open Radiopaedia's annotated scrollable neck CT. Scroll one axial series top to bottom "
                               "with labels hidden and name each major structure before checking the labels.")
            figs = figures_for(c.get("id"))
            if figs:
                c["figures"] = figs
                report["figures"] += len(figs)

        lab["cases"] = studies
        lab["fundamentals"] = fundamentals
        lab["seed_case_count"] = len(studies)
        report["folded"] += folded
        report["fundamentals"] += len(fundamentals)
        report["per_lab"][slug] = {"studies": len(studies), "fundamentals": len(fundamentals), "folded": folded}
    data.INTERPRETATION_ATLAS_V530 = report
    return report
