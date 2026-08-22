import os
import sqlite3
from datetime import datetime, timedelta

DATABASE_URL = os.environ.get("DATABASE_URL")
USE_POSTGRES = bool(DATABASE_URL)

if USE_POSTGRES:
    import psycopg
    from psycopg.rows import dict_row

SQLITE_PATH = os.environ.get(
    "SQLITE_PATH",
    os.path.join(os.path.dirname(__file__), "ent_mastery.db")
)

def conn():
    if USE_POSTGRES:
        return psycopg.connect(DATABASE_URL, row_factory=dict_row)
    c = sqlite3.connect(SQLITE_PATH)
    c.row_factory = sqlite3.Row
    return c

def _execute(c, sql, params=()):
    # SQLite uses ? placeholders; PostgreSQL/psycopg uses %s.
    if USE_POSTGRES:
        sql = sql.replace("?", "%s")
    return c.execute(sql, params)

def init_db():
    c = conn()
    if USE_POSTGRES:
        c.execute("""
        CREATE TABLE IF NOT EXISTS attempts (
            id BIGSERIAL PRIMARY KEY,
            question_id TEXT NOT NULL,
            concept_id TEXT NOT NULL,
            correct INTEGER NOT NULL,
            confidence INTEGER DEFAULT 3,
            miss_type TEXT,
            created_at TEXT NOT NULL
        )
        """)
        c.execute("""
        CREATE TABLE IF NOT EXISTS concepts (
            concept_id TEXT PRIMARY KEY,
            strength DOUBLE PRECISION DEFAULT 0,
            interval_days INTEGER DEFAULT 0,
            due_at TEXT,
            last_seen TEXT,
            correct_count INTEGER DEFAULT 0,
            wrong_count INTEGER DEFAULT 0
        )
        """)
    else:
        c.executescript("""
        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id TEXT NOT NULL,
            concept_id TEXT NOT NULL,
            correct INTEGER NOT NULL,
            confidence INTEGER DEFAULT 3,
            miss_type TEXT,
            created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS concepts (
            concept_id TEXT PRIMARY KEY,
            strength REAL DEFAULT 0,
            interval_days INTEGER DEFAULT 0,
            due_at TEXT,
            last_seen TEXT,
            correct_count INTEGER DEFAULT 0,
            wrong_count INTEGER DEFAULT 0
        );
        """)

    # Interpretation-lab progress is stored separately so existing question-bank
    # progress remains untouched.
    if USE_POSTGRES:
        c.execute("""
        CREATE TABLE IF NOT EXISTS lab_attempts (
            id BIGSERIAL PRIMARY KEY,
            lab_slug TEXT NOT NULL,
            case_id TEXT NOT NULL,
            concept_id TEXT NOT NULL,
            rating INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )
        """)
    else:
        c.execute("""
        CREATE TABLE IF NOT EXISTS lab_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lab_slug TEXT NOT NULL,
            case_id TEXT NOT NULL,
            concept_id TEXT NOT NULL,
            rating INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )
        """)

    # v4 dimensional mastery events. Additive only; existing progress is untouched.
    if USE_POSTGRES:
        c.execute("""
        CREATE TABLE IF NOT EXISTS mastery_events (
            id BIGSERIAL PRIMARY KEY,
            concept_id TEXT NOT NULL,
            domain TEXT,
            dimension TEXT NOT NULL,
            score INTEGER NOT NULL,
            source_type TEXT,
            source_id TEXT,
            miss_type TEXT,
            created_at TEXT NOT NULL
        )
        """)
    else:
        c.execute("""
        CREATE TABLE IF NOT EXISTS mastery_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            concept_id TEXT NOT NULL,
            domain TEXT,
            dimension TEXT NOT NULL,
            score INTEGER NOT NULL,
            source_type TEXT,
            source_id TEXT,
            miss_type TEXT,
            created_at TEXT NOT NULL
        )
        """)
    c.commit()
    c.close()

