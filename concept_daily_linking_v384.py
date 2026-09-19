"""v38.4 additive integration for exact Concept Hub links and topic-based Daily Path.

Preserves the existing app.py routes while adding the focused uploaded app changes.
Avoids fuzzy OR-to-concept redirects that can select unrelated topics.
"""
import random


def install_concept_daily_linking_v384(data_module, app_module):
    original_context = app_module._concept_context_v1006
    original_plan = app_module._adaptive_plan

    def context(domain, module):
        result = original_context(domain, module)
        cid = result['concept_id']
        result['related_questions'] = [q for q in data_module.CLINICAL_CHALLENGES_V119
                                       if q.get('concept_id') == cid][:8]
        return result

    def find_exact(domain, topic):
        norm = app_module._norm_topic_v94(topic)
        if not norm:
            return None, None
        desired = data_module.canonical_domain_v94(domain) if domain else None
        candidates = [(d, m) for d, mods in data_module.DEEP_MODULES_V6.items()
                      for m in mods if app_module._norm_topic_v94(m.get('topic')) == norm]
        if desired:
            matching = [(d, m) for d, m in candidates
                        if data_module.canonical_domain_v94(d) == desired]
            if len(matching) == 1:
                return matching[0]
            if len(matching) > 1:
                return None, None
        return candidates[0] if len(candidates) == 1 else (None, None)

    def plan(minutes=30, focus=None, concept_id=None):
        selected, _ = original_plan(minutes, focus, concept_id)
        if minutes < 20 or not selected:
            return selected, sum(x.get('minutes', 0) for x in selected), {}
        items = data_module.get_adaptive_items_v120()
        grouped = {}
        for item in items:
            grouped.setdefault(item['concept_id'], []).append(item)
        result, used, seen, bundles = [], 0, set(), {}
        for first in selected:
            cid = first['concept_id']
            if first['id'] in seen:
                continue
            if first.get('mastery_before', 0) == 0:
                stages = sorted(grouped.get(cid, [first]), key=lambda x: x['level'])
                added = False
                for item in stages:
                    if item['id'] in seen or used + item['minutes'] > minutes + 8:
                        break
                    result.append(dict(item, prompt=app_module._adaptive_question(item),
                                       mastery_before=0, reason=first['reason'],
                                       bundle_start=not added))
                    used += item['minutes']
                    seen.add(item['id'])
                    added = True
                if added:
                    qs = [q for q in data_module.CLINICAL_CHALLENGES_V119
                          if q.get('concept_id') == cid][:4]
                    if qs:
                        bundles[cid] = qs
            elif used + first['minutes'] <= minutes + 3:
                result.append(first)
                used += first['minutes']
                seen.add(first['id'])
        return result, used, bundles

    def daily_adaptive():
        from flask import request, render_template
        focus = request.args.get('focus') or None
        concept_id = request.args.get('concept') or None
        try:
            mins = int(request.args.get('minutes', '30'))
        except (TypeError, ValueError):
            mins = 30
        mins = max(10, min(60, mins))
        selected, total, bundles = plan(mins, focus, concept_id)
        bundled_ids = {q.get('id') for group in bundles.values() for q in group}
        pool = [q for q in data_module.CLINICAL_CHALLENGES_V119
                if q.get('id') not in bundled_ids
                and (not focus or data_module.canonical_domain_v94(q.get('domain'))
                     == data_module.canonical_domain_v94(focus))]
        random.shuffle(pool)
        challenges = pool[:max(1, min(3, mins // 15))]
        return render_template('daily_adaptive.html', plan=selected, total=total,
                               minutes=mins, focus=focus, concept_id=concept_id,
                               domains=list(data_module.DEEP_MODULES_V6.keys()),
                               daily_challenges=challenges, bundle_questions=bundles)

    app_module._concept_context_v1006 = context
    app_module._find_deep_module_v94 = find_exact
    app_module._adaptive_plan = plan
    app_module.app.view_functions['daily_adaptive'] = daily_adaptive
    return {'exact_concept_links': True, 'daily_bundle_support': True,
            'practice_question_links': True}
