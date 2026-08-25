from flask import Flask, render_template, request, redirect, url_for, jsonify
import os, random, re, difflib
from data import *
from data import _v6_item_id
from db import init_db, record_lab_attempt, lab_progress, lab_stats, record_mastery_event, unified_mastery_profiles, unified_stats, unified_dimension_summary, unified_domain_mastery, unified_weak_concepts, unified_mistakes

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-ent-mastery-change-me")
init_db()

@app.context_processor
def inject():
    try:
        shell_stats=unified_stats()
    except Exception:
        shell_stats={"mastery":0,"due":0,"concepts":0,"attempts":0,"coverage":0}
    return {
        "DOMAINS":[{"id":d,"name":d} for d in CANONICAL_DOMAINS_V94],
        "shell_stats":shell_stats,
        "shell_domains":CANONICAL_DOMAINS_V94
    }

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

    domain_icons={
      "Otology / Neurotology":"◉",
      "Rhinology / Allergy / Skull Base":"⌁",
      "Head & Neck Oncology":"◇",
      "Thyroid / Parathyroid / Salivary":"♢",
      "Pediatric Otolaryngology":"○",
      "Laryngology / Voice / Swallowing":"◫",
      "Facial Plastics / Trauma":"△",
      "Sleep Surgery":"☾",
      "General ENT / Emergencies":"+",
    }
    domain_cards=[]
    for dname in CANONICAL_DOMAINS_V94:
        domain_cards.append({
          "name":dname,
          "mastery":domains.get(dname,0),
          "topics":len(DEEP_MODULES_V6.get(dname,[])),
          "icon":domain_icons.get(dname,"•")
        })

    return render_template("dashboard.html", stats=st, weak=weak,
                           dimension_summary=dsum, domain_mastery=domains,
                           weakest_dimensions=weakest_dims,
                           integrated_cases=recommended,
                           integrated_total=len(INTEGRATED_CASES),
                           domain_cards=domain_cards,
                           anatomy_total=len(ANATOMY_ATLAS_V97),
                           or_total=len(OR_PREP_REGISTRY),
                           lab_total=len(INTERPRETATION_LABS), challenge_total=len(CLINICAL_CHALLENGES_V119), concept_check_total=len(CONCEPT_CHECKS_V112))

@app.route("/today")
def today():
    return redirect(url_for("daily_adaptive", minutes=request.args.get("minutes",30)))

@app.route("/learn")
def learn():
    return redirect(url_for("curriculum"))

@app.route("/topic/<slug>")
def topic(slug):
    return redirect(url_for("search", q=slug.replace("-"," ")))