def record_attempt(question_id, concept_id, correct, confidence=3, miss_type=None):
    now = datetime.now()
    c = conn()

    _execute(
        c,
        """
        INSERT INTO attempts
        (question_id, concept_id, correct, confidence, miss_type, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            question_id,
            concept_id,
            int(bool(correct)),
            int(confidence),
            miss_type,
            now.isoformat(),
        ),
    )

    row = _execute(
        c,
        "SELECT * FROM concepts WHERE concept_id=?",
        (concept_id,),
    ).fetchone()

    if row:
        strength = float(row["strength"] or 0)
        interval = int(row["interval_days"] or 0)
        cc = int(row["correct_count"] or 0)
        wc = int(row["wrong_count"] or 0)
    else:
        strength, interval, cc, wc = 0, 0, 0, 0

    # Adaptive spaced repetition.
    # Confidently-wrong answers return sooner and lose more strength.
    if correct:
        cc += 1
        strength = min(100, strength + 12 + max(0, confidence - 3) * 2)
        interval = 1 if interval == 0 else min(
            60, max(1, round(interval * 2.15))
        )
    else:
        wc += 1
        penalty = 12 + max(0, confidence - 3) * 5
        strength = max(0, strength - penalty)
        interval = 0 if confidence >= 4 else 1

    due = now + timedelta(days=interval)

    if USE_POSTGRES:
        c.execute(
            """
            INSERT INTO concepts
            (concept_id, strength, interval_days, due_at, last_seen,
             correct_count, wrong_count)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (concept_id) DO UPDATE SET
                strength=EXCLUDED.strength,
                interval_days=EXCLUDED.interval_days,
                due_at=EXCLUDED.due_at,
                last_seen=EXCLUDED.last_seen,
                correct_count=EXCLUDED.correct_count,
                wrong_count=EXCLUDED.wrong_count
            """,
            (
                concept_id,
                strength,
                interval,
                due.isoformat(),
                now.isoformat(),
                cc,
                wc,
            ),
        )
    else:
        c.execute(
            """
            INSERT INTO concepts
            (concept_id, strength, interval_days, due_at, last_seen,
             correct_count, wrong_count)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(concept_id) DO UPDATE SET
                strength=excluded.strength,
                interval_days=excluded.interval_days,
                due_at=excluded.due_at,
                last_seen=excluded.last_seen,
                correct_count=excluded.correct_count,
                wrong_count=excluded.wrong_count
            """,
            (
                concept_id,
                strength,
                interval,
                due.isoformat(),
                now.isoformat(),
                cc,
                wc,
            ),
        )

    c.commit()
    c.close()

def stats():
    c = conn()

    total = _execute(c, "SELECT COUNT(*) AS n FROM attempts").fetchone()["n"]
    correct = _execute(
        c, "SELECT COUNT(*) AS n FROM attempts WHERE correct=1"
    ).fetchone()["n"]
    concepts = _execute(
        c, "SELECT COUNT(*) AS n FROM concepts"
    ).fetchone()["n"]
    avg = _execute(
        c, "SELECT AVG(strength) AS x FROM concepts"
    ).fetchone()["x"] or 0
    due = _execute(
        c,
        """
        SELECT COUNT(*) AS n
        FROM concepts
        WHERE due_at IS NOT NULL AND due_at <= ?
        """,
        (datetime.now().isoformat(),),
    ).fetchone()["n"]

    c.close()

    return {
        "attempts": total,
        "correct": correct,
        "accuracy": round(100 * correct / total) if total else 0,
        "concepts": concepts,
        "mastery": round(avg),
        "due": due,
    }

def mistake_rows(limit=50):
    c = conn()
    rows = _execute(
        c,
        """
        SELECT a.*
        FROM attempts a
        INNER JOIN (
            SELECT concept_id, MAX(id) AS max_id
            FROM attempts
            WHERE correct=0
            GROUP BY concept_id
        ) z ON a.id=z.max_id
        ORDER BY a.id DESC
        LIMIT ?
        """,
        (limit,),
    ).fetchall()
    c.close()
    return rows

def concept_strengths():
    c = conn()
    rows = _execute(
        c,
        "SELECT * FROM concepts ORDER BY strength ASC"
    ).fetchall()
    c.close()
    return {r["concept_id"]: dict(r) for r in rows}


def record_lab_attempt(lab_slug, case_id, concept_id, rating):
    """rating: 0 Again, 1 Hard, 2 Good, 3 Easy."""
    now=datetime.now()
    c=conn()
    _execute(c, "INSERT INTO lab_attempts (lab_slug,case_id,concept_id,rating,created_at) VALUES (?,?,?,?,?)",
             (lab_slug,case_id,concept_id,int(rating),now.isoformat()))
    c.commit(); c.close()


def lab_progress(lab_slug=None):
    c=conn()
    if lab_slug:
        rows=_execute(c, "SELECT * FROM lab_attempts WHERE lab_slug=? ORDER BY id", (lab_slug,)).fetchall()
    else:
        rows=_execute(c, "SELECT * FROM lab_attempts ORDER BY id").fetchall()
    c.close()
    out={}
    for r in rows:
        key=r["case_id"]
        x=out.setdefault(key,{"attempts":0,"last_rating":None,"avg_rating":0.0,"last_seen":None,"sum":0})
        x["attempts"]+=1; x["sum"]+=int(r["rating"]); x["last_rating"]=int(r["rating"]); x["last_seen"]=r["created_at"]
        x["avg_rating"]=round(x["sum"]/x["attempts"],2)
    return out


def lab_stats(lab_slug):
    p=lab_progress(lab_slug)
    attempted=len(p)
    weak=sum(1 for x in p.values() if x["last_rating"] is not None and x["last_rating"] <= 1)
    mastered=sum(1 for x in p.values() if x["attempts"] >= 2 and x["avg_rating"] >= 2.5)
    return {"attempted":attempted,"weak":weak,"mastered":mastered}


def record_mastery_event(concept_id, domain, dimension, score,
                         source_type=None, source_id=None, miss_type=None):
    now=datetime.now().isoformat()
    score=max(0,min(3,int(score)))
    c=conn()
    _execute(c, """INSERT INTO mastery_events
        (concept_id,domain,dimension,score,source_type,source_id,miss_type,created_at)
        VALUES (?,?,?,?,?,?,?,?)""",
        (concept_id,domain,dimension,score,source_type,source_id,miss_type,now))
    c.commit(); c.close()

def mastery_profiles():
    c=conn()
    rows=_execute(c, "SELECT * FROM mastery_events ORDER BY id").fetchall()
    c.close()
    concepts={}
    for r in rows:
        cid=r["concept_id"]; dim=r["dimension"]
        x=concepts.setdefault(cid,{"concept_id":cid,"domain":r["domain"] or "ENT","dimensions":{},"events":0,"overall":0})
        d=x["dimensions"].setdefault(dim,{"scores":[],"score":0,"events":0,"last":None})
        s=int(r["score"]); d["scores"].append(s); d["events"]+=1; d["last"]=r["created_at"]
        recent=d["scores"][-4:]; weights=list(range(1,len(recent)+1))
        d["score"]=round(100*sum(a*w for a,w in zip(recent,weights))/(3*sum(weights))) if weights else 0
        x["events"]+=1
    for x in concepts.values():
        vals=[d["score"] for d in x["dimensions"].values()]
        x["overall"]=round(sum(vals)/len(vals)) if vals else 0
    return concepts

def dimension_summary():
    profiles=mastery_profiles(); dims={}
    for p in profiles.values():
        for dim,d in p["dimensions"].items():
            dims.setdefault(dim,[]).append(d["score"])
    return {dim:round(sum(vals)/len(vals)) if vals else 0 for dim,vals in dims.items()}

def domain_mastery():
    profiles=mastery_profiles(); by={}
    for p in profiles.values():
        by.setdefault(p["domain"],[]).append(p["overall"])
    return {d:round(sum(v)/len(v)) if v else 0 for d,v in by.items()}

def mastery_misses(limit=100):
    c=conn()
    rows=_execute(c, """SELECT * FROM mastery_events
        WHERE score <= 1 OR miss_type IS NOT NULL ORDER BY id DESC LIMIT ?""",(limit,)).fetchall()
    c.close()
    return [dict(r) for r in rows]


# =============================================================================
# v6 adaptive curriculum persistence
# =============================================================================
def ensure_adaptive_schema():
    conn=get_conn()
    cur=conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS curriculum_mastery (
        concept_id TEXT PRIMARY KEY,
        domain TEXT,
        topic TEXT,
        mastery_level INTEGER DEFAULT 0,
        attempts INTEGER DEFAULT 0,
        correct INTEGER DEFAULT 0,
        last_seen TIMESTAMP,
        next_due DATE
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS daily_path_events (
        id SERIAL PRIMARY KEY,
        concept_id TEXT,
        item_id TEXT,
        stage TEXT,
        rating INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit(); conn.close()

def adaptive_mastery_map():
    ensure_adaptive_schema()
    conn=get_conn(); cur=conn.cursor()
    cur.execute("SELECT concept_id, domain, topic, mastery_level, attempts, correct, last_seen, next_due FROM curriculum_mastery")
    rows=cur.fetchall(); conn.close()
    keys=["concept_id","domain","topic","mastery_level","attempts","correct","last_seen","next_due"]
    return {r[0]:dict(zip(keys,r)) for r in rows}

def record_adaptive_result(concept_id, item_id, domain, topic, stage, level, rating, interval_days):
    ensure_adaptive_schema()
    conn=get_conn(); cur=conn.cursor()
    # rating: 0 miss, 1 hard, 2 good, 3 easy
    cur.execute("""INSERT INTO daily_path_events(concept_id,item_id,stage,rating) VALUES(%s,%s,%s,%s)""",
                (concept_id,item_id,stage,rating))
    cur.execute("SELECT mastery_level, attempts, correct FROM curriculum_mastery WHERE concept_id=%s",(concept_id,))
    row=cur.fetchone()
    old_level=(row[0] if row else 0); attempts=(row[1] if row else 0)+1; correct=(row[2] if row else 0)+(1 if rating>=2 else 0)
    if rating==0: new_level=max(0,min(old_level,level)-1); days=1
    elif rating==1: new_level=max(old_level,min(level,6)); days=max(1,interval_days//2)
    elif rating==2: new_level=max(old_level,min(level,6)); days=interval_days
    else: new_level=max(old_level,min(level+1,6)); days=min(90,max(interval_days,1)*2)
    cur.execute("""INSERT INTO curriculum_mastery(concept_id,domain,topic,mastery_level,attempts,correct,last_seen,next_due)
                   VALUES(%s,%s,%s,%s,%s,%s,CURRENT_TIMESTAMP,CURRENT_DATE + %s)
                   ON CONFLICT(concept_id) DO UPDATE SET domain=EXCLUDED.domain,topic=EXCLUDED.topic,
                   mastery_level=EXCLUDED.mastery_level,attempts=EXCLUDED.attempts,correct=EXCLUDED.correct,
                   last_seen=CURRENT_TIMESTAMP,next_due=EXCLUDED.next_due""",
                (concept_id,domain,topic,new_level,attempts,correct,days))
    conn.commit(); conn.close()
    return new_level
