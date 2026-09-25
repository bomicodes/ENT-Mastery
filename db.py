import os
import sqlite3
from datetime import datetime, timedelta

DATABASE_URL = os.environ.get("DATABASE_URL")
USE_POSTGRES = bool(DATABASE_URL)

# v44.4 multi-user accounts. LEGACY_USER_ID is where every attempt/mastery row
# lived before accounts existed; it stays a valid, permanent "Legacy / Shared"
# account so no pre-existing progress is lost when accounts are introduced.
LEGACY_USER_ID = 1


def _current_user_id():
    """Resolve the acting user for this call.

    Reads the logged-in user from the active Flask session when one exists.
    Falls back to LEGACY_USER_ID outside a request context (scripts, audits,
    the pre-accounts shared-progress bucket) so every existing db.py caller
    keeps working unmodified.
    """
    if os.environ.get("ENT_MASTERY_AUDIT_MODE") == "1":
        return LEGACY_USER_ID
    try:
        from flask import has_request_context, session
        if has_request_context():
            uid = session.get("user_id")
            if uid:
                return int(uid)
    except Exception:
        pass
    return LEGACY_USER_ID

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

def _table_columns(c, table):
    if USE_POSTGRES:
        rows = c.execute(
            "SELECT column_name FROM information_schema.columns WHERE table_name=%s",
            (table,),
        ).fetchall()
        return {r["column_name"] if isinstance(r, dict) else r[0] for r in rows}
    rows = c.execute(f"PRAGMA table_info({table})").fetchall()
    return {r[1] for r in rows}


def _table_exists(c, table):
    if USE_POSTGRES:
        row = c.execute(
            "SELECT 1 FROM information_schema.tables WHERE table_name=%s", (table,)
        ).fetchone()
        return row is not None
    row = c.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (table,)
    ).fetchone()
    return row is not None


def _init_users_table(c):
    if USE_POSTGRES:
        c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id BIGSERIAL PRIMARY KEY,
            email TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'resident',
            created_at TEXT NOT NULL
        )
        """)
    else:
        c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'resident',
            created_at TEXT NOT NULL
        )
        """)
    # Seed the permanent "Legacy / Shared" account (id=1) that every row of
    # progress recorded before accounts existed is attributed to. It has no
    # usable password (empty hash never matches check_password_hash), so it
    # cannot be logged into directly -- it exists only to hold history.
    existing = _execute(c, "SELECT id FROM users WHERE id=?", (LEGACY_USER_ID,)).fetchone()
    if not existing:
        if USE_POSTGRES:
            c.execute(
                "INSERT INTO users (id, email, name, password_hash, role, created_at) "
                "VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING",
                (LEGACY_USER_ID, "legacy@ent-mastery.local", "Legacy / Shared", "", "legacy", datetime.now().isoformat()),
            )
            # An explicit id does not advance PostgreSQL's BIGSERIAL sequence.
            # Without this, the first real resident would try to reuse id=1.
            c.execute("SELECT setval(pg_get_serial_sequence('users', 'id'), "
                      "GREATEST((SELECT MAX(id) FROM users), 1))")
        else:
            c.execute(
                "INSERT OR IGNORE INTO users (id, email, name, password_hash, role, created_at) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (LEGACY_USER_ID, "legacy@ent-mastery.local", "Legacy / Shared", "", "legacy", datetime.now().isoformat()),
            )

    # v44.5: PIN-based accounts. password_hash/email stay on the table (a chief
    # could still be added the old way), but residents are now created with a
    # short PIN instead -- pin_hash is nullable so it coexists with any
    # already-created password accounts without a migration branch per login
    # style.
    if "pin_hash" not in _table_columns(c, "users"):
        c.execute("ALTER TABLE users ADD COLUMN pin_hash TEXT")


def _add_user_id_column(c, table):
    """Idempotently add a `user_id INTEGER DEFAULT 1` column to a surrogate-key table."""
    if "user_id" in _table_columns(c, table):
        return
    if USE_POSTGRES:
        c.execute(f"ALTER TABLE {table} ADD COLUMN user_id BIGINT DEFAULT {LEGACY_USER_ID}")
    else:
        c.execute(f"ALTER TABLE {table} ADD COLUMN user_id INTEGER DEFAULT {LEGACY_USER_ID}")
    _execute(c, f"UPDATE {table} SET user_id=? WHERE user_id IS NULL", (LEGACY_USER_ID,))


