"""v47.0 Daily Path rebuild: teach each topic from foundation to mastery.

Scraps the stage-template prompts ("How would you build a practical map of X...")
that were generated from the Recognize/Localize/... slots.  A Daily Path session is
now a list of topic lessons and spaced reviews built from real authored material:

  Lesson (new or resumed topic)
    1. Learn       -- why it matters, normal physiology, pathophysiology (the new
                      textbook sections), with key clinical points one tap away.
    2. Foundation  -- concept-check MCQs + foundation-level board vignettes.
    3. Application -- application-level board vignettes.
    4. Mastery     -- senior-decision vignettes, a teach-back, and links to the
                      topic's progressive case(s) and OR card(s).
  Review (mastered topic that is due)
    3 mixed board vignettes from the topic.

Progress uses the existing per-user ``curriculum_mastery`` table (levels 0-6):
foundation passed = 2, application passed = 4, mastered = 6, with the existing
spaced-review intervals.  Every answer is also written to ``attempts`` (Mistakes
page / spaced repetition) and ``mastery_events`` (unified mastery profile).
"""
from __future__ import annotations

import random
import re
from datetime import date

PHASES_V470 = [
    # key, label, level awarded, legacy stage name (for the unified dimension map)
    ("foundation", "Foundation", 2, "recognize"),
    ("application", "Application", 4, "manage"),
    ("mastery", "Mastery", 6, "operate"),
]
PHASE_LEVEL = {k: lvl for k, _, lvl, _ in PHASES_V470}
PHASE_STAGE = {k: st for k, _, _, st in PHASES_V470}
PHASE_GOALS = {
    "foundation": "Can you recognize it and explain the mechanism? Concept checks and foundation-level vignettes.",
    "application": "Can you work it up and manage it? Board vignettes that apply the concept to a patient.",
    "mastery": "Can you make the senior decision and teach it? Chief-level vignettes, a teach-back, and the OR/case connection.",
}
_FOUNDATION_WORDS = re.compile(
    r"anatomy|physiology|neuroanatomy|interpretation|audiogram|tympanometry|test battery|"
    r"electrophysiology|fundamentals|framework|imaging|examination|principles|\bpsg\b|"
    r"stroboscopy|\bfees\b|barium|analysis|biomechanics|phenotyping|assessment|testing|"
    r"monitoring|foundations|healing|stewardship|triage", re.I)
LESSON_MIN, REVIEW_MIN = 15, 4


def _classify(q):
    stage = q.get("learning_stage")
    if stage == "foundation":
        return "foundation"
    if stage in ("senior_decision", "mastery"):
        return "mastery"
    if stage == "application":
        return "application"
    tier = (q.get("tier") or "").lower()
    if "chief" in tier or "call/or" in tier or "second-pass" in tier:
        return "mastery"
    if (q.get("mode") or "") == "Clinical discrimination":
        return "foundation"
    return "application"


def _mcq(q, kind):
    choices = q.get("choices") or []
    if not isinstance(choices, list) or len(choices) < 2:
        return None
    try:
        answer = int(q.get("answer"))
    except (TypeError, ValueError):
        return None
    if not 0 <= answer < len(choices):
        return None
    why = q.get("why_wrong") if isinstance(q.get("why_wrong"), list) else []
    return {
        "id": q.get("id"), "kind": kind,
        "stem": q.get("stem") or q.get("prompt") or "",
        "choices": list(choices), "answer": answer,
        "explanation": q.get("explanation") or "",
        "why_wrong": [str(w) for w in why] if len(why) == len(choices) else [],
        "pearl": q.get("board_pearl") or "",
    }