def _canonical_search_index():
    """Build the searchable index without allowing one bad source record to blank the whole search."""
    from urllib.parse import quote_plus
    rows=[]

    # Deep Curriculum is canonical. Always retain it even if an optional source has malformed data.
    for domain,mods in (DEEP_MODULES_V6 or {}).items():
        for mod in (mods or []):
            try:
                title=str(mod.get("topic","") or "")
                if not title:
                    continue
                cid=_v6_item_id(domain,title)
                rows.append({
                    "type":"Curriculum concept",
                    "title":title,
                    "subtitle":str(domain),
                    "url":"/concept/id/"+quote_plus(cid),
                    "text":" ".join(str(mod.get(k,"") or "") for k in
                                  ["recognize","localize","workup","manage","operate","teach"])
                })
            except Exception:
                app.logger.exception("Skipping malformed curriculum search record")

    try:
        for c in (INTEGRATED_CASES or []):
            try:
                rows.append({
                    "type":"Progressive case",
                    "title":str(c.get("title","") or ""),
                    "subtitle":str(c.get("domain","ENT") or "ENT"),
                    "url":"/integrated/"+str(c.get("id","") or ""),
                    "text":str(c.get("summary","") or "")+" "+" ".join(str(x) for x in (c.get("tags") or []))
                })
            except Exception:
                app.logger.exception("Skipping malformed case search record")
    except Exception:
        app.logger.exception("Integrated case search indexing failed")

    try:
        for slug,lab in (INTERPRETATION_LABS or {}).items():
            try:
                rows.append({
                    "type":"Interpretation Atlas",
                    "title":str(lab.get("title",slug) or slug),
                    "subtitle":"Interpretation Atlas",
                    "url":"/lab/"+str(slug),
                    "text":" ".join(str(x) for x in (lab.get("framework") or []))+" "+str(lab.get("source_note","") or "")
                })
            except Exception:
                app.logger.exception("Skipping malformed lab search record")
    except Exception:
        app.logger.exception("Interpretation search indexing failed")

    try:
        for q in CLINICAL_CHALLENGES_V119:
            rows.append({
                "type":"Clinical Challenge",
                "title":q.get("topic",""),
                "subtitle":q.get("domain",""),
                "url":"/clinical-challenge/"+q.get("id",""),
                "text":q.get("stem","")+" "+" ".join(q.get("choices") or [])
            })
    except Exception:
        app.logger.exception("Clinical challenge search indexing failed")

    rows.append({
        "type":"Interpretation Atlas",
        "title":"Otoscopy Atlas",
        "subtitle":"Otology",
        "url":"/lab/otoscopy",
        "text":"otoscopy tympanic membrane external auditory canal middle ear"
    })

    try:
        for slug,op in (OR_PREP_REGISTRY or {}).items():
            try:
                title=str(op.get("title",slug) or slug)
                rows.append({
                    "type":"OR Tomorrow",
                    "title":title,
                    "subtitle":str(canonical_domain_v94(op.get("domain")) or ""),
                    "url":"/case-tomorrow?q="+quote_plus(title),
                    "text":" ".join(
                        [str(op.get("indications","") or "")]
                        + [str(x) for x in (op.get("steps") or [])]
                        + [str(x) for x in (op.get("danger") or [])]
                    )
                })
            except Exception:
                app.logger.exception("Skipping malformed OR search record")
    except Exception:
        app.logger.exception("OR search indexing failed")

    try:
        for src in (CURRENT_EVIDENCE_CATALOG_V98 or []):
            try:
                rows.append({
                    "type":"Evidence",
                    "title":str(src.get("title","") or ""),
                    "subtitle":str(src.get("area","Evidence") or "Evidence"),
                    "url":"/evidence",
                    "text":" ".join(str(src.get(k,"") or "") for k in ["kind","year","status"])
                })
            except Exception:
                app.logger.exception("Skipping malformed evidence search record")
    except Exception:
        pass

    return rows


_SEARCH_ALIASES_V1009 = {
    "scc":["squamous cell carcinoma"],
    "squamous cell carcinoma":["scc"],
    "aoe":["acute otitis externa"],
    "otitis externa":["acute otitis externa"],
    "osa":["obstructive sleep apnea"],
    "ssnhl":["sudden sensorineural hearing loss"],
    "bppv":["benign paroxysmal positional vertigo"],
    "aom":["acute otitis media"],
    "ome":["otitis media with effusion"],
    "crs":["chronic rhinosinusitis"],
    "crswnp":["chronic rhinosinusitis with nasal polyps"],
    "crssnp":["chronic rhinosinusitis without nasal polyps"],
    "fess":["functional endoscopic sinus surgery","endoscopic sinus surgery"],
    "rln":["recurrent laryngeal nerve"],
    "ebsln":["external branch superior laryngeal nerve"],
    "hns":["hypoglossal nerve stimulation","hypoglossal nerve stimulator"],
    "ci":["cochlear implant","cochlear implantation"],
    "tmj":["temporomandibular joint"],
    "pta":["peritonsillar abscess"],
}

def _search_terms_v1009(q):
    q=(q or "").strip().lower()
    terms=[x for x in re.split(r"\s+",q) if x]
    aliases=[]
    for key,vals in _SEARCH_ALIASES_V1009.items():
        if key == q or key in terms or key in q:
            aliases.extend(vals)
    return terms,aliases

def _search_score_v1009(row,q):
    title=str(row.get("title","") or "").lower()
    subtitle=str(row.get("subtitle","") or "").lower()
    text=str(row.get("text","") or "").lower()
    hay=title+" "+subtitle+" "+text
    terms,aliases=_search_terms_v1009(q)

    score=0
    if q == title:
        score += 1000
    elif q and q in title:
        score += 300
    elif q and q in hay:
        score += 100

    matched_terms=0
    for t in terms:
        if t in title:
            score += 40
            matched_terms += 1
        elif t in hay:
            score += 8
            matched_terms += 1

    for alias in aliases:
        if alias == title:
            score += 600
        elif alias in title:
            score += 200
        elif alias in hay:
            score += 50

    try:
        ratio=difflib.SequenceMatcher(None,q,title).ratio()
        if ratio >= .84:
            score += int(ratio*100)
    except Exception:
        pass

    if row.get("type")=="Curriculum concept" and score>0:
        score += 75

    if terms and matched_terms==0 and not aliases:
        return 0

    return score