def _rekey_concept_table(c, table, extra_cols_sql, extra_col_names):
    """Rebuild a concept_id-primary-keyed table with a (user_id, concept_id) key.

    `concepts` and `curriculum_mastery` predate accounts and use concept_id as
    their sole primary key -- one row per concept, shared by everyone. Adding
    per-user history means each user needs their own row per concept, so the
    primary key has to become (user_id, concept_id). Neither SQLite nor
    Postgres can just ALTER a primary key in place, so this recreates the
    table, copies every existing row in under the Legacy/Shared user, and
    swaps it in. Idempotent: skipped entirely once user_id already exists.
    """
    if "user_id" in _table_columns(c, table):
        return
    cols_csv = ", ".join(extra_col_names)
    if USE_POSTGRES:
        # Build under a distinct name. Renaming the old table first leaves its
        # primary-key index named <table>_pkey, which conflicts with the new
        # table's automatically generated index on PostgreSQL.
        new_table = f"{table}_accounts_new"
        c.execute(f"""
        CREATE TABLE {new_table} (
            user_id BIGINT NOT NULL DEFAULT {LEGACY_USER_ID},
            {extra_cols_sql},
            PRIMARY KEY (user_id, concept_id)
        )
        """)
        c.execute(f"INSERT INTO {new_table} (user_id, {cols_csv}) SELECT {LEGACY_USER_ID}, {cols_csv} FROM {table}")
        c.execute(f"DROP TABLE {table}")
        c.execute(f"ALTER TABLE {new_table} RENAME TO {table}")
    else:
        c.execute(f"ALTER TABLE {table} RENAME TO {table}_pre_accounts")
        c.execute(f"""
        CREATE TABLE {table} (
            user_id INTEGER NOT NULL DEFAULT {LEGACY_USER_ID},
            {extra_cols_sql},
            PRIMARY KEY (user_id, concept_id)
        )
        """)
        c.execute(f"INSERT INTO {table} (user_id, {cols_csv}) SELECT {LEGACY_USER_ID}, {cols_csv} FROM {table}_pre_accounts")
        c.execute(f"DROP TABLE {table}_pre_accounts")


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

    # v44.4 multi-user accounts: users table + per-user scoping migration.
    # Idempotent and additive -- every existing row of progress is preserved
    # and attributed to the permanent "Legacy / Shared" account (id=1).
    _init_users_table(c)
    _add_user_id_column(c, "attempts")
    _rekey_concept_table(
        c, "concepts",
        "concept_id TEXT NOT NULL, strength " + ("DOUBLE PRECISION" if USE_POSTGRES else "REAL") + " DEFAULT 0, "
        "interval_days INTEGER DEFAULT 0, due_at TEXT, last_seen TEXT, "
        "correct_count INTEGER DEFAULT 0, wrong_count INTEGER DEFAULT 0",
        ["concept_id", "strength", "interval_days", "due_at", "last_seen", "correct_count", "wrong_count"],
    )
    _add_user_id_column(c, "lab_attempts")
    _add_user_id_column(c, "mastery_events")
    c.commit()
    c.close()

