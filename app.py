from flask import Flask, render_template, request, redirect, url_for, jsonify
import os, random, re
from data import *
from db import init_db, record_attempt, stats, mistake_rows, concept_strengths, record_lab_attempt, lab_progress, lab_stats, record_mastery_event, mastery_profiles, dimension_summary, domain_mastery, mastery_misses

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-ent-mastery-change-me")
init_db()

@app.context_processor
def inject():
    return {"DOMAINS": DOMAINS}

@app.route("/")
def dashboard():
    st = stats()
    strengths = concept_strengths()
    weak = sorted(strengths.items(), key=lambda x: x[1].get("strength",0))[:4]
    profiles=mastery_profiles()
    dsum=dimension_summary()
    domains=domain_mastery()
    weakest_dims=sorted(dsum.items(), key=lambda x:x[1])[:3]
    return render_template("dashboard.html", stats=st, weak=weak, topic=PARATHYROID,
                           dimension_summary=dsum, domain_mastery=domains,
                           weakest_dimensions=weakest_dims,
                           integrated_cases=INTEGRATED_CASES)

@app.route("/today")
def today():
    mins=max(10,min(45,int(request.args.get("minutes",20))))
    strengths=concept_strengths(); profiles=mastery_profiles()
    qs=sorted(QUESTIONS,key=lambda q:(strengths.get(q["concept_id"],{}).get("strength",0),random.random()))
    q_count={10:3,20:4,30:6,45:8}.get(mins,4)
    def case_score(c):
        p=profiles.get(c["concept_id"])
        return (p["overall"] if p else -1, random.random())
    integrated=sorted(INTEGRATED_CASES,key=case_score)[0]
    dims=dimension_summary()
    weak_dim=min(dims,key=dims.get) if dims else "reasoning"
    prompt_pool=ATTENDING_LEVEL_PROMPTS["resident"] + ATTENDING_LEVEL_PROMPTS["senior"]
    attending_prompt=random.choice(prompt_pool)
    plan={"recall_count":q_count,"integrated_case":integrated,"weak_dimension":weak_dim,"attending_prompt":attending_prompt}
    return render_template("today.html", minutes=mins, questions=qs[:q_count], topic=PARATHYROID, plan=plan, dimension_summary=dims)

@app.route("/learn")
def learn():
    return render_template("learn.html", topic=PARATHYROID)

@app.route("/topic/<slug>")
def topic(slug):
    if slug != PARATHYROID["slug"]: return redirect(url_for("learn"))
    return render_template("topic.html", topic=PARATHYROID)

@app.route("/search")
def search():
    q = request.args.get("q","").strip().lower()
    rows = search_index()
    if q:
        terms = [x for x in re.split(r"\s+",q) if x]
        scored=[]
        for r in rows:
            hay=(r["title"]+" "+r["subtitle"]+" "+r["text"]).lower()
            score=sum(3 if t in r["title"].lower() else 1 for t in terms if t in hay)
            if score: scored.append((score,r))
        rows=[r for _,r in sorted(scored,key=lambda x:-x[0])]
    else: rows=[]
    return render_template("search.html", q=q, results=rows)

@app.route("/case-tomorrow")
def case_tomorrow():
    q=request.args.get("q","").strip().lower()
    prep=None
    if q:
        for slug,x in OR_PREP_REGISTRY.items():
            hay=(slug+" "+x["title"]).lower()
            if q in hay or any(t in hay for t in q.split()):
                prep=x; break
    if not prep and q:
        matches=[]
        for r in search_index():
            hay=(r["title"]+" "+r.get("subtitle","")+" "+r.get("text","")).lower()
            if any(t in hay for t in q.split()): matches.append(r)
        return render_template("case_tomorrow.html", q=q, prep=None, matches=matches[:8], questions=[])
    if not prep: prep=OR_PREP_REGISTRY.get("parathyroidectomy")
    linked_q=[x for x in QUESTIONS if x.get("topic")==prep.get("linked_topic")][:5] if prep else []
    return render_template("case_tomorrow.html", q=q, prep=prep, matches=[], questions=linked_q)

