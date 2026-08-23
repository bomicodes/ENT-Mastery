from flask import Flask, render_template, request, redirect, url_for, jsonify
import os, random, re, difflib
from data import *
from db import init_db, record_lab_attempt, lab_progress, lab_stats, record_mastery_event, unified_mastery_profiles, unified_stats, unified_dimension_summary, unified_domain_mastery, unified_weak_concepts, unified_mistakes

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-ent-mastery-change-me")
init_db()

@app.context_processor
def inject():
    return {"DOMAINS": [{"id":d,"name":d} for d in CANONICAL_DOMAINS_V94]}

@app.route("/")
def dashboard():
    st=unified_stats()
    profiles=unified_mastery_profiles()
    weak=unified_weak_concepts(4)
    dsum=unified_dimension_summary()
    domains=unified_domain_mastery()
    weakest_dims=sorted(dsum.items(), key=lambda x:x[1])[:3]

    # Homepage shows a small recommended set, not the entire case library.
    weak_domains=[x["domain"] for x in weak]
    def case_score(c):
        p=profiles.get(c.get("concept_id"),{})
        domain_bonus=0 if c.get("domain") in weak_domains else 1
        attempted=1 if p else 0
        mastery=p.get("overall",0)
        return (domain_bonus, attempted, mastery, c.get("title",""))
    recommended=sorted(INTEGRATED_CASES,key=case_score)[:6]

    return render_template("dashboard.html", stats=st, weak=weak,
                           dimension_summary=dsum, domain_mastery=domains,
                           weakest_dimensions=weakest_dims,
                           integrated_cases=recommended,
                           integrated_total=len(INTEGRATED_CASES))

@app.route("/today")
def today():
    return redirect(url_for("daily_adaptive", minutes=request.args.get("minutes",30)))

@app.route("/learn")
def learn():
    return redirect(url_for("curriculum"))

@app.route("/topic/<slug>")
def topic(slug):
    return redirect(url_for("search", q=slug.replace("-"," ")))

@app.route("/search")
def search():
    q=request.args.get("q","").strip().lower()
    rows=_canonical_search_index()
    if q:
        terms=[x for x in re.split(r"\s+",q) if x]
        scored=[]
        for r in rows:
            hay=(r["title"]+" "+r["subtitle"]+" "+r["text"]).lower()
            title=r["title"].lower()
            score=sum((5 if t in title else 1) for t in terms if t in hay)
            if score: scored.append((score,r))
        rows=[r for _,r in sorted(scored,key=lambda x:(-x[0],x[1]["title"]))]
    else:
        rows=[]
    return render_template("search.html", q=q, results=rows)

def _norm_or_text(s):
    import re
    return " ".join(re.findall(r"[a-z0-9]+", (s or "").lower()))

def _or_rank(q):
    import difflib
    nq=_norm_or_text(q)
    if not nq: return []
    qt=nq.split()
    ranked=[]
    for slug,x in OR_PREP_REGISTRY.items():
        ns=_norm_or_text(slug)
        nt=_norm_or_text(x.get("title",""))
        slug_tokens=ns.split()
        title_tokens=nt.split()
        all_tokens=set(slug_tokens+title_tokens)

        score=0
        # Exact title/slug is always strongest.
        if nq==ns or nq==nt:
            score=100
        # Exact word/token matching is next. This deliberately prevents
        # "thyroidectomy" from matching the single word "parathyroidectomy".
        elif all(t in all_tokens for t in qt):
            # Prefer a title containing the query words over a slug-only hit.
            if all(t in title_tokens for t in qt):
                score=94
            else:
                score=88
        else:
            # Fuzzy ranking is only a fallback and is penalized when the query's
            # core words are not present as whole words.
            coverage=sum(1 for t in qt if t in all_tokens)/max(1,len(qt))
            phrase=difflib.SequenceMatcher(None,nq,nt).ratio()
            score=round(55*coverage+30*phrase)
            if coverage==0:
                score=min(score,45)

        ranked.append((score,slug,x))
    return sorted(ranked,key=lambda z:z[0],reverse=True)

def _canonical_for_or_domain(label):
    return canonical_domain_v94(label)

