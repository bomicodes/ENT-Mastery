"""Hard gate for the database-backed Pasha 6e review subsystem."""
import os, tempfile

# Force isolated SQLite before importing the app stack.
os.environ.pop("DATABASE_URL",None)
os.environ["SQLITE_PATH"]=os.path.join(tempfile.gettempdir(),"ent_mastery_pasha_ci.sqlite3")
try: os.remove(os.environ["SQLITE_PATH"])
except FileNotFoundError: pass

import runtime_entry_pasha
from pasha_review_data import PASHA_CHAPTERS
from pasha_routes import chapter_bank, section_questions
from pasha_db import pasha_progress

app=runtime_entry_pasha.app
failures=[]
with app.test_client() as c:
    r=c.get('/pasha-review')
    if r.status_code!=200: failures.append(('index',r.status_code))
    for ch in PASHA_CHAPTERS:
        cid=ch['id']
        for path in [f'/pasha-review?chapter={cid}',f'/pasha-review?chapter={cid}&mode=exam&seed=42']:
            rr=c.get(path)
            if rr.status_code!=200: failures.append((path,rr.status_code))
        bank=chapter_bank(ch)
        if len(bank)<5: failures.append((f'chapter-{cid}-bank',len(bank)))
        for sec in ch['sections']:
            rows=section_questions(ch,sec,20)
            if not rows: failures.append((f'{cid}:{sec[0]}-empty',0))
            rr=c.get(f'/pasha-review?chapter={cid}&section={sec[0]}')
            if rr.status_code!=200: failures.append((f'{cid}:{sec[0]}',rr.status_code))
    # Verify a real answer writes persistence and mastery without a 500.
    ch=PASHA_CHAPTERS[6]
    q=chapter_bank(ch)[0]
    rr=c.post('/api/pasha-review/answer',json={'chapter_id':ch['id'],'section_id':q.get('section_id','chapter'),'question_id':q['id'],'chosen':q['answer']})
    if rr.status_code!=200 or not (rr.get_json() or {}).get('ok'): failures.append(('answer-api',rr.status_code,rr.get_json()))
    if pasha_progress().get('total_attempts',0)<1: failures.append(('persistence',0))

if failures:
    print('PASHA REVIEW AUDIT FAILED')
    for x in failures: print(' -',x)
    raise SystemExit(1)
print('PASHA REVIEW AUDIT PASSED')
print('chapters:',len(PASHA_CHAPTERS),'sections:',sum(len(c['sections']) for c in PASHA_CHAPTERS))