@app.route("/questions")
def questions():
    kind = request.args.get("kind")
    concept = request.args.get("concept")
    qs = [
        q for q in QUESTIONS
        if (not kind or q["kind"] == kind)
        and (not concept or q["concept_id"] == concept)
    ]
    title = "Question Bank"
    if concept:
        title = f"Review: {concept.replace('_', ' ').title()}"
    return render_template("questions.html", questions=qs, title=title, active_concept=concept)

@app.route("/api/answer", methods=["POST"])
def answer():
    d=request.get_json(force=True)
    q=next((x for x in QUESTIONS if x["id"]==d.get("question_id")),None)
    if not q: return jsonify({"error":"not found"}),404
    choice=int(d.get("choice",-1))
    correct=choice==q["answer"]
    record_attempt(q["id"],q["concept_id"],correct,int(d.get("confidence",3)),d.get("miss_type"))
    return jsonify({
        "correct": correct,
        "answer": q["answer"],
        "explanation": q["explanation"],
        "why_wrong": q["why_wrong"],
        "why_it_matters": q.get("why_it_matters"),
        "what_to_look_for": q.get("what_to_look_for"),
        "management_change": q.get("management_change"),
        "board_pearl": q.get("board_pearl"),
        "attending_followup": q.get("attending_followup")
    })

@app.route("/api/classify-miss", methods=["POST"])
def classify_miss():
    # Classification is intentionally separate from scoring so one missed
    # question produces one attempt, not a duplicate miss.
    d=request.get_json(force=True)
    from db import conn
    c=conn()
    row=c.execute("SELECT id FROM attempts WHERE question_id=? AND correct=0 ORDER BY id DESC LIMIT 1",
                  (d.get("question_id"),)).fetchone()
    if row:
        c.execute("UPDATE attempts SET miss_type=? WHERE id=?", (d.get("miss_type"), row["id"]))
        c.commit()
    c.close()
    return jsonify({"ok": True})


@app.route("/integrated")
def integrated_index():
    return render_template("integrated_index.html", cases=INTEGRATED_CASES, profiles=mastery_profiles())

@app.route("/integrated/<case_id>")
def integrated_case(case_id):
    c=get_integrated_case(case_id)
    if not c: return redirect(url_for("integrated_index"))
    return render_template("integrated_case.html", case=c)

@app.route("/api/mastery-event", methods=["POST"])
def mastery_event():
    d=request.get_json(force=True); cid=d.get("concept_id"); dim=d.get("dimension")
    if not cid or not dim: return jsonify({"error":"concept_id and dimension required"}),400
    try: score=int(d.get("score",0))
    except Exception: score=0
    if score not in (0,1,2,3): return jsonify({"error":"score must be 0-3"}),400
    record_mastery_event(cid,d.get("domain","ENT"),dim,score,d.get("source_type"),d.get("source_id"),d.get("miss_type"))
    return jsonify({"ok":True,"profile":mastery_profiles().get(cid,{})})

@app.route("/api/mastery-miss", methods=["POST"])
def mastery_miss():
    d=request.get_json(force=True); cid=d.get("concept_id"); miss=d.get("miss_type")
    if not cid or not miss: return jsonify({"error":"missing fields"}),400
    record_mastery_event(cid,d.get("domain","ENT"),d.get("dimension","reasoning"),1,d.get("source_type"),d.get("source_id"),miss)
    return jsonify({"ok":True})

@app.route("/cases")
def cases():
    return render_template("cases.html", cases=CASES)

@app.route("/case/<cid>")
def case(cid):
    c=next((x for x in CASES if x["id"]==cid),None)
    if not c: return redirect(url_for("cases"))
    return render_template("case.html", case=c)

@app.route("/operate")
def operate():
    return render_template("operate_index.html", operations=OPERATIONS)