def _related_or_gaps(prep, limit=4):
    if not prep: return []
    canonical=_canonical_for_or_domain(prep.get("domain"))
    profiles=unified_mastery_profiles()
    try:
        from db import adaptive_mastery_map
        adaptive=adaptive_mastery_map()
    except Exception:
        adaptive={}

    title_tokens=set(_norm_or_text(prep.get("title")).split())
    candidates=[]
    for domain,mods in DEEP_MODULES_V6.items():
        if canonical_domain_v94(domain)!=canonical:
            continue
        for idx,mod in enumerate(mods):
            cid=_v6_item_id(domain,mod["topic"])
            p=profiles.get(cid,{})
            meta=adaptive.get(cid,{})
            mastery=p.get("overall",0)
            coverage=p.get("coverage",0)
            attempts=int(meta.get("attempts") or 0)
            overlap=len(title_tokens & set(_norm_or_text(mod["topic"]).split()))
            # Same-operation concept first, then foundations that are weak/unseen.
            score=(-overlap, mastery, coverage, 0 if attempts==0 else 1, idx)
            candidates.append((score,{
              "concept_id":cid,"topic":mod["topic"],"domain":domain,
              "mastery":mastery,"coverage":coverage,"attempts":attempts
            }))
    candidates.sort(key=lambda x:x[0])
    return [x[1] for x in candidates[:limit]]

@app.route("/case-tomorrow")
def case_tomorrow():
    q=request.args.get("q","").strip()
    prep=None; or_choices=[]; related=[]
    if q:
        ranked=_or_rank(q)
        if ranked:
            top=ranked[0]
            margin=top[0]-(ranked[1][0] if len(ranked)>1 else 0)
            if top[0]>=92 or (top[0]>=82 and margin>=7):
                prep=top[2]
            elif top[0]>=60:
                or_choices=[x[2] for x in ranked[:5] if x[0]>=55]
    if prep:
        related=_related_or_gaps(prep)
        return render_template("case_tomorrow.html", q=q, prep=prep, or_choices=[], matches=[],
                               questions=[], or_directory=OR_PREP_REGISTRY, related_gaps=related)
    if or_choices:
        return render_template("case_tomorrow.html", q=q, prep=None, or_choices=or_choices,
                               matches=[], questions=[], or_directory=OR_PREP_REGISTRY, related_gaps=[])
    if q:
        matches=[]
        nq=_norm_or_text(q); qt=nq.split()
        for r in _canonical_search_index():
            hay=_norm_or_text(r["title"]+" "+r.get("subtitle","")+" "+r.get("text",""))
            if all(t in hay.split() for t in qt): matches.append(r)
        return render_template("case_tomorrow.html", q=q, prep=None, or_choices=[], matches=matches[:8],
                               questions=[], or_directory=OR_PREP_REGISTRY, related_gaps=[])
    # True empty state: never default to a random operation.
    return render_template("case_tomorrow.html", q="", prep=None, or_choices=[], matches=[],
                           questions=[], or_directory=OR_PREP_REGISTRY, related_gaps=[])

@app.route("/questions")
def questions():
    return redirect(url_for("daily_adaptive"))



@app.route("/integrated")
def integrated_index():
    return render_template("integrated_index.html", cases=INTEGRATED_CASES, profiles=unified_mastery_profiles())

@app.route("/integrated/<case_id>")
def integrated_case(case_id):
    c=get_integrated_case(case_id)
    if not c: return redirect(url_for("integrated_index"))
    return render_template("integrated_case.html", case=c)

@app.route("/api/mastery-event", methods=["POST"])
def mastery_event():
    d=request.get_json(force=True); raw=d.get("concept_id"); dim=d.get("dimension")
    if not raw or not dim: return jsonify({"error":"concept_id and dimension required"}),400
    try: score=int(d.get("score",0))
    except Exception: score=0
    if score not in (0,1,2,3): return jsonify({"error":"score must be 0-3"}),400
    cid=canonical_concept_id_v98(raw,d.get("domain","ENT"))
    domain=canonical_concept_domain_v98(raw,d.get("domain","ENT"))
    record_mastery_event(cid,domain,dim,score,d.get("source_type"),d.get("source_id"),d.get("miss_type"))
    return jsonify({"ok":True,"profile":unified_mastery_profiles().get(cid,{})})

@app.route("/api/mastery-miss", methods=["POST"])
def mastery_miss():
    d=request.get_json(force=True); cid=d.get("concept_id"); miss=d.get("miss_type")
    if not cid or not miss: return jsonify({"error":"missing fields"}),400
    record_mastery_event(cid,d.get("domain","ENT"),d.get("dimension","reasoning"),1,d.get("source_type"),d.get("source_id"),miss)
    return jsonify({"ok":True})

@app.route("/cases")
def cases():
    return redirect(url_for("integrated_index"))

@app.route("/case/<cid>")
def case(cid):
    return redirect(url_for("integrated_index"))