@app.route("/search")
def search():
    q=request.args.get("q","").strip().lower()
    rows=[]
    try:
        index=_canonical_search_index()
        if q:
            scored=[]
            for r in index:
                score=_search_score_v1009(r,q)
                if score>0:
                    scored.append((score,r))
            rows=[r for _,r in sorted(scored,key=lambda x:(-x[0],0 if x[1].get("type")=="Curriculum concept" else 1,str(x[1].get("title",""))))[:80]]
    except Exception:
        app.logger.exception("Search failed")
        rows=[]
    return render_template("search.html", q=q, results=rows)


def _norm_or_text(s):
    import re
    return " ".join(re.findall(r"[a-z0-9]+", (s or "").lower()))

def _or_rank(q):
    import difflib
    nq=_norm_or_text(q)
    if not nq: return []
    qt=nq.split(); ranked=[]
    for slug,x in OR_PREP_REGISTRY.items():
        ns=_norm_or_text(slug); nt=_norm_or_text(x.get("title",""))
        slug_tokens=ns.split(); title_tokens=nt.split(); all_tokens=set(slug_tokens+title_tokens)
        score=0
        if nq==ns or nq==nt: score=100
        elif all(t in all_tokens for t in qt): score=94 if all(t in title_tokens for t in qt) else 88
        else:
            coverage=sum(1 for t in qt if t in all_tokens)/max(1,len(qt))
            phrase=difflib.SequenceMatcher(None,nq,nt).ratio(); score=round(55*coverage+30*phrase)
            if coverage==0: score=min(score,45)
        ranked.append((score,slug,x))
    return sorted(ranked,key=lambda z:z[0],reverse=True)

def _canonical_for_or_domain(label): return canonical_domain_v94(label)

def _related_or_gaps(prep, limit=4):
    if not prep: return []
    canonical=_canonical_for_or_domain(prep.get("domain")); profiles=unified_mastery_profiles()
    try:
        from db import adaptive_mastery_map
        adaptive=adaptive_mastery_map()
    except Exception: adaptive={}
    title_tokens=set(_norm_or_text(prep.get("title")).split()); candidates=[]
    for domain,mods in DEEP_MODULES_V6.items():
        if canonical_domain_v94(domain)!=canonical: continue
        for idx,mod in enumerate(mods):
            cid=_v6_item_id(domain,mod["topic"]); p=profiles.get(cid,{}); meta=adaptive.get(cid,{})
            mastery=p.get("overall",0); coverage=p.get("coverage",0); attempts=int(meta.get("attempts") or 0)
            overlap=len(title_tokens & set(_norm_or_text(mod["topic"]).split()))
            score=(-overlap,mastery,coverage,0 if attempts==0 else 1,idx)
            candidates.append((score,{"concept_id":cid,"topic":mod["topic"],"domain":domain,"mastery":mastery,"coverage":coverage,"attempts":attempts}))
    candidates.sort(key=lambda x:x[0]); return [x[1] for x in candidates[:limit]]

@app.route("/case-tomorrow")
def case_tomorrow():
    q=request.args.get("q","").strip(); directory=OR_PREP_REGISTRY or {}; prep=None; or_choices=[]; related=[]; matches=[]
    try:
        if q:
            ranked=_or_rank(q)
            if ranked:
                top=ranked[0]; margin=top[0]-(ranked[1][0] if len(ranked)>1 else 0)
                if top[0]>=92 or (top[0]>=82 and margin>=7): prep=top[2]
                elif top[0]>=60: or_choices=[x[2] for x in ranked[:5] if x[0]>=55]
        if prep:
            try: related=_related_or_gaps(prep)
            except Exception: related=[]
            return render_template("case_tomorrow.html",q=q,prep=prep,or_choices=[],matches=[],questions=[],or_directory=directory,related_gaps=related)
        if or_choices:
            return render_template("case_tomorrow.html",q=q,prep=None,or_choices=or_choices,matches=[],questions=[],or_directory=directory,related_gaps=[])
        if q:
            nq=_norm_or_text(q); qt=nq.split()
            for r in _canonical_search_index():
                hay=_norm_or_text(r.get("title","")+" "+r.get("subtitle","")+" "+r.get("text",""))
                if all(t in hay.split() for t in qt): matches.append(r)
        return render_template("case_tomorrow.html",q=q,prep=None,or_choices=[],matches=matches[:8],questions=[],or_directory=directory,related_gaps=[])
    except Exception:
        app.logger.exception("OR Tomorrow failed")
        return render_template("case_tomorrow.html",q=q,prep=None,or_choices=[],matches=[],questions=[],or_directory=directory,related_gaps=[],runtime_warning="Some personalized OR recommendations could not load; the audited procedure directory is still available.")

