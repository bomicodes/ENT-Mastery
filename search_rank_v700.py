"""v70.0: tighter search ranking.

The old scorer matched raw substrings, so short words and abbreviations fired inside other
words: the alias "ci" (cochlear implant) matched inside "laryngomalacia", "facial" and almost
every query; "ear" matched "year" and "near"; "thyroidectomy" matched "parathyroidectomy".
Aliases also bypassed the "a query word must match" rule.

This scorer matches whole words (a query word of 4+ letters may also match the start of a
longer word, so "thyroid" finds "thyroidectomy"), expands abbreviations only when the
abbreviation is a whole query word, requires every meaningful query word to match, weighs
title over subtitle over body text, and drops the long tail far below the best result.
"""
import re

STOP = {"a", "an", "the", "of", "for", "and", "or", "with", "in", "on", "to", "my", "is", "are",
        "how", "what", "why", "when", "do", "does", "after", "vs", "versus", "wont", "won", "t",
        "dont", "not", "patient", "management", "treatment", "case"}

ALIASES = {
    "scc": ["squamous cell carcinoma"], "aoe": ["acute otitis externa"], "osa": ["obstructive sleep apnea"],
    "ssnhl": ["sudden sensorineural hearing loss"], "snhl": ["sensorineural hearing loss"],
    "bppv": ["benign paroxysmal positional vertigo"], "aom": ["acute otitis media"],
    "ome": ["otitis media with effusion"], "crs": ["chronic rhinosinusitis"],
    "crswnp": ["chronic rhinosinusitis with nasal polyps"], "crssnp": ["chronic rhinosinusitis without nasal polyps"],
    "fess": ["endoscopic sinus surgery", "revision fess"], "ess": ["endoscopic sinus surgery"],
    "rln": ["recurrent laryngeal nerve"], "ebsln": ["external branch superior laryngeal nerve"],
    "hns": ["hypoglossal nerve stimulation"], "ci": ["cochlear implant", "cochlear implantation"],
    "tmj": ["temporomandibular joint"], "pta": ["peritonsillar abscess"], "pth": ["parathyroid"],
    "jna": ["juvenile nasopharyngeal angiofibroma"], "npc": ["nasopharyngeal carcinoma"],
    "csf": ["cerebrospinal fluid", "csf"], "noe": ["naso orbito ethmoid", "noe"], "zmc": ["zygomaticomaxillary"],
    "tors": ["transoral robotic surgery"], "dise": ["drug induced sleep endoscopy"], "rrp": ["recurrent respiratory papillomatosis"],
    "ptc": ["papillary thyroid carcinoma"], "mtc": ["medullary thyroid"], "lpr": ["laryngopharyngeal reflux"],
    "bleed": ["hemorrhage", "bleeding", "epistaxis"], "bleeding": ["hemorrhage"], "tubes": ["tympanostomy"],
    "nosebleed": ["epistaxis"], "drop": ["persistent", "reoperative", "fall"], "hoarse": ["dysphonia", "hoarseness"],
    "hoarseness": ["dysphonia"], "palsy": ["paralysis"], "dizzy": ["vertigo", "dizziness"], "dizziness": ["vertigo"],
    "infant": ["pediatric", "neonatal", "infantile"], "child": ["pediatric"], "kid": ["pediatric"], "baby": ["pediatric", "infant"],
    "swallowed": ["ingestion", "foreign body"], "battery": ["button battery"], "cancer": ["carcinoma", "malignancy"],
}
TYPE_BOOST = {"OR Tomorrow": 1.25, "Curriculum concept": 1.2, "Progressive case": 1.1, "Interpretation Atlas": 1.05,
              "Pasha Review Section": 1.0, "Pasha Review Chapter": 1.0, "Evidence": 1.0, "Practice bank": 1.0,
              "Clinical Challenge": 0.7, "Concept Check": 0.65}
QUESTION_TYPES = {"Clinical Challenge", "Concept Check"}


def _words(s):
    return re.findall(r"[a-z0-9]+", str(s or "").lower())


def _term_hit(term, words):
    if term in words:
        return 1.0
    if len(term) >= 4 and any(w.startswith(term) for w in words):
        return 0.8
    return 0.0