@app.route("/operate")
def operate():
    return redirect(url_for("case_tomorrow"))

@app.route("/operate/<slug>")
def operation(slug):
    return redirect(url_for("case_tomorrow", q=slug.replace("-"," ")))

@app.route("/anatomy")
def anatomy():
    regions={}
    for x in ANATOMY_ATLAS_V97:
        regions.setdefault(x["region"],[]).append(x)
    return render_template("anatomy_atlas.html", regions=regions, total=len(ANATOMY_ATLAS_V97))

@app.route("/complications")
def complications():
    return redirect(url_for("curriculum_depth"))


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
    parent=LAB_PARENT_CONCEPT_V98.get(slug,concept_id)
    record_mastery_event(parent,canonical_concept_domain_v98(parent,d.get("domain",slug)),dimension,rating,"interpretation_atlas",case_id,d.get("miss_type"))
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
    return redirect(url_for("attending", level="chief"))

@app.route("/mistakes")
def mistakes():
    profiles=unified_mastery_profiles()
    misses=unified_mistakes(100)
    for x in misses:
        p=profiles.get(x["concept_id"],{})
        x["name"]=x.get("name") or p.get("name") or x["concept_id"].replace("-"," ").title()
        x["domain"]=x.get("domain") or p.get("domain") or "ENT"
    return render_template("mistakes.html", mistakes=misses)


@app.route("/curriculum")
def curriculum():
    from data import CURRICULUM_V5, PREREQUISITES_V5, SPIRAL_LEVELS_V5
    return render_template("curriculum.html", curriculum=CURRICULUM_V5, prerequisites=PREREQUISITES_V5, spiral=SPIRAL_LEVELS_V5)


def _norm_topic_v94(s):
    return re.sub(r"[^a-z0-9]+"," ",(s or "").lower()).strip()

def _find_deep_module_v94(domain, topic):
    nt=_norm_topic_v94(topic)
    # Exact topic first, regardless of minor domain taxonomy mismatch.
    for dname,mods in DEEP_MODULES_V6.items():
        for mod in mods:
            if _norm_topic_v94(mod["topic"])==nt:
                return dname,mod
    # Fuzzy fallback within requested canonical domain.
    target_domain=canonical_domain_v94(domain)
    best=None
    for dname,mods in DEEP_MODULES_V6.items():
        if canonical_domain_v94(dname)!=target_domain: continue
        for mod in mods:
            ratio=difflib.SequenceMatcher(None,nt,_norm_topic_v94(mod["topic"])).ratio()
            if best is None or ratio>best[0]: best=(ratio,dname,mod)
    if best and best[0]>=0.58: return best[1],best[2]
    return None,None

@app.route("/concept")
def concept_hub():
    domain=request.args.get("domain","")
    topic=request.args.get("topic","")
    dname,mod=_find_deep_module_v94(domain,topic)
    if not mod:
        return redirect(url_for("search",q=topic))
    cid=_v6_item_id(dname,mod["topic"])
    profiles=unified_mastery_profiles()
    profile=profiles.get(cid,{})
    # Prerequisites from the mapped curriculum.
    prereqs=PREREQUISITES_V5.get(topic, PREREQUISITES_V5.get(mod["topic"],[]))
    # Related progressive cases by normalized domain + keyword overlap.
    mtoks=set(_norm_topic_v94(mod["topic"]).split())
    cases=[]
    for c in INTEGRATED_CASES:
        overlap=len(mtoks & set(c.get("tags",[])))
        if c.get("domain")==canonical_domain_v94(dname) or overlap:
            cases.append((overlap,c))
    cases=[c for _,c in sorted(cases,key=lambda x:(-x[0],x[1]["title"]))[:4]]
    # Related OR modules.
    ors=[]
    for slug,op in OR_PREP_REGISTRY.items():
        if canonical_domain_v94(op.get("domain"))!=canonical_domain_v94(dname): continue
        overlap=len(mtoks & set(_norm_topic_v94(op["title"]).split()))
        ors.append((overlap,op))
    ors=[o for _,o in sorted(ors,key=lambda x:(-x[0],x[1]["title"]))[:4]]
    # Related interpretation areas.
    labs=[]
    for slug,lab in INTERPRETATION_LABS.items():
        text=_norm_topic_v94(lab.get("title","")+" "+" ".join(lab.get("framework",[])))
        overlap=sum(1 for t in mtoks if t in text.split())
        if overlap: labs.append((overlap,slug,lab))
    labs=[(s,l) for _,s,l in sorted(labs,key=lambda x:-x[0])[:4]]
    return render_template("concept_hub.html", domain=dname, topic=mod["topic"], module=mod,
                           concept_id=cid, profile=profile, prerequisites=prereqs,
                           related_cases=cases, related_or=ors, related_labs=labs)

