import random, re
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from pasha_review_data import PASHA_CHAPTERS, PASHA_CHAPTER_BY_ID, PASHA_SEED_QUESTIONS
from pasha_db import pasha_progress, record_pasha_attempt
from data import CONCEPT_CHECKS_V112, CLINICAL_CHALLENGES_V119, canonical_domain_v94, canonical_concept_id_v98

bp=Blueprint("pasha_review",__name__)

def _norm(s): return " ".join(re.findall(r"[a-z0-9]+",str(s or "").lower()))

def _valid_mcq(q):
    choices=q.get("choices") or []
    try: ans=int(q.get("answer"))
    except Exception: return False
    return len(choices)==4 and 0<=ans<4 and bool(q.get("stem") or q.get("prompt") or q.get("question"))

def _canonical_question(q, prefix):
    stem=q.get("stem") or q.get("prompt") or q.get("question") or ""
    choices=list(q.get("choices") or [])
    try: answer=int(q.get("answer"))
    except Exception: answer=0
    explanation=q.get("explanation") or q.get("rationale") or q.get("reveal_answer") or q.get("answer_text") or "Review the key discriminator and why the alternatives do not fit."
    domain=canonical_domain_v94(q.get("domain")) or q.get("domain") or "ENT"
    topic=q.get("topic") or q.get("title") or "Pasha review"
    raw_cid=q.get("concept_id") or topic
    try: cid=canonical_concept_id_v98(raw_cid,domain)
    except Exception: cid=raw_cid
    qid=str(q.get("id") or f"{prefix}-{abs(hash(stem))}")
    return {"id":f"{prefix}:{qid}","stem":stem,"choices":choices,"answer":answer,"explanation":str(explanation),"domain":domain,"topic":topic,"concept_id":cid}

def _source_pool():
    pool=[]
    for q in (CONCEPT_CHECKS_V112 or []):
        if _valid_mcq(q): pool.append(_canonical_question(q,"cc"))
    for q in (CLINICAL_CHALLENGES_V119 or []):
        if _valid_mcq(q): pool.append(_canonical_question(q,"challenge"))
    return pool

SOURCE_POOL=_source_pool()

def _seed_questions(chapter):
    out=[]
    for i,row in enumerate(PASHA_SEED_QUESTIONS.get(chapter["id"],[]),1):
        stem,choices,answer,explanation,section_id=row
        out.append({"id":f"pasha:{chapter['id']}:{i}","stem":stem,"choices":choices,"answer":answer,"explanation":explanation,"domain":chapter["domain"],"topic":chapter["title"],"concept_id":f"pasha-{chapter['id']}-{section_id}","section_id":section_id,"seed":True})
    return out

def _section_score(q, chapter, section):
    section_id,title,keywords=section
    if canonical_domain_v94(q.get("domain")) != canonical_domain_v94(chapter["domain"]): return 0
    hay=_norm(" ".join([q.get("topic",""),q.get("stem","")]))
    score=0
    for kw in keywords:
        nkw=_norm(kw)
        if nkw and nkw in hay: score+=8+len(nkw.split())
    title_norm=_norm(title)
    if title_norm and title_norm in hay: score+=12
    return score

def section_questions(chapter, section, target=20):
    section_id=section[0]
    candidates=[]
    for q in SOURCE_POOL:
        s=_section_score(q,chapter,section)
        if s>0:
            z=dict(q); z["section_id"]=section_id; candidates.append((s,z))
    candidates.sort(key=lambda x:(-x[0],x[1]["id"]))
    rows=[q for _,q in candidates[:target]]
    for q in _seed_questions(chapter):
        if q["section_id"]==section_id and not any(x["id"]==q["id"] for x in rows): rows.insert(0,q)
    if len(rows)<min(8,target):
        # Graceful fallback: same-domain audited questions, still clinically relevant to the chapter.
        used={x["id"] for x in rows}
        extras=[dict(q,section_id=section_id) for q in SOURCE_POOL if canonical_domain_v94(q.get("domain"))==canonical_domain_v94(chapter["domain"]) and q["id"] not in used]
        rows.extend(extras[:max(0,min(target,12)-len(rows))])
    return rows[:target]

def chapter_bank(chapter):
    rows=[]; seen=set()
    for section in chapter["sections"]:
        for q in section_questions(chapter,section,20):
            if q["id"] in seen: continue
            seen.add(q["id"]); rows.append(q)
    return rows

@bp.route("/pasha-review")
def index():
    try: ch=int(request.args.get("chapter",1))
    except Exception: ch=1
    chapter=PASHA_CHAPTER_BY_ID.get(ch) or PASHA_CHAPTERS[0]
    section_id=request.args.get("section") or ""
    mode=request.args.get("mode","chapter")
    section=None
    for s in chapter["sections"]:
        if s[0]==section_id: section=s; break
    if section:
        questions=section_questions(chapter,section,20)
    else:
        bank=chapter_bank(chapter)
        if mode=="exam":
            rng=random.Random(request.args.get("seed") or str(ch))
            questions=list(bank); rng.shuffle(questions); questions=questions[:25]
        else:
            # Chapter review: balanced sample, up to 2 per section, then fill to 20.
            questions=[]; seen=set()
            for s in chapter["sections"]:
                for q in section_questions(chapter,s,2):
                    if q["id"] not in seen: questions.append(q); seen.add(q["id"])
            for q in bank:
                if len(questions)>=20: break
                if q["id"] not in seen: questions.append(q); seen.add(q["id"])
    progress=pasha_progress()
    section_counts={}
    for s in chapter["sections"]:
        section_counts[s[0]]=len(section_questions(chapter,s,20))
    return render_template("pasha_review_dynamic.html",chapters=PASHA_CHAPTERS,chapter=chapter,section=section,mode=mode,questions=questions,progress=progress,section_counts=section_counts)

@bp.route("/api/pasha-review/answer",methods=["POST"])
def answer():
    d=request.get_json(silent=True) or {}
    try: chapter_id=int(d.get("chapter_id")); chosen=int(d.get("chosen"))
    except Exception: return jsonify({"ok":False,"error":"invalid payload"}),400
    chapter=PASHA_CHAPTER_BY_ID.get(chapter_id)
    if not chapter: return jsonify({"ok":False,"error":"unknown chapter"}),404
    qid=str(d.get("question_id") or "")
    section_id=str(d.get("section_id") or "chapter")
    bank=chapter_bank(chapter)
    q=next((x for x in bank if x["id"]==qid),None)
    if not q: return jsonify({"ok":False,"error":"unknown question"}),404
    correct=(chosen==int(q["answer"]))
    record_pasha_attempt(chapter_id,section_id,qid,q.get("concept_id"),q.get("domain"),correct)
    return jsonify({"ok":True,"correct":correct,"answer":q["answer"],"explanation":q["explanation"]})

@bp.route("/pasha-review/legacy")
def legacy():
    return redirect("/static/pasha_review.html")
