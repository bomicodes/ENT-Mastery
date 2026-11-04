import random, re
from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from pasha_review_data import PASHA_CHAPTERS, PASHA_CHAPTER_BY_ID, PASHA_SEED_QUESTIONS
from pasha_db import pasha_progress, record_pasha_attempt
import data as _data_module
from data import canonical_domain_v94, canonical_concept_id_v98

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

# v43.4: this module was imported (and SOURCE_POOL snapshotted) partway through
# the runtime_entry_pasha patch chain, before dozens of later patches finished
# appending to CONCEPT_CHECKS_V112/CLINICAL_CHALLENGES_V119 -- confirmed live at
# 1866 vs. 1929 valid live MCQs in the patch author's final boot audit.
# Recompute from the live data module instead of a one-time snapshot, cached and
# invalidated when either bank changes identity or size. Later patches sometimes
# replace a whole list with a new one of the same length.
_SOURCE_POOL_CACHE={"key":None,"pool":[]}

def _build_source_pool():
    pool=[]
    for q in (_data_module.CONCEPT_CHECKS_V112 or []):
        if _valid_mcq(q): pool.append(_canonical_question(q,"cc"))
    for q in (_data_module.CLINICAL_CHALLENGES_V119 or []):
        if _valid_mcq(q): pool.append(_canonical_question(q,"challenge"))
    return pool

def _source_pool():
    checks=_data_module.CONCEPT_CHECKS_V112
    challenges=_data_module.CLINICAL_CHALLENGES_V119
    key=(id(checks), len(checks or []), id(challenges), len(challenges or []))
    if _SOURCE_POOL_CACHE["key"] != key:
        _SOURCE_POOL_CACHE["pool"]=_build_source_pool()
        _SOURCE_POOL_CACHE["key"]=key
    return _SOURCE_POOL_CACHE["pool"]

import hashlib as _hashlib

def _stable_shuffle(stem, choices, answer):
    """Deterministic per-question shuffle so section-specific answers are not stuck in one position."""
    order=list(range(len(choices)))
    random.Random(int(_hashlib.md5(stem.encode()).hexdigest()[:8],16)).shuffle(order)
    return [choices[i] for i in order], order.index(answer)

def _seed_questions(chapter):
    """Book-specific questions: section-specific ones (v64) first, then the original chapter seeds."""
    out=[]
    try:
        from pasha_extra_questions_v640 import EXTRA_QUESTIONS_V640
    except Exception:
        EXTRA_QUESTIONS_V640={}
    sids={s[0] for s in chapter["sections"]}
    for sid,rows in EXTRA_QUESTIONS_V640.items():
        if sid not in sids: continue
        for j,(stem,choices,answer,explanation) in enumerate(rows,1):
            ch,ans=_stable_shuffle(stem,list(choices),answer)
            out.append({"id":f"pasha:{chapter['id']}:{sid}:{j}","stem":stem,"choices":ch,"answer":ans,"explanation":explanation,"domain":chapter["domain"],"topic":chapter["title"],"concept_id":f"pasha-{chapter['id']}-{sid}","section_id":sid,"seed":True})
    for i,row in enumerate(PASHA_SEED_QUESTIONS.get(chapter["id"],[]),1):
        stem,choices,answer,explanation,section_id=row
        ch,ans=_stable_shuffle(stem,list(choices),answer)
        out.append({"id":f"pasha:{chapter['id']}:{i}","stem":stem,"choices":ch,"answer":ans,"explanation":explanation,"domain":chapter["domain"],"topic":chapter["title"],"concept_id":f"pasha-{chapter['id']}-{section_id}","section_id":section_id,"seed":True,"chapter_seed":True})
    return out

def _section_score(q, chapter, section):
    """Keyword relevance, used to order questions and to place image-review items."""
    section_id,title,keywords=section
    hay=_norm(" ".join([q.get("topic",""),q.get("stem","")]))
    score=0
    for kw in keywords:
        nkw=_norm(kw)
        if nkw and nkw in hay: score+=8+len(nkw.split())
    title_norm=_norm(title)
    if title_norm and title_norm in hay: score+=12
    return score

def _section_topics(section_id):
    from pasha_section_map_v640 import SECTION_TOPICS_V640
    return SECTION_TOPICS_V640.get(section_id, [])

def _tokens(text):
    return set(w for w in _norm(text).split() if len(w)>3)

def _near_duplicate(stem, kept):
    a=_tokens(stem)
    if not a: return False
    for b in kept:
        if len(a & b)/max(1,len(a | b)) >= 0.6: return True
    return False

_HOME_CACHE={}

def _chapter_assignment(chapter):
    """v64: each bank question gets one home section per chapter, so the same question does not
    appear in several section quizzes. Image-review items, which span a whole chapter, only go
    to a section whose keywords they match."""
    pool=_source_pool()
    key=(chapter["id"], _SOURCE_POOL_CACHE["key"])
    if key in _HOME_CACHE: return _HOME_CACHE[key]
    best={}
    for si,section in enumerate(chapter["sections"]):
        topics=_section_topics(section[0])
        pos={t:i for i,t in enumerate(topics)}
        for q in pool:
            t=q["topic"]
            if t not in pos: continue
            sc=_section_score(q,chapter,section)
            if t.startswith("Image review") and sc<=0: continue
            rank=(-sc, pos[t], si)
            if q["id"] not in best or rank<best[q["id"]][0]:
                best[q["id"]]=(rank, section[0])
    home={}
    for q in pool:
        b=best.get(q["id"])
        if b: home.setdefault(b[1],[]).append(q)
    _HOME_CACHE.clear(); _HOME_CACHE[key]=home
    return home