@app.route("/questions")
def questions(): return redirect(url_for("daily_adaptive"))

@app.route("/clinical-challenges")
def clinical_challenges():
    domain=request.args.get("domain","").strip(); topic=request.args.get("topic","").strip(); tier=request.args.get("tier","").strip(); mode=request.args.get("mode","").strip(); rows=list(CLINICAL_CHALLENGES_V119)
    if domain: rows=[q for q in rows if canonical_domain_v94(q.get("domain"))==canonical_domain_v94(domain)]
    if topic:
        t=topic.lower(); rows=[q for q in rows if t in q.get("topic","").lower() or t in q.get("stem","").lower()]
    if tier: rows=[q for q in rows if q.get("tier")==tier]
    if mode: rows=[q for q in rows if q.get("mode")==mode]
    stats={"questions":len(CLINICAL_CHALLENGES_V119),"topics":len({q.get("concept_id") for q in CLINICAL_CHALLENGES_V119 if q.get("concept_id")}),"curated":sum(1 for q in CLINICAL_CHALLENGES_V119 if q.get("tier")=="Curated board-style"),"coverage":sum(1 for q in CLINICAL_CHALLENGES_V119 if q.get("tier")!="Curated board-style")}
    return render_template("clinical_challenges.html",questions=rows,domains=CANONICAL_DOMAINS_V94,domain=domain,topic=topic,tier=tier,mode=mode,stats=stats)

@app.route("/clinical-challenge/<qid>")
def clinical_challenge(qid):
    q=CLINICAL_CHALLENGE_BY_ID_V119.get(qid)
    if not q: return redirect(url_for("clinical_challenges"))
    return render_template("clinical_challenge.html",q=q)

@app.route("/api/clinical-challenge", methods=["POST"])
def api_clinical_challenge():
    payload=request.get_json(force=True) or {}; qid=str(payload.get("qid","")); q=CLINICAL_CHALLENGE_BY_ID_V119.get(qid)
    if not q: return jsonify({"ok":False,"error":"unknown challenge"}),404
    try: chosen=int(payload.get("chosen",-1))
    except Exception: chosen=-1
    correct=(chosen==int(q.get("answer",-2))); dimension="management" if q.get("mode")=="Manage" else "reasoning"
    try: record_mastery_event(q.get("concept_id") or _v6_item_id(q.get("domain","ENT"),q.get("topic","")),q.get("domain","ENT"),dimension,3 if correct else 0,source_type="clinical_challenge",source_id=qid,miss_type=None if correct else "discrimination")
    except Exception: app.logger.exception("Clinical challenge mastery recording failed")
    return jsonify({"ok":True,"correct":correct})

@app.route("/concept-checks")
def concept_checks():
    domain=request.args.get("domain","").strip(); topic=request.args.get("topic","").strip(); rows=list(CONCEPT_CHECKS_V112)
    if domain: rows=[q for q in rows if canonical_domain_v94(q.get("domain"))==canonical_domain_v94(domain)]
    if topic:
        t=topic.lower(); rows=[q for q in rows if t in q.get("topic","").lower()]
    return render_template("concept_checks.html",questions=rows,domains=CANONICAL_DOMAINS_V94,domain=domain,topic=topic,total=len(CONCEPT_CHECKS_V112))

@app.route("/concept-check/<qid>")
def concept_check(qid):
    q=CONCEPT_CHECK_BY_ID_V112.get(qid)
    if not q: return redirect(url_for("concept_checks"))
    return render_template("concept_check.html",q=q)

@app.route("/integrated")
def integrated_index(): return render_template("integrated_index.html",cases=INTEGRATED_CASES,profiles=unified_mastery_profiles())

@app.route("/integrated/<case_id>")
def integrated_case(case_id):
    c=get_integrated_case(case_id)
    if not c: return redirect(url_for("integrated_index"))
    return render_template("integrated_case.html",case=c)

@app.route("/api/mastery-event",methods=["POST"])
def mastery_event():
    d=request.get_json(force=True); raw=d.get("concept_id"); dim=d.get("dimension")
    if not raw or not dim: return jsonify({"error":"concept_id and dimension required"}),400
    try: score=int(d.get("score",0))
    except Exception: score=0
    if score not in (0,1,2,3): return jsonify({"error":"score must be 0-3"}),400
    cid=canonical_concept_id_v98(raw,d.get("domain","ENT")); domain=canonical_concept_domain_v98(raw,d.get("domain","ENT")); record_mastery_event(cid,domain,dim,score,d.get("source_type"),d.get("source_id"),d.get("miss_type")); return jsonify({"ok":True,"profile":unified_mastery_profiles().get(cid,{})})