@app.route("/operate/<slug>")
def operation(slug):
    op=next((x for x in OPERATIONS if x["slug"]==slug),None)
    if not op: return redirect(url_for("operate"))
    return render_template("operation.html", op=op)

@app.route("/anatomy")
def anatomy():
    return render_template("anatomy.html", anatomy=ANATOMY)

@app.route("/complications")
def complications():
    return render_template("complications.html", complications=COMPLICATIONS)



def _adaptive_lab_session(slug, cases, count=7):
    """Prefer weak -> unseen -> older/less-practiced, while preserving variety."""
    progress=lab_progress(slug)
    def score(c):
        p=progress.get(c.get("id"), {})
        attempts=p.get("attempts",0)
        rating=p.get("last_rating")
        # Lower score is shown sooner.
        if rating is not None and rating <= 1: bucket=0
        elif attempts == 0: bucket=1
        elif rating == 2: bucket=2
        else: bucket=3
        return (bucket, attempts, random.random())
    ranked=sorted(cases,key=score)
    # Avoid showing multiple variants of the same seed in one session when possible.
    picked=[]; concepts=set()
    for c in ranked:
        concept=c.get("concept_id",c.get("id"))
        if concept in concepts: continue
        picked.append(c); concepts.add(concept)
        if len(picked)>=count: break
    if len(picked)<count:
        for c in ranked:
            if c not in picked:
                picked.append(c)
                if len(picked)>=count: break
    return picked

@app.route("/lab")
def lab():
    return render_template("lab.html", labs=INTERPRETATION_LABS)

@app.route("/lab/<slug>")
def interpretation_lab(slug):
    if slug == "otoscopy":
        return redirect(url_for("otoscopy_lab"))
    lab_data = INTERPRETATION_LABS.get(slug)
    if not lab_data:
        return redirect(url_for("lab"))
    level = request.args.get("level", "all")
    track = request.args.get("track", "all")
    cases = lab_data.get("cases", [])
    if track != "all":
        cases = [c for c in cases if c.get("track", "all") == track]
    if level != "all":
        cases = [c for c in cases if str(c.get("level")) == str(level)]
    mode = request.args.get("mode", "session")
    session_size = max(3, min(12, int(request.args.get("count", 7))))
    if mode == "session":
        cases = _adaptive_lab_session(slug, cases, session_size)
    return render_template(
        "interpretation_lab.html", lab=lab_data, slug=slug, cases=cases,
        level=level, track=track, mode=mode, session_size=session_size,
        lab_stats=lab_stats(slug), bank_size=len(lab_data.get("cases", [])),
        seed_count=lab_data.get("seed_case_count", len(lab_data.get("cases", [])))
    )

@app.route("/lab/otoscopy")
def otoscopy_lab():
    level = request.args.get("level", "all")
    cases = OTOSCOPY_CASES
    if level != "all":
        cases = [c for c in cases if str(c.get("level")) == str(level)]
    return render_template("otoscopy_lab.html", cases=cases, level=level)



@app.route("/api/lab-rate", methods=["POST"])
def lab_rate():
    d=request.get_json(force=True)
    slug=d.get("lab_slug","")
    case_id=d.get("case_id","")
    concept_id=d.get("concept_id") or case_id
    try: rating=int(d.get("rating",2))
    except Exception: rating=2
    if not slug or not case_id or rating not in (0,1,2,3):
        return jsonify({"error":"invalid lab rating"}),400
    record_lab_attempt(slug,case_id,concept_id,rating)
    variant=d.get("variant_type","interpret")
    dimension={"interpret":"recognition","reason":"reasoning","teach":"teaching"}.get(variant,"recognition")
    record_mastery_event(concept_id,d.get("domain",slug),dimension,rating,"interpretation_lab",case_id,d.get("miss_type"))
    return jsonify({"ok":True,"stats":lab_stats(slug)})

