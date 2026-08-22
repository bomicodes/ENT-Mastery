import os, sqlite3
from datetime import datetime, timedelta

DB_PATH = os.environ.get("DATABASE_PATH", os.path.join(os.path.dirname(__file__), "ent_mastery.db"))

def conn():
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c

def init_db():
    c = conn()
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
    c.commit()
    c.close()

def record_attempt(question_id, concept_id, correct, confidence=3, miss_type=None):
    now = datetime.now()
    c = conn()
    c.execute(
        "INSERT INTO attempts(question_id,concept_id,correct,confidence,miss_type,created_at) VALUES (?,?,?,?,?,?)",
        (question_id, concept_id, int(bool(correct)), int(confidence), miss_type, now.isoformat())
    )
    row = c.execute("SELECT * FROM concepts WHERE concept_id=?", (concept_id,)).fetchone()
    if row:
        strength = float(row["strength"] or 0)
        interval = int(row["interval_days"] or 0)
        cc = int(row["correct_count"] or 0)
        wc = int(row["wrong_count"] or 0)
    else:
        strength, interval, cc, wc = 0, 0, 0, 0

    # Lightweight adaptive SRS. Confidently-wrong answers return fastest.
    if correct:
        cc += 1
        strength = min(100, strength + 12 + max(0, confidence-3)*2)
        interval = 1 if interval == 0 else min(60, max(1, round(interval * 2.15)))
    else:
        wc += 1
        penalty = 12 + max(0, confidence-3)*5
        strength = max(0, strength - penalty)
        interval = 0 if confidence >= 4 else 1

    due = now + timedelta(days=interval)
    c.execute("""
        INSERT INTO concepts(concept_id,strength,interval_days,due_at,last_seen,correct_count,wrong_count)
        VALUES (?,?,?,?,?,?,?)
        ON CONFLICT(concept_id) DO UPDATE SET
          strength=excluded.strength,
          interval_days=excluded.interval_days,
          due_at=excluded.due_at,
          last_seen=excluded.last_seen,
          correct_count=excluded.correct_count,
          wrong_count=excluded.wrong_count
    """, (concept_id, strength, interval, due.isoformat(), now.isoformat(), cc, wc))
    c.commit()
    c.close()

def stats():
    c = conn()
    total = c.execute("SELECT COUNT(*) n FROM attempts").fetchone()["n"]
    correct = c.execute("SELECT COUNT(*) n FROM attempts WHERE correct=1").fetchone()["n"]
    concepts = c.execute("SELECT COUNT(*) n FROM concepts").fetchone()["n"]
    avg = c.execute("SELECT AVG(strength) x FROM concepts").fetchone()["x"] or 0
    due = c.execute("SELECT COUNT(*) n FROM concepts WHERE due_at IS NOT NULL AND due_at <= ?", (datetime.now().isoformat(),)).fetchone()["n"]
    c.close()
    return {"attempts": total, "correct": correct, "accuracy": round(100*correct/total) if total else 0,
            "concepts": concepts, "mastery": round(avg), "due": due}

def mistake_rows(limit=50):
    c = conn()
    rows = c.execute("""
        SELECT a.* FROM attempts a
        INNER JOIN (
          SELECT concept_id, MAX(id) max_id FROM attempts WHERE correct=0 GROUP BY concept_id
        ) z ON a.id=z.max_id
        ORDER BY a.id DESC LIMIT ?
    """, (limit,)).fetchall()
    c.close()
    return rows

def concept_strengths():
    c = conn()
    rows = c.execute("SELECT * FROM concepts ORDER BY strength ASC").fetchall()
    c.close()
    return {r["concept_id"]: dict(r) for r in rows}
