"""Database persistence for the Pasha review companion."""
from datetime import datetime
from db import conn, _execute, USE_POSTGRES, record_mastery_event


def ensure_pasha_schema():
    c=conn()
    if USE_POSTGRES:
        c.execute("""CREATE TABLE IF NOT EXISTS pasha_attempts (
            id BIGSERIAL PRIMARY KEY,
            chapter_id INTEGER NOT NULL,
            section_id TEXT NOT NULL,
            question_id TEXT NOT NULL,
            concept_id TEXT,
            domain TEXT,
            correct INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )""")
    else:
        c.execute("""CREATE TABLE IF NOT EXISTS pasha_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chapter_id INTEGER NOT NULL,
            section_id TEXT NOT NULL,
            question_id TEXT NOT NULL,
            concept_id TEXT,
            domain TEXT,
            correct INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )""")
    c.commit(); c.close()


def record_pasha_attempt(chapter_id, section_id, question_id, concept_id, domain, correct):
    ensure_pasha_schema()
    c=conn()
    _execute(c,"""INSERT INTO pasha_attempts
        (chapter_id,section_id,question_id,concept_id,domain,correct,created_at)
        VALUES (?,?,?,?,?,?,?)""",
        (int(chapter_id),str(section_id),str(question_id),concept_id,domain,int(bool(correct)),datetime.now().isoformat()))
    c.commit(); c.close()
    if concept_id:
        try:
            record_mastery_event(concept_id,domain or "ENT","reasoning",3 if correct else 0,
                                 source_type="pasha_review",source_id=question_id,
                                 miss_type=None if correct else "retrieval")
        except Exception:
            pass


def pasha_progress():
    ensure_pasha_schema(); c=conn()
    rows=_execute(c,"SELECT * FROM pasha_attempts ORDER BY id").fetchall(); c.close()
    out={"total_attempts":0,"total_correct":0,"chapters":{},"sections":{},"questions":{}}
    for r0 in rows:
        r=dict(r0); out["total_attempts"]+=1; out["total_correct"]+=int(r["correct"])
        ch=str(r["chapter_id"]); sec=f"{ch}:{r['section_id']}"; qid=r["question_id"]
        cq=out["chapters"].setdefault(ch,{"attempts":0,"correct":0,"unique":set()})
        cq["attempts"]+=1; cq["correct"]+=int(r["correct"]); cq["unique"].add(qid)
        sq=out["sections"].setdefault(sec,{"attempts":0,"correct":0,"unique":set()})
        sq["attempts"]+=1; sq["correct"]+=int(r["correct"]); sq["unique"].add(qid)
        out["questions"][qid]={"correct":bool(r["correct"]),"created_at":r["created_at"]}
    for bucket in (out["chapters"],out["sections"]):
        for x in bucket.values():
            x["unique"]=len(x["unique"]); x["accuracy"]=round(100*x["correct"]/x["attempts"]) if x["attempts"] else 0
    out["accuracy"]=round(100*out["total_correct"]/out["total_attempts"]) if out["total_attempts"] else 0
    return out