def section_questions(chapter, section, target=20):
    """v64: section-specific book questions first, then bank questions from the topics mapped to
    this section (each question in one section only), spread round-robin over the topics in map
    order, skipping near-duplicates. The original chapter seed questions go last. No filler."""
    section_id=section[0]
    topics=_section_topics(section_id)
    mine=_chapter_assignment(chapter).get(section_id,[])
    by_topic={}
    for q in mine:
        z=dict(q); z["section_id"]=section_id
        by_topic.setdefault(q["topic"],[]).append((-_section_score(q,chapter,section),z["id"],z))
    queues=[[z for _,_,z in sorted(by_topic[t])] for t in topics if t in by_topic]
    seeds=[q for q in _seed_questions(chapter) if q["section_id"]==section_id]
    rows=[q for q in seeds if not q.get("chapter_seed")]
    kept=[_tokens(q["stem"]) for q in rows]
    i=0
    while len(rows)<target and any(queues):
        qq=queues[i%len(queues)]
        if qq:
            z=qq.pop(0)
            if not _near_duplicate(z["stem"],kept):
                rows.append(z); kept.append(_tokens(z["stem"]))
        i+=1
    for q in seeds:
        if q.get("chapter_seed") and len(rows)<target: rows.append(q)
    return rows[:target]

def chapter_bank(chapter):
    rows=[]; seen=set()
    for section in chapter["sections"]:
        for q in section_questions(chapter,section,20):
            if q["id"] in seen: continue
            seen.add(q["id"]); rows.append(q)
    return rows

def concept_check_questions(chapter, per_section=2, cap=14):
    """Short, finite post-reading retrieval check, with subsection attribution."""
    rows=[]; seen=set()
    for section in chapter["sections"]:
        for q in section_questions(chapter,section,per_section):
            if q["id"] in seen: continue
            seen.add(q["id"]); rows.append(q)
    return rows[:cap]

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
    if mode=="check":
        questions=section_questions(chapter,section,8) if section else concept_check_questions(chapter)
    elif section:
        questions=section_questions(chapter,section,20)
    else:
        bank=chapter_bank(chapter)
        if mode=="exam":
            rng=random.Random(request.args.get("seed") or str(ch))
            questions=list(bank); rng.shuffle(questions); questions=questions[:25]
        else:
            questions=[]; seen=set()
            for s in chapter["sections"]:
                for q in section_questions(chapter,s,2):
                    if q["id"] not in seen: questions.append(q); seen.add(q["id"])
            for q in bank:
                if len(questions)>=20: break
                if q["id"] not in seen: questions.append(q); seen.add(q["id"])
    progress=pasha_progress()
    section_counts={s[0]:len(section_questions(chapter,s,20)) for s in chapter["sections"]}
    section_titles={s[0]:s[1] for s in chapter["sections"]}
    concept_check_count=len(concept_check_questions(chapter))
    return render_template("pasha_review_dynamic.html",chapters=PASHA_CHAPTERS,chapter=chapter,section=section,mode=mode,questions=questions,progress=progress,section_counts=section_counts,section_titles=section_titles,concept_check_count=concept_check_count)

@bp.route("/api/pasha-review/answer",methods=["POST"])
def answer():
    d=request.get_json(silent=True) or {}
    try: chapter_id=int(d.get("chapter_id")); chosen=int(d.get("chosen"))
    except Exception: return jsonify({"ok":False,"error":"invalid payload"}),400
    chapter=PASHA_CHAPTER_BY_ID.get(chapter_id)
    if not chapter: return jsonify({"ok":False,"error":"unknown chapter"}),404
    qid=str(d.get("question_id") or "")
    section_id=str(d.get("section_id") or "chapter")
    if section_id not in {s[0] for s in chapter["sections"]}:
        return jsonify({"ok":False,"error":"unknown section"}),400
    bank=chapter_bank(chapter)
    q=next((x for x in bank if x["id"]==qid),None)
    if not q: return jsonify({"ok":False,"error":"unknown question"}),404
    if chosen not in range(len(q["choices"])): return jsonify({"ok":False,"error":"invalid choice"}),400
    if qid not in {item["id"] for s in chapter["sections"] if s[0]==section_id for item in section_questions(chapter,s,20)}:
        return jsonify({"ok":False,"error":"question does not belong to section"}),400
    correct=(chosen==int(q["answer"]))
    record_pasha_attempt(chapter_id,section_id,qid,q.get("concept_id"),q.get("domain"),correct)
    return jsonify({"ok":True,"correct":correct,"answer":q["answer"],"explanation":q["explanation"]})

@bp.route("/pasha-review/legacy")
def legacy():
    return redirect("/static/pasha_review.html")