def record_attempt(question_id, concept_id, correct, confidence=3, miss_type=None, user_id=None):
    now = datetime.now()
    uid = user_id if user_id is not None else _current_user_id()
    c = conn()

    _execute(
        c,
        """
        INSERT INTO attempts
        (user_id, question_id, concept_id, correct, confidence, miss_type, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            uid,
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
        "SELECT * FROM concepts WHERE concept_id=? AND user_id=?",
        (concept_id, uid),
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
            (user_id, concept_id, strength, interval_days, due_at, last_seen,
             correct_count, wrong_count)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (user_id, concept_id) DO UPDATE SET
                strength=EXCLUDED.strength,
                interval_days=EXCLUDED.interval_days,
                due_at=EXCLUDED.due_at,
                last_seen=EXCLUDED.last_seen,
                correct_count=EXCLUDED.correct_count,
                wrong_count=EXCLUDED.wrong_count
            """,
            (
                uid,
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
            (user_id, concept_id, strength, interval_days, due_at, last_seen,
             correct_count, wrong_count)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(user_id, concept_id) DO UPDATE SET
                strength=excluded.strength,
                interval_days=excluded.interval_days,
                due_at=excluded.due_at,
                last_seen=excluded.last_seen,
                correct_count=excluded.correct_count,
                wrong_count=excluded.wrong_count
            """,
            (
                uid,
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

def stats(user_id=None):
    uid = user_id if user_id is not None else _current_user_id()
    c = conn()

    total = _execute(c, "SELECT COUNT(*) AS n FROM attempts WHERE user_id=?", (uid,)).fetchone()["n"]
    correct = _execute(
        c, "SELECT COUNT(*) AS n FROM attempts WHERE correct=1 AND user_id=?", (uid,)
    ).fetchone()["n"]
    concepts = _execute(
        c, "SELECT COUNT(*) AS n FROM concepts WHERE user_id=?", (uid,)
    ).fetchone()["n"]
    avg = _execute(
        c, "SELECT AVG(strength) AS x FROM concepts WHERE user_id=?", (uid,)
    ).fetchone()["x"] or 0
    due = _execute(
        c,
        """
        SELECT COUNT(*) AS n
        FROM concepts
        WHERE due_at IS NOT NULL AND due_at <= ? AND user_id=?
        """,
        (datetime.now().isoformat(), uid),
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

def mistake_rows(limit=50, user_id=None):
    uid = user_id if user_id is not None else _current_user_id()
    c = conn()
    rows = _execute(
        c,
        """
        SELECT a.*
        FROM attempts a
        INNER JOIN (
            SELECT concept_id, MAX(id) AS max_id
            FROM attempts
            WHERE correct=0 AND user_id=?
            GROUP BY concept_id
        ) z ON a.id=z.max_id
        ORDER BY a.id DESC
        LIMIT ?
        """,
        (uid, limit),
    ).fetchall()
    c.close()
    return rows

def concept_strengths(user_id=None):
    uid = user_id if user_id is not None else _current_user_id()
    c = conn()
    rows = _execute(
        c,
        "SELECT * FROM concepts WHERE user_id=? ORDER BY strength ASC", (uid,)
    ).fetchall()
    c.close()
    return {r["concept_id"]: dict(r) for r in rows}


def record_lab_attempt(lab_slug, case_id, concept_id, rating, user_id=None):
    """rating: 0 Again, 1 Hard, 2 Good, 3 Easy."""
    now=datetime.now()
    uid = user_id if user_id is not None else _current_user_id()
    c=conn()
    _execute(c, "INSERT INTO lab_attempts (user_id,lab_slug,case_id,concept_id,rating,created_at) VALUES (?,?,?,?,?,?)",
             (uid,lab_slug,case_id,concept_id,int(rating),now.isoformat()))
    c.commit(); c.close()


def lab_progress(lab_slug=None, user_id=None):
    uid = user_id if user_id is not None else _current_user_id()
    c=conn()
    if lab_slug:
        rows=_execute(c, "SELECT * FROM lab_attempts WHERE lab_slug=? AND user_id=? ORDER BY id", (lab_slug,uid)).fetchall()
    else:
        rows=_execute(c, "SELECT * FROM lab_attempts WHERE user_id=? ORDER BY id", (uid,)).fetchall()
    c.close()
    out={}
    for r in rows:
        key=r["case_id"]
        x=out.setdefault(key,{"attempts":0,"last_rating":None,"avg_rating":0.0,"last_seen":None,"sum":0})
        x["attempts"]+=1; x["sum"]+=int(r["rating"]); x["last_rating"]=int(r["rating"]); x["last_seen"]=r["created_at"]
        x["avg_rating"]=round(x["sum"]/x["attempts"],2)
    return out


def lab_stats(lab_slug, user_id=None):
    p=lab_progress(lab_slug, user_id=user_id)
    attempted=len(p)
    weak=sum(1 for x in p.values() if x["last_rating"] is not None and x["last_rating"] <= 1)
    mastered=sum(1 for x in p.values() if x["attempts"] >= 2 and x["avg_rating"] >= 2.5)
    return {"attempted":attempted,"weak":weak,"mastered":mastered}


def record_mastery_event(concept_id, domain, dimension, score,
                         source_type=None, source_id=None, miss_type=None, user_id=None):
    now=datetime.now().isoformat()
    score=max(0,min(3,int(score)))
    uid = user_id if user_id is not None else _current_user_id()
    c=conn()
    _execute(c, """INSERT INTO mastery_events
        (user_id,concept_id,domain,dimension,score,source_type,source_id,miss_type,created_at)
        VALUES (?,?,?,?,?,?,?,?,?)""",
        (uid,concept_id,domain,dimension,score,source_type,source_id,miss_type,now))
    c.commit(); c.close()

def mastery_profiles(user_id=None):
    uid = user_id if user_id is not None else _current_user_id()
    c=conn()
    rows=_execute(c, "SELECT * FROM mastery_events WHERE user_id=? ORDER BY id", (uid,)).fetchall()
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

def dimension_summary(user_id=None):
    profiles=mastery_profiles(user_id=user_id); dims={}
    for p in profiles.values():
        for dim,d in p["dimensions"].items():
            dims.setdefault(dim,[]).append(d["score"])
    return {dim:round(sum(vals)/len(vals)) if vals else 0 for dim,vals in dims.items()}

def domain_mastery(user_id=None):
    profiles=mastery_profiles(user_id=user_id); by={}
    for p in profiles.values():
        by.setdefault(p["domain"],[]).append(p["overall"])
    return {d:round(sum(v)/len(v)) if v else 0 for d,v in by.items()}

def mastery_misses(limit=100, user_id=None):
    uid = user_id if user_id is not None else _current_user_id()
    c=conn()
    rows=_execute(c, """SELECT * FROM mastery_events
        WHERE (score <= 1 OR miss_type IS NOT NULL) AND user_id=? ORDER BY id DESC LIMIT ?""",(uid,limit)).fetchall()
    c.close()
    return [dict(r) for r in rows]


# =============================================================================
# v6/v9.2 adaptive curriculum persistence
# =============================================================================
def ensure_adaptive_schema():
    c=conn()
    if USE_POSTGRES:
        c.execute("""CREATE TABLE IF NOT EXISTS curriculum_mastery (
            concept_id TEXT PRIMARY KEY, domain TEXT, topic TEXT,
            mastery_level INTEGER DEFAULT 0, attempts INTEGER DEFAULT 0,
            correct INTEGER DEFAULT 0, last_seen TIMESTAMP, next_due DATE
        )""")
        c.execute("""CREATE TABLE IF NOT EXISTS daily_path_events (
            id BIGSERIAL PRIMARY KEY, concept_id TEXT, item_id TEXT,
            stage TEXT, rating INTEGER, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")
    else:
        c.execute("""CREATE TABLE IF NOT EXISTS curriculum_mastery (
            concept_id TEXT PRIMARY KEY, domain TEXT, topic TEXT,
            mastery_level INTEGER DEFAULT 0, attempts INTEGER DEFAULT 0,
            correct INTEGER DEFAULT 0, last_seen TEXT, next_due TEXT
        )""")
        c.execute("""CREATE TABLE IF NOT EXISTS daily_path_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT, concept_id TEXT, item_id TEXT,
            stage TEXT, rating INTEGER, created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )""")
    c.commit()

    # v44.4: same per-user rekey as init_db() applies to concepts/attempts, run
    # here too since curriculum_mastery/daily_path_events are created lazily by
    # this function rather than by init_db() directly.
    _init_users_table(c)
    _rekey_concept_table(
        c, "curriculum_mastery",
        "concept_id TEXT NOT NULL, domain TEXT, topic TEXT, "
        "mastery_level INTEGER DEFAULT 0, attempts INTEGER DEFAULT 0, correct INTEGER DEFAULT 0, "
        "last_seen " + ("TIMESTAMP" if USE_POSTGRES else "TEXT") + ", next_due " + ("DATE" if USE_POSTGRES else "TEXT"),
        ["concept_id", "domain", "topic", "mastery_level", "attempts", "correct", "last_seen", "next_due"],
    )
    _add_user_id_column(c, "daily_path_events")
    c.commit(); c.close()

def adaptive_mastery_map(user_id=None):
    ensure_adaptive_schema()
    uid = user_id if user_id is not None else _current_user_id()
    c=conn()
    rows=_execute(c,"SELECT concept_id, domain, topic, mastery_level, attempts, correct, last_seen, next_due FROM curriculum_mastery WHERE user_id=?",(uid,)).fetchall()
    c.close()
    out={}
    for row in rows:
        d=dict(row)
        due=d.get("next_due")
        if isinstance(due,str) and due:
            try: due=datetime.fromisoformat(due).date()
            except Exception:
                try: due=datetime.strptime(due[:10],"%Y-%m-%d").date()
                except Exception: due=None
        elif hasattr(due,"date"):
            due=due.date()
        d["next_due"]=due
        out[d["concept_id"]]=d
    return out

def record_adaptive_result(concept_id, item_id, domain, topic, stage, level, rating, interval_days, user_id=None):
    ensure_adaptive_schema()
    uid = user_id if user_id is not None else _current_user_id()
    c=conn()
    _execute(c,"INSERT INTO daily_path_events(user_id,concept_id,item_id,stage,rating) VALUES(?,?,?,?,?)",(uid,concept_id,item_id,stage,rating))
    row=_execute(c,"SELECT mastery_level, attempts, correct FROM curriculum_mastery WHERE concept_id=? AND user_id=?",(concept_id,uid)).fetchone()
    old_level=(row["mastery_level"] if row else 0)
    attempts=(row["attempts"] if row else 0)+1
    correct=(row["correct"] if row else 0)+(1 if rating>=2 else 0)
    # Missed/Hard do not pass the stage. Got it/Easy pass exactly one stage.
    if rating==0:
        new_level=max(0,old_level-1 if old_level>=level else old_level); days=1
    elif rating==1:
        new_level=old_level; days=max(1,interval_days//2)
    elif rating==2:
        new_level=max(old_level,min(level,6)); days=max(1,interval_days)
    else:
        new_level=max(old_level,min(level,6)); days=min(90,max(interval_days,1)*2)
    now=datetime.now(); due=(now+timedelta(days=days)).date().isoformat()
    exists=_execute(c,"SELECT concept_id FROM curriculum_mastery WHERE concept_id=? AND user_id=?",(concept_id,uid)).fetchone()
    if exists:
        _execute(c,"UPDATE curriculum_mastery SET domain=?, topic=?, mastery_level=?, attempts=?, correct=?, last_seen=?, next_due=? WHERE concept_id=? AND user_id=?",(domain,topic,new_level,attempts,correct,now.isoformat(),due,concept_id,uid))
    else:
        _execute(c,"INSERT INTO curriculum_mastery (user_id,concept_id,domain,topic,mastery_level,attempts,correct,last_seen,next_due) VALUES(?,?,?,?,?,?,?,?,?)",(uid,concept_id,domain,topic,new_level,attempts,correct,now.isoformat(),due))
    c.commit(); c.close()
    return new_level



# =============================================================================
# v9.3 unified learner model
# =============================================================================
UNIFIED_DIMENSIONS = ["recognition","localization","reasoning","workup","management","operative","teaching"]
_STAGE_TO_DIMENSION = {
    "recognize":"recognition","localize":"localization","workup":"workup",
    "manage":"management","operate":"operative","teach":"teaching"
}

def unified_mastery_profiles(user_id=None):
    """One read model for Dashboard, Progress, Daily Path, Atlas and Cases.

    It does not delete the legacy tables. It combines the modern learning streams
    and scores unattempted dimensions as unmastered so a single successful task
    cannot make a concept appear fully mastered.
    """
    uid = user_id if user_id is not None else _current_user_id()
    c=conn()
    # Current adaptive concept metadata.
    try:
        cm_rows=_execute(c,"SELECT * FROM curriculum_mastery WHERE user_id=?",(uid,)).fetchall()
    except Exception:
        cm_rows=[]
    cm={r["concept_id"]:dict(r) for r in cm_rows}

    events=[]

    # Integrated cases / attending mode / atlas variants already write here.
    try:
        rows=_execute(c,"SELECT * FROM mastery_events WHERE user_id=? ORDER BY id",(uid,)).fetchall()
        from data import canonical_concept_id_v98, canonical_concept_domain_v98
        for r in rows:
            cid=canonical_concept_id_v98(r["concept_id"],r["domain"])
            events.append({
                "concept_id":cid,"domain":canonical_concept_domain_v98(r["concept_id"],r["domain"]),
                "topic":None,"dimension":r["dimension"],"score":int(r["score"]),
                "created_at":r["created_at"],"source":r["source_type"] or "mastery"
            })
    except Exception:
        pass

    # Daily Path ratings.
    try:
        rows=_execute(c,"SELECT * FROM daily_path_events WHERE user_id=? ORDER BY id",(uid,)).fetchall()
        for r in rows:
            meta=cm.get(r["concept_id"],{})
            events.append({
                "concept_id":r["concept_id"],"domain":meta.get("domain") or "ENT",
                "topic":meta.get("topic"),"dimension":_STAGE_TO_DIMENSION.get(r["stage"],"reasoning"),
                "score":int(r["rating"]),"created_at":r["created_at"],"source":"daily_path"
            })
    except Exception:
        pass

    # Interpretation Atlas ratings are already represented in mastery_events.
    # Do not ingest lab_attempts again or every Atlas interaction is double-counted.
    c.close()

    profiles={}
    for e in events:
        cid=e["concept_id"]
        x=profiles.setdefault(cid,{
            "concept_id":cid,
            "name":e.get("topic") or cm.get(cid,{}).get("topic") or cid.replace("v6-","").replace("-"," ").title(),
            "domain":e.get("domain") or cm.get(cid,{}).get("domain") or "ENT",
            "dimensions":{},"events":0,"overall":0,"coverage":0,"last_seen":None,
        })
        if e.get("topic"): x["name"]=e["topic"]
        if e.get("domain"): x["domain"]=e["domain"]
        dim=e["dimension"]
        d=x["dimensions"].setdefault(dim,{"scores":[],"score":0,"events":0,"last":None})
        s=max(0,min(3,int(e["score"])))
        d["scores"].append(s); d["events"]+=1; d["last"]=e["created_at"]
        recent=d["scores"][-4:]
        weights=list(range(1,len(recent)+1))
        d["score"]=round(100*sum(a*w for a,w in zip(recent,weights))/(3*sum(weights))) if weights else 0
        x["events"]+=1
        if not x["last_seen"] or str(e["created_at"])>str(x["last_seen"]):
            x["last_seen"]=e["created_at"]

    # Add adaptive concepts with saved mastery even if an older database has no events.
    for cid,meta in cm.items():
        if cid not in profiles and int(meta.get("attempts") or 0)>0:
            profiles[cid]={
                "concept_id":cid,"name":meta.get("topic") or cid,"domain":meta.get("domain") or "ENT",
                "dimensions":{},"events":int(meta.get("attempts") or 0),"overall":0,"coverage":0,
                "last_seen":meta.get("last_seen")
            }

    for x in profiles.values():
        # Missing dimensions intentionally count as zero.
        scores=[x["dimensions"].get(dim,{}).get("score",0) for dim in UNIFIED_DIMENSIONS]
        x["overall"]=round(sum(scores)/len(UNIFIED_DIMENSIONS))
        x["coverage_count"]=sum(1 for dim in UNIFIED_DIMENSIONS if dim in x["dimensions"])
        x["coverage"]=round(100*x["coverage_count"]/len(UNIFIED_DIMENSIONS))
    return profiles

def unified_stats(user_id=None):
    profiles=unified_mastery_profiles(user_id=user_id)
    try:
        mastery=adaptive_mastery_map(user_id=user_id)
    except Exception:
        mastery={}
    today=datetime.now().date()
    due=0
    for x in mastery.values():
        d=x.get("next_due")
        if d and d<=today: due+=1
    attempts=sum(p["events"] for p in profiles.values())
    avg=round(sum(p["overall"] for p in profiles.values())/len(profiles)) if profiles else 0
    coverage=round(sum(p["coverage"] for p in profiles.values())/len(profiles)) if profiles else 0
    return {"attempts":attempts,"concepts":len(profiles),"mastery":avg,"coverage":coverage,"due":due}

def unified_dimension_summary(user_id=None):
    profiles=unified_mastery_profiles(user_id=user_id)
    out={}
    for dim in UNIFIED_DIMENSIONS:
        vals=[p["dimensions"][dim]["score"] for p in profiles.values() if dim in p["dimensions"]]
        out[dim]=round(sum(vals)/len(vals)) if vals else 0
    return out

def unified_domain_mastery(user_id=None):
    profiles=unified_mastery_profiles(user_id=user_id); by={}
    for p in profiles.values():
        by.setdefault(p["domain"],[]).append(p["overall"])
    return {k:round(sum(v)/len(v)) if v else 0 for k,v in by.items()}

def unified_weak_concepts(limit=6, user_id=None):
    profiles=unified_mastery_profiles(user_id=user_id)
    touched=[p for p in profiles.values() if p["events"]>0]
    return sorted(touched,key=lambda p:(p["overall"],p["coverage"],-p["events"]))[:limit]

def unified_mistakes(limit=100, user_id=None):
    """Recent weak interactions from modern learning streams."""
    uid = user_id if user_id is not None else _current_user_id()
    c=conn(); out=[]
    try:
        rows=_execute(c,"""SELECT concept_id,domain,dimension,score,source_type,source_id,miss_type,created_at
                           FROM mastery_events WHERE (score<=1 OR miss_type IS NOT NULL) AND user_id=?
                           ORDER BY id DESC LIMIT ?""",(uid,limit)).fetchall()
        for r in rows:
            out.append({"concept_id":r["concept_id"],"domain":r["domain"] or "ENT",
                        "dimension":r["dimension"],"score":int(r["score"]),
                        "source":r["source_type"] or "case","source_id":r["source_id"],
                        "miss_type":r["miss_type"],"created_at":r["created_at"]})
    except Exception: pass
    try:
        rows=_execute(c,"""SELECT e.*, m.domain, m.topic FROM daily_path_events e
                           LEFT JOIN curriculum_mastery m ON m.concept_id=e.concept_id AND m.user_id=e.user_id
                           WHERE e.rating<=1 AND e.user_id=? ORDER BY e.id DESC LIMIT ?""",(uid,limit)).fetchall()
        for r in rows:
            out.append({"concept_id":r["concept_id"],"name":r["topic"],
                        "domain":r["domain"] or "ENT","dimension":_STAGE_TO_DIMENSION.get(r["stage"],"reasoning"),
                        "score":int(r["rating"]),"source":"daily_path","source_id":r["item_id"],
                        "miss_type":None,"created_at":r["created_at"]})
    except Exception: pass
    try:
        rows=_execute(c,"""SELECT * FROM lab_attempts WHERE rating<=1 AND user_id=? ORDER BY id DESC LIMIT ?""",(uid,limit)).fetchall()
        for r in rows:
            out.append({"concept_id":r["concept_id"],"domain":r["lab_slug"].replace("-"," ").title(),
                        "dimension":"recognition","score":int(r["rating"]),"source":"interpretation_atlas",
                        "source_id":r["case_id"],"miss_type":None,"created_at":r["created_at"]})
    except Exception: pass
    c.close()
    # Deduplicate most-recent by concept/dimension/source.
    out.sort(key=lambda x:str(x.get("created_at") or ""),reverse=True)
    seen=set(); dedup=[]
    for x in out:
        key=(x["concept_id"],x["dimension"],x["source"])
        if key in seen: continue
        seen.add(key); dedup.append(x)
        if len(dedup)>=limit: break
    return dedup


# =============================================================================
# v44.4 multi-user accounts
# =============================================================================
def create_user(email, name, password_hash, role="resident"):
    """Insert a new account. Raises on a duplicate email (caller should catch)."""
    now = datetime.now().isoformat()
    c = conn()
    if USE_POSTGRES:
        row = c.execute(
            "INSERT INTO users (email, name, password_hash, role, created_at) "
            "VALUES (%s, %s, %s, %s, %s) RETURNING id",
            (email.strip().lower(), name.strip(), password_hash, role, now),
        ).fetchone()
        new_id = row["id"] if row else None
    else:
        cur = c.execute(
            "INSERT INTO users (email, name, password_hash, role, created_at) VALUES (?, ?, ?, ?, ?)",
            (email.strip().lower(), name.strip(), password_hash, role, now),
        )
        new_id = cur.lastrowid
    c.commit(); c.close()
    return new_id


def _slugify_name(name):
    import re as _re
    slug = _re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")
    return slug or "resident"


def create_resident_pin(name, pin_hash, role="resident"):
    """Create a PIN-login account. No real email is collected -- residents are

    added by a chief from the roster page with just a name and a PIN, so a
    synthetic-but-unique placeholder email is derived from the name (email
    stays NOT NULL UNIQUE on the table; it is never shown or used to log in).
    """
    now = datetime.now().isoformat()
    base = _slugify_name(name)
    c = conn()
    email = f"{base}@resident.local"
    suffix = 1
    while _execute(c, "SELECT 1 FROM users WHERE email=?", (email,)).fetchone():
        suffix += 1
        email = f"{base}-{suffix}@resident.local"
    if USE_POSTGRES:
        row = c.execute(
            "INSERT INTO users (email, name, password_hash, pin_hash, role, created_at) "
            "VALUES (%s, %s, %s, %s, %s, %s) RETURNING id",
            (email, name.strip(), "", pin_hash, role, now),
        ).fetchone()
        new_id = row["id"] if row else None
    else:
        cur = c.execute(
            "INSERT INTO users (email, name, password_hash, pin_hash, role, created_at) VALUES (?, ?, ?, ?, ?, ?)",
            (email, name.strip(), "", pin_hash, role, now),
        )
        new_id = cur.lastrowid
    c.commit(); c.close()
    return new_id


def get_user_by_email(email):
    c = conn()
    row = _execute(c, "SELECT * FROM users WHERE email=?", (email.strip().lower(),)).fetchone()
    c.close()
    return dict(row) if row else None


def get_user_by_id(user_id):
    c = conn()
    row = _execute(c, "SELECT * FROM users WHERE id=?", (user_id,)).fetchone()
    c.close()
    return dict(row) if row else None


def get_user_by_name(name):
    c = conn()
    row = _execute(c, "SELECT * FROM users WHERE LOWER(name)=LOWER(?) AND id<>? ORDER BY id LIMIT 1",
                   (name.strip(), LEGACY_USER_ID)).fetchone()
    c.close()
    return dict(row) if row else None


def update_user_pin(user_id, pin_hash):
    c = conn()
    _execute(c, "UPDATE users SET pin_hash=? WHERE id=? AND id<>?",
             (pin_hash, user_id, LEGACY_USER_ID))
    c.commit()
    c.close()


def list_users(include_legacy=False):
    c = conn()
    rows = _execute(c, "SELECT id, email, name, role, created_at FROM users ORDER BY name COLLATE NOCASE" if not USE_POSTGRES else "SELECT id, email, name, role, created_at FROM users ORDER BY LOWER(name)").fetchall()
    c.close()
    out = [dict(r) for r in rows]
    if not include_legacy:
        out = [u for u in out if u["id"] != LEGACY_USER_ID]
    return out


def roster_summary():
    """Per-resident mastery/coverage/activity snapshot for a chief/attending view.

    Reuses the same unified_stats()/unified_domain_mastery() math every learner
    already sees on their own Progress page, just run once per real account
    (the Legacy/Shared bucket is excluded -- it is pre-accounts history, not a
    person).
    """
    out = []
    for u in list_users(include_legacy=False):
        st = unified_stats(user_id=u["id"])
        domains = unified_domain_mastery(user_id=u["id"])
        out.append({
            "id": u["id"], "name": u["name"], "email": u["email"], "role": u["role"],
            "created_at": u["created_at"], "attempts": st["attempts"], "mastery": st["mastery"],
            "coverage": st["coverage"], "concepts": st["concepts"], "due": st["due"],
            "domains": domains,
        })
    out.sort(key=lambda x: x["name"].lower())
    return out