@app.route("/evidence")
def evidence():
    return render_template("evidence.html", sources=CURRENT_EVIDENCE_CATALOG_V98)


@app.route("/progress")
def progress():
    profiles=unified_mastery_profiles()
    return render_template("progress.html",
                           stats=unified_stats(),
                           profiles=profiles,
                           dimensions=unified_dimension_summary(),
                           domains=unified_domain_mastery(),
                           mastery_dimensions=MASTERY_DIMENSIONS)
@app.route("/sources")
def sources():
    return redirect(url_for("evidence"))


if __name__ == "__main__":
    app.run(debug=True)


# =============================================================================
# v6 Adaptive Daily Path
# =============================================================================
def _adaptive_question(item):
    """Generate a prompt that matches the *kind* of concept being tested.

    The old generator asked every level-1 item for a "clinical pattern," which made
    foundational concepts such as Laryngeal Anatomy read nonsensically. Foundation
    topics now use structure/relationship/mechanism prompts while disease topics keep
    the clinical-recognition pathway.
    """
    topic=item.get("topic","this topic")
    stage=item.get("stage","recognize")
    ntopic=topic.lower()
    tags={str(x).lower() for x in item.get("tags",[]) }
    foundation_terms=("anatomy","physiology","neuroanatomy","principles","fundamentals","imaging fundamentals","electrophysiology")
    is_foundation=any(t in ntopic for t in foundation_terms) or bool(tags & {"anatomy","physiology","fundamentals"})

    if is_foundation:
        prompts={
          "recognize":f"Without looking: how would you organize {topic}, and what core structures or mechanisms must you know?",
          "localize":f"Walk through the key spatial or physiologic relationships in {topic}. What connects to what, and why does it matter?",
          "workup":f"How do you identify or assess {topic} on exam, testing, imaging, or endoscopy—and which findings or variants matter?",
          "manage":f"How does {topic} change your clinical or operative decisions? Give the practical consequences of the anatomy/physiology.",
          "operate":f"Apply {topic} to a procedure: what are the landmarks, danger structures, key relationships, and bailout considerations?",
          "teach":f"Teach {topic} to a junior from first principles, then give the one attending/boards pearl you would not want them to miss."
        }
    else:
        prompts={
          "recognize":f"Without looking: what presentation or finding should make you think of {topic}, and what dangerous alternative must you not miss?",
          "localize":f"How do you localize {topic} anatomically or physiologically, and what localization changes the differential?",
          "workup":f"What workup is useful for {topic}, and which findings actually change management?",
          "manage":f"What is your management framework for {topic}, including when to observe, treat, or escalate?",
          "operate":f"What is the advanced decision for {topic}? If a procedure has a role, give indication, anatomy, danger structures, and rescue plan; if not, explain the refractory/complication pathway.",
          "teach":f"Teach {topic} to a junior from first principles and give the key attending/boards pearl."
        }
    return prompts.get(stage, f"Explain the core reasoning for {topic}.")