@app.route("/api/mastery-miss",methods=["POST"])
def mastery_miss():
    d=request.get_json(force=True); cid=d.get("concept_id"); miss=d.get("miss_type")
    if not cid or not miss: return jsonify({"error":"missing fields"}),400
    record_mastery_event(cid,d.get("domain","ENT"),d.get("dimension","reasoning"),1,d.get("source_type"),d.get("source_id"),miss); return jsonify({"ok":True})

@app.route("/cases")
def cases(): return redirect(url_for("integrated_index"))
@app.route("/case/<cid>")
def case(cid): return redirect(url_for("integrated_index"))
@app.route("/operate")
def operate(): return redirect(url_for("case_tomorrow"))
@app.route("/operate/<slug>")
def operation(slug): return redirect(url_for("case_tomorrow",q=slug.replace("-"," ")))

@app.route("/anatomy")
def anatomy():
    regions={}
    for x in ANATOMY_ATLAS_V97: regions.setdefault(x["region"],[]).append(x)
    return render_template("anatomy_atlas.html",regions=regions,total=len(ANATOMY_ATLAS_V97))
@app.route("/complications")
def complications(): return redirect(url_for("curriculum_depth"))

def _adaptive_lab_session(slug,cases,count=7):
    progress=lab_progress(slug)
    def score(c):
        p=progress.get(c.get("id"),{}); attempts=p.get("attempts",0); rating=p.get("last_rating")
        if rating is not None and rating<=1: bucket=0
        elif attempts==0: bucket=1
        elif rating==2: bucket=2
        else: bucket=3
        return (bucket,attempts,random.random())
    ranked=sorted(cases,key=score); picked=[]; concepts=set()
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
def lab(): return render_template("lab.html",labs=INTERPRETATION_LABS)
@app.route("/lab/<slug>")
def interpretation_lab(slug):
    if slug=="otoscopy": return redirect(url_for("otoscopy_lab"))
    lab_data=INTERPRETATION_LABS.get(slug)
    if not lab_data: return redirect(url_for("lab"))
    level=request.args.get("level","all"); track=request.args.get("track","all"); cases=lab_data.get("cases",[])
    if track!="all": cases=[c for c in cases if c.get("track","all")==track]
    if level!="all": cases=[c for c in cases if str(c.get("level"))==str(level)]
    mode=request.args.get("mode","session")
    try: session_size=int(request.args.get("count",7))
    except (TypeError,ValueError): session_size=7
    session_size=max(3,min(12,session_size))
    if mode=="session": cases=_adaptive_lab_session(slug,cases,session_size)
    return render_template("interpretation_lab.html",lab=lab_data,slug=slug,cases=cases,level=level,track=track,mode=mode,session_size=session_size,lab_stats=lab_stats(slug),bank_size=len(lab_data.get("cases",[])),seed_count=lab_data.get("seed_case_count",len(lab_data.get("cases",[]))))
@app.route("/lab/otoscopy")
def otoscopy_lab():
    level=request.args.get("level","all"); cases=OTOSCOPY_CASES
    if level!="all": cases=[c for c in cases if str(c.get("level"))==str(level)]
    return render_template("otoscopy_lab.html",cases=cases,level=level)
@app.route("/api/lab-rate",methods=["POST"])
def lab_rate():
    d=request.get_json(force=True); slug=d.get("lab_slug",""); case_id=d.get("case_id",""); concept_id=d.get("concept_id") or case_id
    try: rating=int(d.get("rating",2))
    except Exception: rating=2
    if not slug or not case_id or rating not in (0,1,2,3): return jsonify({"error":"invalid lab rating"}),400
    record_lab_attempt(slug,case_id,concept_id,rating); variant=d.get("variant_type","interpret"); dimension={"interpret":"recognition","reason":"reasoning","teach":"teaching"}.get(variant,"recognition"); parent=LAB_PARENT_CONCEPT_V98.get(slug,concept_id); record_mastery_event(parent,canonical_concept_domain_v98(parent,d.get("domain",slug)),dimension,rating,"interpretation_atlas",case_id,d.get("miss_type")); return jsonify({"ok":True,"stats":lab_stats(slug)})