@app.route("/attending")
def attending():
    level=request.args.get("level","resident")
    if level not in ATTENDING_LEVEL_PROMPTS: level="resident"
    domain=request.args.get("domain","all")
    prompts=ATTENDING_LEVEL_PROMPTS[level]
    if domain!="all": prompts=[p for p in prompts if p.get("domain")==domain]
    return render_template("attending.html", prompts=prompts, level=level, levels=ATTENDING_LEVELS, domain=domain)

@app.route("/chief")
def chief():
    return render_template("chief.html", prompts=CHIEF_PROMPTS)

@app.route("/mistakes")
def mistakes():
    rows=mistake_rows()
    byid={q["id"]:q for q in QUESTIONS}
    data=[{"row":dict(r),"q":byid.get(r["question_id"])} for r in rows if byid.get(r["question_id"])]
    return render_template("mistakes.html", mistakes=data)



@app.route("/curriculum")
def curriculum():
    from data import CURRICULUM_V5, PREREQUISITES_V5, SPIRAL_LEVELS_V5
    return render_template("curriculum.html", curriculum=CURRICULUM_V5, prerequisites=PREREQUISITES_V5, spiral=SPIRAL_LEVELS_V5)

@app.route("/evidence")
def evidence():
    sources=[
      {"area":"Otology / Audiology","title":"Sudden Hearing Loss (Update)","year":"2019","kind":"AAO-HNSF CPG","status":"current reviewed source"},
      {"area":"Vestibular","title":"Ménière’s Disease","year":"2020","kind":"AAO-HNSF CPG","status":"current reviewed source"},
      {"area":"Vestibular","title":"BPPV (Update)","year":"2017","kind":"AAO-HNSF CPG","status":"current reviewed source"},
      {"area":"Pediatric Otolaryngology","title":"Tympanostomy Tubes in Children (Update)","year":"2022","kind":"AAO-HNSF CPG","status":"current reviewed source"},
      {"area":"Pediatric Otolaryngology / Sleep","title":"Tonsillectomy in Children (Update)","year":"2019","kind":"AAO-HNSF CPG","status":"current reviewed source"},
      {"area":"Head & Neck Oncology","title":"Evaluation of the Neck Mass in Adults","year":"2017","kind":"AAO-HNSF CPG","status":"current reviewed source"},
      {"area":"Laryngology","title":"Hoarseness (Dysphonia) Update","year":"2018","kind":"AAO-HNSF CPG","status":"current reviewed source"},
      {"area":"Rhinology","title":"Nosebleed (Epistaxis)","year":"2020","kind":"AAO-HNSF CPG","status":"current reviewed source"},
      {"area":"Rhinology","title":"Adult Sinusitis Update","year":"2025","kind":"AAO-HNSF CPG","status":"current reviewed source"},
      {"area":"Rhinology","title":"Surgical Management of Chronic Rhinosinusitis","year":"2025","kind":"AAO-HNSF CPG","status":"current reviewed source"},
      {"area":"Audiology","title":"Age-Related Hearing Loss","year":"2024","kind":"AAO-HNSF CPG","status":"current reviewed source"},
      {"area":"Thyroid","title":"2025 ATA Differentiated Thyroid Cancer","year":"2025","kind":"ATA Guideline","status":"current reviewed source"},
      {"area":"Rhinology","title":"ICAR-RS: Rhinosinusitis","year":"2021","kind":"International Consensus Statement","status":"core comprehensive rhinology reference; newer CPGs supersede where applicable"},
      {"area":"Otology","title":"Color Atlas of Otoscopy: From Diagnosis to Surgery","year":"1999","kind":"Uploaded atlas","status":"visual/anatomic source; management cross-check required"}
    ]
    return render_template("evidence.html", sources=sources)

@app.route("/progress")
def progress():
    return render_template("progress.html", stats=stats(), strengths=concept_strengths(), profiles=mastery_profiles(), dimensions=dimension_summary(), domains=domain_mastery(), mastery_dimensions=MASTERY_DIMENSIONS)