def _adaptive_plan(target_minutes=30, focus=None, concept_id=None):
    from data import ADAPTIVE_ITEMS_V99 as ITEMS, PREREQUISITES_V5, CURRICULUM_V5
    try:
        from db import adaptive_mastery_map
        mastery=adaptive_mastery_map()
    except Exception:
        mastery={}

    import datetime
    today=datetime.date.today()

    def norm(s):
        return re.sub(r"[^a-z0-9]+"," ",(s or "").lower()).strip()

    # Curriculum rank makes unseen material move from foundations toward chief-level content.
    curriculum_rank={}
    for domain,blob in CURRICULUM_V5.items():
        rank=0
        for section,topics in blob.get("sequence",[]):
            for t in topics:
                curriculum_rank[(domain,norm(t))]=rank
                rank+=1

    # Deep items grouped by concept.
    concepts={}
    topic_lookup={}
    for x in ITEMS:
        concepts.setdefault(x["concept_id"],[]).append(x)
        topic_lookup[(x["domain"],norm(x["topic"]))]=x["concept_id"]

    # Explicit prerequisites only block new progression when the prerequisite concept exists
    # and has not yet been demonstrated at all.
    prereq_norm={norm(k):[norm(p) for p in v] for k,v in PREREQUISITES_V5.items()}

    candidates=[]
    for cid,items in concepts.items():
        if concept_id and cid != concept_id:
            continue
        base=items[0]
        if focus and base["domain"]!=focus:
            continue
        meta=mastery.get(cid,{})
        level=int(meta.get("mastery_level") or 0)
        due=meta.get("next_due")
        if hasattr(due,"date"): due=due.date()
        is_due=bool(due and due<=today)
        unseen=not meta or int(meta.get("attempts") or 0)==0

        target=max(1,min(6, level+1))
        item=next((i for i in items if i["level"]==target),items[0])

        unmet=[]
        for pre in prereq_norm.get(norm(base["topic"]),[]):
            pcid=topic_lookup.get((base["domain"],pre))
            if pcid and int(mastery.get(pcid,{}).get("attempts") or 0)==0:
                unmet.append(pre)

        # Don't introduce an advanced concept before a mapped prerequisite;
        # due review is still allowed so existing learning isn't hidden.
        if unmet and unseen and not is_due:
            continue

        rank=curriculum_rank.get((base["domain"],norm(base["topic"])),999)
        reason="Due review" if is_due else ("New foundation" if unseen and rank<5 else "New curriculum step" if unseen else "Next mastery step")
        priority=(0 if is_due else 1, rank if unseen else 500+level, level)
        candidates.append({"priority":priority,"item":item,"due":is_due,"unseen":unseen,
                           "level":level,"rank":rank,"reason":reason})

    if not candidates:
        return [],0
    candidates.sort(key=lambda z:z["priority"])

    # Mixed sessions still have one anchor domain so the experience feels curricular,
    # with due reviews from elsewhere allowed first.
    if focus:
        anchor=focus
    else:
        domain_scores={}
        for z in candidates:
            d=z["item"]["domain"]
            s=domain_scores.setdefault(d,{"due":0,"rank":999,"mastery":[]})
            s["due"]+=1 if z["due"] else 0
            s["rank"]=min(s["rank"],z["rank"])
            s["mastery"].append(z["level"])
        anchor=min(domain_scores, key=lambda d:(
            -domain_scores[d]["due"],
            sum(domain_scores[d]["mastery"])/len(domain_scores[d]["mastery"]),
            domain_scores[d]["rank"],
            d
        ))

    chosen=[]; used=0; used_ids=set()
    due_budget=max(4,round(target_minutes*.30))

    def add(z):
        nonlocal used
        item=z["item"]
        if item["id"] in used_ids or used+item["minutes"]>target_minutes+3:
            return False
        chosen.append(dict(item,prompt=_adaptive_question(item),mastery_before=z["level"],reason=z["reason"]))
        used+=item["minutes"]; used_ids.add(item["id"]); return True

    # 1) due reviews, limited so they don't fragment the whole session.
    for z in [x for x in candidates if x["due"]]:
        if used>=due_budget: break
        add(z)

    # 2) coherent progression in anchor domain.
    for z in [x for x in candidates if x["item"]["domain"]==anchor and not x["due"]]:
        if used>=target_minutes-3: break
        add(z)

    # 3) fill remaining time with the best next items from other domains.
    for z in candidates:
        if used>=target_minutes-3: break
        add(z)

    return chosen,used

@app.route("/daily-adaptive")
def daily_adaptive():
    focus=request.args.get("focus") or None
    concept_id=request.args.get("concept") or None
    try: mins=int(request.args.get("minutes","30"))
    except: mins=30
    mins=max(10,min(60,mins))
    plan,total=_adaptive_plan(mins,focus,concept_id)
    from data import DEEP_MODULES_V6
    return render_template("daily_adaptive.html",plan=plan,total=total,minutes=mins,focus=focus,
                           concept_id=concept_id,domains=list(DEEP_MODULES_V6.keys()))

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
        from db import adaptive_mastery_map
        state=adaptive_mastery_map().get(payload.get("concept_id"),{})
        due=state.get("next_due")
        next_level=min(6,new_level+1) if new_level < 6 else None
        next_stage={1:"Recognize",2:"Localize",3:"Evaluate",4:"Manage",5:"Advanced",6:"Teach"}.get(next_level)
        return jsonify({"ok":True,"mastery_level":new_level,"next_due":str(due) if due else None,
                        "passed":rating>=2,"next_level":next_level,"next_stage":next_stage})
    except Exception as e:
        return jsonify({"ok":False,"error":str(e)}),500

@app.route("/curriculum/depth")
def curriculum_depth():
    from data import DEEP_MODULES_V6, EVIDENCE_HIERARCHY_V6
    return render_template("curriculum_depth.html",modules=DEEP_MODULES_V6,evidence=EVIDENCE_HIERARCHY_V6)
