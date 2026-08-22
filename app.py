from flask import Flask, render_template, request, redirect, url_for, jsonify
import os, random, re
from data import *
from db import init_db, record_attempt, stats, mistake_rows, concept_strengths

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
    return render_template("dashboard.html", stats=st, weak=weak, topic=PARATHYROID)

@app.route("/today")
def today():
    mins = int(request.args.get("minutes",20))
    count = {10:4,20:7,30:10,45:14}.get(mins,7)
    strengths = concept_strengths()
    qs = sorted(QUESTIONS, key=lambda q: strengths.get(q["concept_id"],{}).get("strength",0))
    return render_template("today.html", minutes=mins, questions=qs[:count], topic=PARATHYROID)

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
    q = request.args.get("q","parathyroidectomy").strip()
    return render_template("case_tomorrow.html", q=q, topic=PARATHYROID, operation=OPERATIONS[0], questions=QUESTIONS[:5])

@app.route("/questions")
def questions():
    kind = request.args.get("kind")
    qs = [q for q in QUESTIONS if not kind or q["kind"]==kind]
    return render_template("questions.html", questions=qs, title="Question Bank")

@app.route("/api/answer", methods=["POST"])
def answer():
    d=request.get_json(force=True)
    q=next((x for x in QUESTIONS if x["id"]==d.get("question_id")),None)
    if not q: return jsonify({"error":"not found"}),404
    choice=int(d.get("choice",-1))
    correct=choice==q["answer"]
    record_attempt(q["id"],q["concept_id"],correct,int(d.get("confidence",3)),d.get("miss_type"))
    return jsonify({"correct":correct,"answer":q["answer"],"explanation":q["explanation"],"why_wrong":q["why_wrong"]})

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

@app.route("/lab")
def lab():
    return render_template("lab.html")

@app.route("/attending")
def attending():
    return render_template("attending.html", prompts=ATTENDING_PROMPTS)

@app.route("/chief")
def chief():
    return render_template("chief.html", prompts=CHIEF_PROMPTS)

@app.route("/mistakes")
def mistakes():
    rows=mistake_rows()
    byid={q["id"]:q for q in QUESTIONS}
    data=[{"row":dict(r),"q":byid.get(r["question_id"])} for r in rows if byid.get(r["question_id"])]
    return render_template("mistakes.html", mistakes=data)

@app.route("/progress")
def progress():
    return render_template("progress.html", stats=stats(), strengths=concept_strengths())

@app.route("/sources")
def sources():
    return render_template("sources.html", sources=PARATHYROID["sources"])

if __name__ == "__main__":
    app.run(debug=True)