@app.route("/attending")
def attending():
    mode=request.args.get("mode","attending"); domain=request.args.get("domain","all"); topic=request.args.get("topic","").strip().lower(); prompts=list(get_chief_prompts_v120() if mode=="chief" else get_attending_prompts_v120())
    if domain!="all": prompts=[p for p in prompts if p.get("domain")==domain]
    if topic: prompts=[p for p in prompts if topic in p.get("topic","").lower()]
    return render_template("attending.html",prompts=prompts,mode=mode,domain=domain,domains=CANONICAL_DOMAINS_V94,topic=topic)
@app.route("/chief")
def chief(): return redirect(url_for("attending",mode="chief"))
@app.route("/mistakes")
def mistakes():
    profiles=unified_mastery_profiles(); misses=unified_mistakes(100)
    for x in misses:
        p=profiles.get(x["concept_id"],{}); x["name"]=x.get("name") or p.get("name") or x["concept_id"].replace("-"," ").title(); x["domain"]=x.get("domain") or p.get("domain") or "ENT"
    return render_template("mistakes.html",mistakes=misses)
@app.route("/curriculum")
def curriculum(): return render_template("curriculum.html",curriculum=get_curriculum_v120(),prerequisites=PREREQUISITES_SUGGESTED_V114,spiral=SPIRAL_LEVELS_V5)

def _norm_topic_v94(s): return re.sub(r"[^a-z0-9]+"," ",(s or "").lower()).strip()
def _find_deep_module_v94(domain,topic):
    nt=_norm_topic_v94(topic)
    for dname,mods in DEEP_MODULES_V6.items():
        for mod in mods:
            if _norm_topic_v94(mod["topic"])==nt: return dname,mod
    target_domain=canonical_domain_v94(domain); best=None
    for dname,mods in DEEP_MODULES_V6.items():
        if canonical_domain_v94(dname)!=target_domain: continue
        for mod in mods:
            ratio=difflib.SequenceMatcher(None,nt,_norm_topic_v94(mod["topic"])).ratio()
            if best is None or ratio>best[0]: best=(ratio,dname,mod)
    if best and best[0]>=0.58: return best[1],best[2]
    return None,None

def _concept_context_v1006(dname,mod):
    cid=_v6_item_id(dname,mod["topic"])
    try: profiles=unified_mastery_profiles(); profile=profiles.get(cid,{})
    except Exception: app.logger.exception("Concept Hub mastery profile failed"); profile={}
    try: prereqs=PREREQUISITES_SUGGESTED_V114.get(mod["topic"],[])
    except Exception: prereqs=[]
    mtoks=set(_norm_topic_v94(mod["topic"]).split()); cases=[]
    try:
        for c in INTEGRATED_CASES:
            ctags=set(c.get("tags") or []); overlap=len(mtoks & ctags)
            if canonical_domain_v94(c.get("domain"))==canonical_domain_v94(dname) or overlap: cases.append((overlap,c))
        cases=[c for _,c in sorted(cases,key=lambda x:(-x[0],x[1].get("title","")))[:4]]
    except Exception: app.logger.exception("Concept Hub related cases failed"); cases=[]
    ors=[]
    try:
        for slug,op in OR_PREP_REGISTRY.items():
            if canonical_domain_v94(op.get("domain"))!=canonical_domain_v94(dname): continue
            overlap=len(mtoks & set(_norm_topic_v94(op.get("title","")).split())); ors.append((overlap,op))
        ors=[o for _,o in sorted(ors,key=lambda x:(-x[0],x[1].get("title","")))[:4]]
    except Exception: app.logger.exception("Concept Hub related OR failed"); ors=[]
    labs=[]
    try:
        for slug,lab in INTERPRETATION_LABS.items():
            fw=lab.get("framework") or []; text=_norm_topic_v94((lab.get("title") or "")+" "+" ".join(fw)); overlap=sum(1 for t in mtoks if t in set(text.split()))
            if overlap: labs.append((overlap,slug,lab))
        labs=[(s,l) for _,s,l in sorted(labs,key=lambda x:-x[0])[:4]]
    except Exception: app.logger.exception("Concept Hub related labs failed"); labs=[]
    return dict(domain=dname,topic=mod["topic"],module=mod,concept_id=cid,profile=profile,prerequisites=prereqs,related_cases=cases,related_or=ors,related_labs=labs)

def _deep_module_by_id_v1006(concept_id):
    for dname,mods in DEEP_MODULES_V6.items():
        for mod in mods:
            if _v6_item_id(dname,mod["topic"])==concept_id: return dname,mod
    return None,None