def install_learning_path_v470(data, app_mod, app):
    from flask import jsonify, render_template, request
    import db

    item_id = app_mod._v6_item_id
    topics = []           # (domain, module, cid) in curriculum order
    by_cid = {}
    for dname, mods in data.DEEP_MODULES_V6.items():
        ordered = sorted(enumerate(mods), key=lambda p: (0 if _FOUNDATION_WORDS.search(p[1]["topic"]) else 1, p[0]))
        for _, m in ordered:
            cid = item_id(dname, m["topic"])
            topics.append((dname, m, cid))
            by_cid[cid] = (dname, m)
    domains = list(data.DEEP_MODULES_V6.keys())
    topic_by_name = {m["topic"]: cid for _, m, cid in topics}

    bank = {}
    for q in data.CLINICAL_CHALLENGES_V119:
        cid = q.get("concept_id")
        if cid in by_cid:
            kind = _classify(q)
            mcq = _mcq(q, kind)
            if mcq:
                bank.setdefault(cid, {"foundation": [], "application": [], "mastery": [], "checks": []})[kind].append(mcq)
    for q in data.CONCEPT_CHECKS_V112:
        cid = q.get("concept_id")
        mcq = _mcq(q, "check") if cid in by_cid else None
        # Skip the auto-generated template checks ("Based on the current curriculum
        # framework, which management principle...") whose distractors are truncated
        # answers borrowed from other topics -- the guess-what-I'm-thinking problem.
        if mcq and (re.search(r"curriculum framework", mcq["stem"], re.I)
                    or any(str(ch).rstrip().endswith(("...", "\u2026", ";")) for ch in mcq["choices"])):
            mcq = None
        if mcq and mcq["stem"]:
            bank.setdefault(cid, {"foundation": [], "application": [], "mastery": [], "checks": []})["checks"].append(mcq)

    def phase_questions(cid, phase):
        b = bank.get(cid) or {}
        if phase == "foundation":
            qs = b.get("checks", [])[:1] + b.get("foundation", [])[:3]
            if len(qs) < 2:
                qs += b.get("application", [])[3:5 - len(qs)]
        elif phase == "application":
            qs = b.get("application", [])[:3]
            if not qs:
                qs = b.get("foundation", [])[2:4] or b.get("mastery", [])[:1]
        else:
            qs = b.get("mastery", [])[:2]
            if not qs:
                qs = b.get("application", [])[3:5]
        return qs

    def review_questions(cid, level):
        b = bank.get(cid) or {}
        pool = b.get("foundation", []) + b.get("application", []) + (b.get("mastery", []) if level >= 4 else []) + b.get("checks", [])
        rnd = random.Random("%s-%s" % (cid, date.today().isoformat()))
        rnd.shuffle(pool)
        return pool[:3]

    def norm_level(level):
        level = int(level or 0)
        return level - 1 if level % 2 else level   # legacy odd levels resume at the phase below

    def lesson(cid, level, reason):
        dname, m = by_cid[cid]
        phases = []
        for key, label, lvl, _ in PHASES_V470:
            phases.append({"key": key, "label": label, "goal": PHASE_GOALS[key], "done": level >= lvl,
                           "questions": phase_questions(cid, key)})
        return {"type": "lesson", "cid": cid, "domain": dname, "module": m, "topic": m["topic"], "level": level,
                "reason": reason, "phases": phases,
                "cases": data.textbook_cases_for_v470(cid, m["topic"]),
                "ors": data.textbook_or_cards_for_v470(m["topic"]),
                "qtotal": len(data.textbook_questions_for_v470(cid))}

    def review(cid, level, reason):
        dname, m = by_cid[cid]
        return {"type": "review", "cid": cid, "domain": dname, "module": m, "topic": m["topic"], "level": level,
                "reason": reason, "questions": review_questions(cid, level)}

    def mastery_map():
        try:
            return db.adaptive_mastery_map()
        except Exception:
            app.logger.exception("Daily Path mastery map failed")
            return {}

    def build_session(minutes, focus, topic_cid):
        state = mastery_map()
        today = date.today()
        canon = data.canonical_domain_v94
        in_focus = (lambda d: canon(d) == canon(focus)) if focus else (lambda d: True)
        level_of = lambda cid: norm_level((state.get(cid) or {}).get("mastery_level"))
        items, used, chosen = [], 0, set()

        if topic_cid in by_cid:
            items.append(lesson(topic_cid, level_of(topic_cid) if level_of(topic_cid) < 6 else 0, "You picked this topic"))
            used += LESSON_MIN
            chosen.add(topic_cid)

        due = []
        for cid, st in state.items():
            if cid in chosen or cid not in by_cid or not in_focus(by_cid[cid][0]):
                continue
            nd, lvl = st.get("next_due"), level_of(cid)
            if lvl > 0 and nd and nd <= today:
                due.append((nd, cid, lvl))
        due.sort()
        review_budget = max(REVIEW_MIN, minutes // 2)
        for nd, cid, lvl in due:
            cost = REVIEW_MIN if lvl >= 6 else LESSON_MIN - 5
            if used + cost > review_budget + (LESSON_MIN if topic_cid else 0):
                break
            items.append(review(cid, lvl, "Spaced review — due %s" % nd.isoformat()) if lvl >= 6
                         else lesson(cid, lvl, "Resume — you passed %s" % ("Foundation" if lvl < 4 else "Application")))
            used += cost
            chosen.add(cid)

        def started(cid):
            return level_of(cid) > 0 or cid in chosen

        prereq = getattr(data, "PREREQUISITES_SUGGESTED_V114", {}) or {}
        while not topic_cid and (used + LESSON_MIN <= minutes + 5
                                 or not any(i["type"] == "lesson" for i in items)):
            pool = [(d, m, c) for d, m, c in topics if in_focus(d) and not started(c)]
            if not pool:
                break
            if focus:
                pick = pool[0]
            else:
                counts = {d: 0 for d in domains}
                totals = {d: 0 for d in domains}
                for d, m, c in topics:
                    totals[d] += 1
                    counts[d] += 1 if started(c) else 0
                open_domains = {d for d, _, _ in pool}
                best = min(open_domains, key=lambda d: (counts[d] / max(1, totals[d]), domains.index(d)))
                pick = next(p for p in pool if p[0] == best)
            # Learn an unstarted prerequisite first when one exists.
            for pre in prereq.get(pick[1]["topic"], []):
                pc = topic_by_name.get(pre)
                if pc and not started(pc) and pc in by_cid:
                    pick = (by_cid[pc][0], by_cid[pc][1], pc)
                    break
            items.append(lesson(pick[2], 0, "New topic — next in your curriculum"))
            chosen.add(pick[2])
            used += LESSON_MIN
        return items, used, state

    def progress_summary(state):
        rows = []
        for d in domains:
            cids = [c for dd, _, c in topics if dd == d]
            lv = [norm_level((state.get(c) or {}).get("mastery_level")) for c in cids]
            rows.append({"domain": d, "total": len(cids), "started": sum(1 for x in lv if x > 0),
                         "mastered": sum(1 for x in lv if x >= 6)})
        return rows

    def daily_adaptive():
        focus = request.args.get("focus") or None
        topic_cid = request.args.get("topic") or request.args.get("concept") or None
        if topic_cid and topic_cid not in by_cid:
            topic_cid = topic_by_name.get(topic_cid)
        try:
            minutes = int(request.args.get("minutes", "30"))
        except (TypeError, ValueError):
            minutes = 30
        minutes = max(15, min(60, minutes))
        items, used, state = build_session(minutes, focus, topic_cid)
        prog = progress_summary(state)
        return render_template("daily_path_v470.html", items=items, minutes=minutes, total=used,
                               focus=focus, domains=domains, progress=prog,
                               topic_names=[m["topic"] for _, m, _ in topics],
                               overall={"total": sum(r["total"] for r in prog),
                                        "started": sum(r["started"] for r in prog),
                                        "mastered": sum(r["mastered"] for r in prog)})

    q_index = {}
    for cid, b in bank.items():
        for kind, qs in b.items():
            for q in qs:
                q_index[q["id"]] = (cid, q)

    def answer():
        payload = request.get_json(silent=True) or {}
        hit = q_index.get(str(payload.get("qid", "")))
        if not hit:
            return jsonify({"ok": False, "error": "unknown question"}), 404
        cid, q = hit
        try:
            chosen = int(payload.get("chosen", -1))
        except (TypeError, ValueError):
            chosen = -1
        correct = chosen == q["answer"]
        dname = by_cid[cid][0]
        try:
            db.record_attempt(q["id"], cid, correct, 3, None if correct else "discrimination")
        except Exception:
            app.logger.exception("Daily Path attempt save failed")
        try:
            app_mod.record_mastery_event(cid, dname, "reasoning", 3 if correct else 0,
                                         source_type="daily_path_v470", source_id=q["id"],
                                         miss_type=None if correct else "discrimination")
        except Exception:
            app.logger.exception("Daily Path mastery event failed")
        return jsonify({"ok": True, "correct": correct, "answer": q["answer"]})

    def phase_done():
        payload = request.get_json(silent=True) or {}
        cid = payload.get("cid")
        phase = payload.get("phase")
        if cid not in by_cid or (phase not in PHASE_LEVEL and phase != "review"):
            return jsonify({"ok": False, "error": "bad phase"}), 400
        try:
            correct = max(0, int(payload.get("correct", 0)))
            total = max(1, int(payload.get("total", 1)))
        except (TypeError, ValueError):
            return jsonify({"ok": False, "error": "bad score"}), 400
        correct = min(correct, total)
        if correct == total:
            rating = 3
        elif total >= 3 and correct >= total - 1:
            rating = 2
        else:
            rating = 0
        dname, m = by_cid[cid]
        if phase == "review":
            level = max(2, norm_level((mastery_map().get(cid) or {}).get("mastery_level")))
            stage = "teach"
        else:
            level, stage = PHASE_LEVEL[phase], PHASE_STAGE[phase]
        intervals = getattr(data, "REVIEW_INTERVALS_V6", {}) or {}
        try:
            new_level = db.record_adaptive_result(cid, "v470-" + phase, dname, m["topic"], stage, level, rating,
                                                  intervals.get(level, 7))
            due = (mastery_map().get(cid) or {}).get("next_due")
        except Exception:
            app.logger.exception("Daily Path phase save failed")
            return jsonify({"ok": False, "error": "Could not save progress. Please retry."}), 500
        return jsonify({"ok": True, "passed": rating >= 2, "level": new_level,
                        "next_due": due.isoformat() if hasattr(due, "isoformat") else due})

    app.view_functions["daily_adaptive"] = daily_adaptive
    if "daily_path_answer_v470" not in app.view_functions:
        try:
            app.add_url_rule("/daily-path/answer", "daily_path_answer_v470", answer, methods=["POST"])
            app.add_url_rule("/daily-path/phase", "daily_path_phase_v470", phase_done, methods=["POST"])
        except AssertionError:
            # Only happens when an audit imports this module into an app object that
            # has already served requests; production installs before first request.
            app.logger.warning("Daily Path v47 answer routes not registered (app already serving)")
    else:
        app.view_functions["daily_path_answer_v470"] = answer
        app.view_functions["daily_path_phase_v470"] = phase_done

    stats = {"topics": len(topics),
             "topics_with_all_phases": sum(1 for _, _, c in topics if all(phase_questions(c, k) for k, *_ in PHASES_V470)),
             "questions_indexed": len(q_index)}
    data.LEARNING_PATH_V470 = stats
    data.learning_path_build_session_v470 = build_session
    return stats
