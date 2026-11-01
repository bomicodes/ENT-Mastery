"""v54.1: installable app and offline study.

/manifest.webmanifest   app manifest (install to home screen)
/sw.js                  service worker at root scope: caches the app shell, pages you
                        visit and an offline question pack; network-first for pages
/offline                offline quiz that runs from the cached pack, saves answers
                        on the device and syncs them when the connection returns
/offline-pack.json      ~400 board-style questions in blueprint proportions plus the
                        user's due missed questions (text only; images need a connection)
"""
import json
import random

import db

PACK_SIZE = 400
CACHE_VERSION = "entm-v541-1"

SW_JS = r"""
const CACHE = '%(ver)s';
const SHELL = ['/offline', '/offline-pack.json', '/static/style.css', '/static/layout_v520.css', '/static/exam_v531.css',
  '/static/question_v490.css', '/static/mobile_nav_v183.css', '/static/reliability_v168.css', '/static/app.js',
  '/static/icons/icon-192.png', '/static/icons/icon-512.png'];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => Promise.all(SHELL.map(u => c.add(new Request(u, {credentials: 'same-origin'})).catch(() => null)))).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;
  if (url.pathname.startsWith('/api/') || url.pathname.startsWith('/logout') || url.pathname.startsWith('/account/')) return;
  if (req.mode === 'navigate') {
    e.respondWith(fetch(req).then(res => {
      if (res.ok && !res.redirected) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }
      return res;
    }).catch(() => caches.match(req).then(r => r || caches.match('/offline'))));
    return;
  }
  if (url.pathname.startsWith('/static/') || url.pathname === '/offline-pack.json') {
    e.respondWith(caches.match(req).then(hit => {
      const net = fetch(req).then(res => { if (res.ok) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); } return res; }).catch(() => hit);
      return hit || net;
    }));
  }
});
"""


def install_offline_v541(app, data, app_mod=None):
    from flask import Response, jsonify, render_template, url_for

    bank = data.CLINICAL_CHALLENGES_V119
    src = app_mod if app_mod is not None else data
    canon = getattr(src, "canonical_domain_v94", None) or getattr(data, "canonical_domain_v94", lambda d: d)

    def manifest():
        body = {
            "name": "ENT Mastery", "short_name": "ENT Mastery", "start_url": "/", "scope": "/",
            "display": "standalone", "background_color": "#f4f7f7", "theme_color": "#0f3b3a",
            "description": "Otolaryngology board prep: questions, timed exams, atlas, OR prep.",
            "icons": [{"src": "/static/icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
                      {"src": "/static/icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}],
            "shortcuts": [{"name": "Offline questions", "url": "/offline"}, {"name": "Timed exam", "url": "/exam"}],
        }
        return Response(json.dumps(body), mimetype="application/manifest+json")

    def sw():
        r = Response(SW_JS % {"ver": CACHE_VERSION}, mimetype="application/javascript")
        r.headers["Service-Worker-Allowed"] = "/"
        r.headers["Cache-Control"] = "no-cache"
        return r

    def pack():
        q = getattr(data, "QUALITY_V540", None) or {}
        paused = q.get("paused_ids", lambda: set())()
        weights = q.get("blueprint") or {}
        board = [x for x in bank if x.get("tier") == "Curated board-style" and not x.get("image_url") and x["id"] not in paused]
        rng = random.Random(db._current_user_id() * 7919 + len(bank))
        by_dom = {}
        for x in board:
            by_dom.setdefault(canon(x.get("domain")), []).append(x)
        chosen, seen = [], set()
        due = q.get("due_reviews", lambda u: {"due": []})(db._current_user_id())["due"]
        by_id = data.CLINICAL_CHALLENGE_BY_ID_V119
        for qid in due:
            if qid in by_id and qid not in paused:
                chosen.append(by_id[qid]); seen.add(qid)
        total_w = sum(weights.values()) or 1
        for d, w in weights.items():
            pool = [x for x in by_dom.get(d, []) if x["id"] not in seen]
            rng.shuffle(pool)
            for x in pool[: int(round(PACK_SIZE * w / total_w))]:
                chosen.append(x); seen.add(x["id"])
        letters = "ABCD"
        items = []
        for x in chosen:
            ans = int(x.get("answer", 0))
            items.append({"id": x["id"], "domain": canon(x.get("domain")), "topic": x.get("topic"), "stem": x.get("stem"),
                          "choices": x.get("choices", []), "answer": ans, "explanation": x.get("explanation", ""),
                          "pearl": x.get("board_pearl", ""), "due": x["id"] in due,
                          "why_wrong": [[letters[i], w] for i, w in enumerate(x.get("why_wrong") or []) if i != ans and w]})
        r = jsonify({"version": CACHE_VERSION, "count": len(items), "items": items})
        r.headers["Cache-Control"] = "no-cache"
        return r

    def offline():
        return render_template("offline_v541.html")

    routes = [
        ("/manifest.webmanifest", "manifest_v541", manifest),
        ("/sw.js", "sw_v541", sw),
        ("/offline-pack.json", "offline_pack_v541", pack),
        ("/offline", "offline_v541", offline),
    ]
    served = getattr(app, "_got_first_request", False)
    if served:
        app._got_first_request = False
    try:
        for rule, name, fn in routes:
            if name not in app.view_functions:
                app.add_url_rule(rule, name, fn)
    finally:
        if served:
            app._got_first_request = True
    return {"routes": [r[0] for r in routes], "pack_size": PACK_SIZE}