@app.route("/concept")
def concept_hub():
    domain=request.args.get("domain",""); topic=request.args.get("topic","")
    try:
        dname,mod=_find_deep_module_v94(domain,topic)
        if not mod: return redirect(url_for("search",q=topic))
        return render_template("concept_hub.html",**_concept_context_v1006(dname,mod))
    except Exception: app.logger.exception("Concept Hub route failed"); return redirect(url_for("search",q=topic or domain))
@app.route("/concept/id/<concept_id>")
def concept_hub_id(concept_id):
    try:
        dname,mod=_deep_module_by_id_v1006(concept_id)
        if not mod: return redirect(url_for("search",q=concept_id.replace("-"," ")))
        return render_template("concept_hub.html",**_concept_context_v1006(dname,mod))
    except Exception: app.logger.exception("Concept Hub ID route failed"); return redirect(url_for("search",q=concept_id.replace("-"," ")))
@app.route("/evidence")
def evidence(): return render_template("evidence.html",sources=CURRENT_EVIDENCE_CATALOG_V98)
@app.route("/progress")
def progress():
    profiles=unified_mastery_profiles(); profile_rows=sorted(profiles.values(),key=lambda p:(p.get("overall",0),p.get("coverage",0),p.get("name","").lower()))
    return render_template("progress.html",stats=unified_stats(),profiles=profiles,profile_rows=profile_rows,dimensions=unified_dimension_summary(),domains=unified_domain_mastery(),mastery_dimensions=MASTERY_DIMENSIONS)
@app.route("/sources")
def sources(): return redirect(url_for("evidence"))

if __name__ == "__main__": app.run(debug=True)

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

    # v15.10 fix: topics that teach an interpretive/examination SKILL (reading
    # an audiogram, PSG, or stroboscopy exam; performing a structured trauma
    # exam) are neither a disease with a "dangerous alternative" to rule out,
    # nor pure anatomy/physiology. Without this branch they fell through to
    # the disease-pattern prompt, producing nonsensical questions like "what
    # presentation should make you think of Audiogram Interpretation, and
    # what dangerous alternative must you not miss?" - nothing "presents
    # like" an interpretive skill.
    interpretation_terms=("interpretation","structured facial trauma examination","outcomes research")
    is_interpretation=any(t in ntopic for t in interpretation_terms) or "interpretation" in tags

    if is_interpretation:
        prompts={
          "recognize":f"Without looking: what is your systematic approach to {topic}? What do you check, in what order, and what would make you question the result's validity?",
          "localize":f"Which specific findings or components of {topic} carry the most diagnostic weight, and which are easy to overweight or misread?",
          "workup":f"What additional data, history, or corroborating test would you want before acting on {topic} alone?",
          "manage":f"How does the result of {topic} actually change management, versus findings that are reassuring but don't change the plan?",
          "operate":f"What is the highest-stakes misread in {topic} - the mistake that leads to the wrong treatment or a missed diagnosis?",
          "teach":f"Teach {topic} to a junior as a step-by-step framework, then give the one pearl that catches the most common misread."
        }
    elif is_foundation:
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
    return prompts.get(stage,f"Explain the core reasoning for {topic}.")