def _phrase_in(phrase_words, words):
    n = len(phrase_words)
    if not n:
        return False
    for i in range(len(words) - n + 1):
        if words[i:i + n] == phrase_words:
            return True
    return False


# v92: words that name a kind of scheme rather than the topic; they help ranking but aren't required,
# so "Chandler's classification" finds the Chandler material even if the text says "Chandler stages".
SOFT = {"classification", "classifications", "criteria", "staging", "stage", "stages", "grading", "grade",
        "grades", "system", "score", "scale", "sign", "triad", "rule", "type", "types"}


def parse_query(q):
    q = re.sub(r"[\'\u2019]s\b", "", str(q or ""))  # possessives: "chandler's" -> "chandler"
    words = _words(q)
    terms = [w for w in words if w not in STOP] or words
    alts = {}
    for t in terms:
        if t in ALIASES:
            alts[t] = [_words(a) for a in ALIASES[t]]
    return words, terms, alts


def score_row(row, parsed):
    words, terms, alts = parsed
    if not terms:
        return 0.0
    tw = _words(row.get("title")); sw = _words(row.get("subtitle")); xw = _words(row.get("text"))
    total, matched, in_title = 0.0, 0, 0
    for t in terms:
        best = 0.0
        for weight, fw in ((10, tw), (3, sw), (1, xw)):
            h = _term_hit(t, fw)
            for alt in alts.get(t, []):
                if _phrase_in(alt, fw):
                    h = max(h, 1.0)
            best = max(best, weight * h)
        if best > 0:
            matched += 1
            total += best
            if best >= 8:
                in_title += 1
    required = [t for t in terms if t not in SOFT] or terms
    req_hit = sum(1 for t in required if any(_term_hit(t, fw) or any(_phrase_in(a, fw) for a in alts.get(t, []))
                                             for fw in (tw, sw, xw)))
    if req_hit < len(required):
        return 0.0  # every meaningful word (or its abbreviation) must match; scheme words are optional
    page = row.get("type") not in QUESTION_TYPES
    if tw == terms or tw == words:
        total += 60 if page else 10
    elif _phrase_in(terms, tw):
        total += 30 if page else 8
    if in_title >= len(required):
        total += 15
    # a shorter title that matches is a more specific hit
    total *= 1.0 + 0.4 / max(1, len(tw))
    row_tier = 1 if in_title >= len(required) else (2 if page else 3)
    return total * TYPE_BOOST.get(row.get("type"), 1.0), row_tier


def _score(row, parsed):
    res = score_row(row, parsed)
    return res if isinstance(res, tuple) else (res, 3)


def rank(index, q, limit=None, tail=None):
    """Title matches first (all of them), then pages that mention the query in their subtitle or
    body (up to 15), then questions that mention it only in their text (up to 12)."""
    parsed = parse_query(q)
    scored = [(_score(r, parsed), r) for r in index]
    scored = [(sc, r) for sc, r in scored if sc[0] > 0]
    words, terms, alts = parsed
    if not scored and len(terms) > 2:
        # nothing matches every word: fall back to rows matching all but one
        best = []
        for drop in range(len(terms)):
            sub = (words, terms[:drop] + terms[drop + 1:], alts)
            for r in index:
                sc = _score(r, sub)
                if sc[0] > 0:
                    best.append(((sc[0] * 0.7, sc[1]), r))
        seen, scored = set(), []
        for sc, r in sorted(best, key=lambda x: -x[0][0]):
            if id(r) not in seen:
                seen.add(id(r)); scored.append((sc, r))
    if not scored:
        return []
    caps = {1: None, 2: 15, 3: 12}
    out = []
    for t in (1, 2, 3):
        tier = sorted([(sc[0], r) for sc, r in scored if sc[1] == t], key=lambda x: (-x[0], str(x[1].get("title", ""))))
        if caps[t] is not None:
            # questions are grouped by topic later, so cap distinct topics rather than rows
            kept, topics = [], set()
            for s_, r in tier:
                key = (r.get("type"), r.get("title"))
                if key not in topics and len(topics) >= caps[t]:
                    continue
                topics.add(key); kept.append((s_, r))
            tier = kept
        out += tier
    return out[:limit] if limit else out


def install_search_rank_v700(app_mod):
    app_mod._search_rank_v700 = rank
    return {"aliases": len(ALIASES)}