@app.route("/sources")
def sources():
    return render_template("sources.html", sources=PARATHYROID["sources"])

if __name__ == "__main__":
    app.run(debug=True)


# =============================================================================
# v6 Adaptive Daily Path
# =============================================================================
def _adaptive_plan(target_minutes=30, focus=None):
    from data import ADAPTIVE_ITEMS_V6, REVIEW_INTERVALS_V6
    try:
        from db import adaptive_mastery_map
        mastery=adaptive_mastery_map()
    except Exception:
        mastery={}
    import datetime, random
    today=datetime.date.today()
    concepts={}
    for x in ADAPTIVE_ITEMS_V6:
        concepts.setdefault(x["concept_id"],[]).append(x)

    candidates=[]
    for cid, items in concepts.items():
        meta=mastery.get(cid,{})
        if focus and items[0]["domain"] != focus:
            continue
        level=int(meta.get("mastery_level") or 0)
        due=meta.get("next_due")
        if hasattr(due,"date"): due=due.date()
        is_due=(due is not None and due <= today)
        unseen=(not meta)
        # Choose next stage, or one stage lower for due review.
        target=max(1,min(6, level if is_due and level else level+1))
        stage_item=next((i for i in items if i["level"]==target),items[0])
        priority=(100 if is_due else 80 if unseen else 40-level*3)
        candidates.append((priority,stage_item,is_due,unseen,level))
    random.shuffle(candidates); candidates.sort(key=lambda z:z[0],reverse=True)

    # Session recipe: ~40% due review, ~40% progression/new, ~20% operative/interpretive depth.
    chosen=[]; used=0; domains=set()
    for pri,item,is_due,unseen,level in candidates:
        if used + item["minutes"] > target_minutes+3: continue
        # encourage variety unless focused
        if not focus and item["domain"] in domains and len(chosen)<4: continue
        chosen.append(dict(item, reason=("Due review" if is_due else "New foundation" if unseen else "Next mastery step")))
        used += item["minutes"]; domains.add(item["domain"])
        if used >= target_minutes-3: break
    # fill if diversity rule undershot
    if used < target_minutes-5:
        ids={x["id"] for x in chosen}
        for _,item,is_due,unseen,level in candidates:
            if item["id"] in ids or used+item["minutes"]>target_minutes+3: continue
            chosen.append(dict(item, reason=("Due review" if is_due else "Next mastery step")))
            used+=item["minutes"]; ids.add(item["id"])
            if used>=target_minutes-3: break
    return chosen,used

@app.route("/daily-adaptive")
def daily_adaptive():
    focus=request.args.get("focus") or None
    try: mins=int(request.args.get("minutes","30"))
    except: mins=30
    mins=max(10,min(60,mins))
    plan,total=_adaptive_plan(mins,focus)
    from data import DEEP_MODULES_V6
    return render_template("daily_adaptive.html",plan=plan,total=total,minutes=mins,focus=focus,domains=list(DEEP_MODULES_V6.keys()))

@app.route("/daily-adaptive/answer", methods=["POST"])
def daily_adaptive_answer():
    from data import REVIEW_INTERVALS_V6
    payload=request.get_json(silent=True) or request.form
    try: rating=int(payload.get("rating",2))
    except: rating=2
    level=int(payload.get("level",1))
    try:
        from db import record_adaptive_result
        new_level=record_adaptive_result(payload.get("concept_id"),payload.get("item_id"),
            payload.get("domain"),payload.get("topic"),payload.get("stage"),level,rating,
            REVIEW_INTERVALS_V6.get(level,7))
        return jsonify({"ok":True,"mastery_level":new_level})
    except Exception as e:
        return jsonify({"ok":False,"error":str(e)}),500

@app.route("/curriculum/depth")
def curriculum_depth():
    from data import DEEP_MODULES_V6, EVIDENCE_HIERARCHY_V6
    return render_template("curriculum_depth.html",modules=DEEP_MODULES_V6,evidence=EVIDENCE_HIERARCHY_V6)