def _adaptive_plan(target_minutes=30,focus=None,concept_id=None):
    from data import get_adaptive_items_v120,PREREQUISITES_GATING_V114
    ITEMS=get_adaptive_items_v120()
    try:
        from db import adaptive_mastery_map
        mastery=adaptive_mastery_map()
    except Exception: mastery={}
    import datetime
    today=datetime.date.today()
    def norm(s): return re.sub(r"[^a-z0-9]+"," ",(s or "").lower()).strip()
    curriculum_rank={}
    for domain,blob in CURRICULUM_V5.items():
        rank=0
        for section,topics in blob.get("sequence",[]):
            for t in topics: curriculum_rank[(domain,norm(t))]=rank; rank+=1
    concepts={}; topic_lookup={}
    for x in ITEMS:
        concepts.setdefault(x["concept_id"],[]).append(x); topic_lookup[(x["domain"],norm(x["topic"]))]=x["concept_id"]
    prereq_norm={norm(k):[norm(p) for p in v] for k,v in PREREQUISITES_GATING_V114.items()}; candidates=[]
    for cid,items in concepts.items():
        if concept_id and cid!=concept_id: continue
        base=items[0]
        if focus and base["domain"]!=focus: continue
        meta=mastery.get(cid,{}); level=int(meta.get("mastery_level") or 0); due=meta.get("next_due")
        if hasattr(due,"date"): due=due.date()
        is_due=bool(due and due<=today); unseen=not meta or int(meta.get("attempts") or 0)==0; target=max(1,min(6,level+1)); item=next((i for i in items if i["level"]==target),items[0]); unmet=[]
        for pre in prereq_norm.get(norm(base["topic"]),[]):
            pcid=topic_lookup.get((base["domain"],pre))
            if pcid and int(mastery.get(pcid,{}).get("attempts") or 0)==0: unmet.append(pre)
        if unmet and unseen and not is_due: continue
        rank=curriculum_rank.get((base["domain"],norm(base["topic"])),999); reason="Due review" if is_due else ("New foundation" if unseen and rank<5 else "New curriculum step" if unseen else "Next mastery step"); priority=(0 if is_due else 1,rank if unseen else 500+level,level); candidates.append({"priority":priority,"item":item,"due":is_due,"unseen":unseen,"level":level,"rank":rank,"reason":reason})
    if not candidates: return [],0
    candidates.sort(key=lambda z:z["priority"])
    if focus: anchor=focus
    else:
        domain_scores={}
        for z in candidates:
            d=z["item"]["domain"]; s=domain_scores.setdefault(d,{"due":0,"rank":999,"mastery":[]}); s["due"]+=1 if z["due"] else 0; s["rank"]=min(s["rank"],z["rank"]); s["mastery"].append(z["level"])
        anchor=min(domain_scores,key=lambda d:(-domain_scores[d]["due"],sum(domain_scores[d]["mastery"])/len(domain_scores[d]["mastery"]),domain_scores[d]["rank"],d))
    chosen=[]; used=0; used_ids=set(); due_budget=max(4,round(target_minutes*.30))
    def add(z):
        nonlocal used
        item=z["item"]
        if item["id"] in used_ids or used+item["minutes"]>target_minutes+3: return False
        chosen.append(dict(item,prompt=_adaptive_question(item),mastery_before=z["level"],reason=z["reason"])); used+=item["minutes"]; used_ids.add(item["id"]); return True
    for z in [x for x in candidates if x["due"]]:
        if used>=due_budget: break
        add(z)
    for z in [x for x in candidates if x["item"]["domain"]==anchor and not x["due"]]:
        if used>=target_minutes-3: break
        add(z)
    for z in candidates:
        if used>=target_minutes-3: break
        add(z)
    return chosen,used

@app.route("/daily-adaptive")
def daily_adaptive():
    focus=request.args.get("focus") or None; concept_id=request.args.get("concept") or None
    try: mins=int(request.args.get("minutes","30"))
    except: mins=30
    mins=max(10,min(60,mins)); plan,total=_adaptive_plan(mins,focus,concept_id); from data import DEEP_MODULES_V6
    challenge_pool=[q for q in CLINICAL_CHALLENGES_V119 if (not focus or canonical_domain_v94(q.get("domain"))==canonical_domain_v94(focus))]; random.shuffle(challenge_pool); challenge_count=max(1,min(3,mins//15)); daily_challenges=challenge_pool[:challenge_count]
    return render_template("daily_adaptive.html",plan=plan,total=total,minutes=mins,focus=focus,concept_id=concept_id,domains=list(DEEP_MODULES_V6.keys()),daily_challenges=daily_challenges)

@app.route("/daily-adaptive/answer",methods=["POST"])
def daily_adaptive_answer():
    from data import REVIEW_INTERVALS_V6
    payload=request.get_json(silent=True) or request.form
    try: rating=int(payload.get("rating",2))
    except: rating=2
    level=int(payload.get("level",1))
    try:
        from db import record_adaptive_result
        new_level=record_adaptive_result(payload.get("concept_id"),payload.get("item_id"),payload.get("domain"),payload.get("topic"),payload.get("stage"),level,rating,REVIEW_INTERVALS_V6.get(level,7))
        from db import adaptive_mastery_map
        state=adaptive_mastery_map().get(payload.get("concept_id"),{}); due=state.get("next_due"); next_level=min(6,new_level+1) if new_level<6 else None; next_stage={1:"Recognize",2:"Localize",3:"Evaluate",4:"Manage",5:"Advanced",6:"Teach"}.get(next_level); return jsonify({"ok":True,"mastery_level":new_level,"next_due":str(due) if due else None,"passed":rating>=2,"next_level":next_level,"next_stage":next_stage})
    except Exception as e: return jsonify({"ok":False,"error":str(e)}),500

@app.route("/curriculum/depth")
def curriculum_depth():
    from data import DEEP_MODULES_V6,EVIDENCE_HIERARCHY_V6
    return render_template("curriculum_depth.html",modules=DEEP_MODULES_V6,evidence=EVIDENCE_HIERARCHY_V6)
