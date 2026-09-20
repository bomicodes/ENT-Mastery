"""v40.3: clean resident-facing editorial notes and guard blind Daily Path stems.
Runs after the reviewed production startup; clinical source_basis and tags are untouched.
"""
import re
import daily_curriculum_quality_v368 as daily

FIELDS = ('recognize', 'localize', 'workup', 'manage', 'operate', 'teach')
EDITORIAL = {
    'This card owns REFERRAL AND SELECTION, not the mastoidectomy. ': '',
    'The operative decision in this card is WHICH EAR / WHETHER TO IMPLANT, not how to perform the facial recess. ': '',
    'Once the patient is selected and the side chosen, transition to the separate COCHLEAR IMPLANT SURGERY framework.': '',
    'Preop vaccination and anatomy belong in the evaluation; mastoidectomy steps and device-failure troubleshooting belong to separate cards.': '',
    'This card owns the OPERATION. ': '',
    'The operation ends with a secured system and viable wound; candidacy testing occurred before surgery, while declining performance months/years later belongs to the FAILURE/REVISION card.': 'The operation ends with a secured system and viable wound; later declining performance requires a structured evaluation for device and patient factors.',
    'Once the goal is established, move to the separate PALLIATIVE DECISION-MAKING card for symptom-directed interventions.': '',
    'This card owns SYMPTOM-DIRECTED H&N INTERVENTION after the therapeutic goal has been defined. ': 'Once therapeutic goals are defined, select interventions directed at the specific symptoms. ',
    'The GOALS-OF-CARE card establishes the destination; this card chooses the least-burdensome ENT/oncologic tool that can realistically get there.': 'Clarify the treatment goal first, then select the least-burdensome intervention likely to achieve it.',
    'The BIOMECHANICS card owns how those findings become a fixation construct.': '',
    'The parent-card operative sequence is:': 'The operative sequence is:',
    'The detailed force-vector and plate-selection logic lives in the separate BIOMECHANICS card.': '',
    'Do not duplicate Champy/load-bearing details here; that is the job of the mechanics card.': '',
    'This is an ADVANCED FIXATION-REASONING card, not a second mandible-fracture workup. ': '',
    'The separate DECISION MODEL card owns the branch-by-branch operation choice.': '',
    'This is the ADVANCED BRANCHING-ALGORITHM card, not a second frontal-sinus-fracture overview. ': '',
    'This card is the geometric toolkit; it does not substitute for the dedicated staged nasal-reconstruction algorithm of a paramedian forehead flap.': '',
    'This card ends at vision-preserving orbital/sinus control; meningitis, empyema, brain abscess, and cerebral venous disease belong to the intracranial card.': 'Vision-threatening orbital disease requires urgent orbital and sinus source control; suspected intracranial extension requires additional neurologic and neurosurgical assessment.',
}


def clean(value):
    if not isinstance(value, str):
        return value
    for old, new in EDITORIAL.items():
        value = value.replace(old, new)
    return re.sub(r' {2,}', ' ', value).strip()


def excerpt(text, limit=900):
    """Prefer complete sentences or clauses, then words; never hard-cut midword."""
    text = daily._clean(text)
    if len(text) <= limit:
        return text
    window = text[:limit]
    boundary = window.rfind('. ')
    if boundary >= max(50, limit // 4):
        return window[:boundary].rstrip(' .,;:-') + '.'
    for separator in (' -- ', '; ', ', '):
        boundary = window.rfind(separator)
        if boundary >= max(50, limit // 4):
            return window[:boundary].rstrip(' .,;:-') + '.'
    words = window.rsplit(None, 1)
    if len(words) > 1:
        return words[0].rstrip(' .,;:-') + '.'
    end = re.search(r'\s', text[limit:])
    return text[:limit + end.start()] + '.' if end else text.rstrip('.') + '.'


def topic_leaked(topic, prompt):
    normalize = lambda s: ' '.join(re.findall(r'[a-z0-9]+', str(s).casefold()))
    name, body = normalize(topic), normalize(prompt)
    return bool(name and re.search(r'(?<!\w)' + re.escape(name) + r'(?!\w)', body))


def repair_blind(item):
    if item.get('stage') != 'recognize' or not item.get('blind_reveal'):
        return False
    topic = str(item.get('topic') or '')
    prompt = item.get('daily_prompt') or item.get('prompt') or ''
    if not topic_leaked(topic, prompt):
        return False
    label = (item.get('blind_case_label') or '').strip()
    if not label or topic_leaked(topic, label):
        prompt = daily._named_recognition_prompt(topic)
        item['blind_reveal'] = False
        item.pop('blind_case_label', None)
    else:
        label = label[0].lower() + label[1:]
        prompt = (f'A patient presents with {label}. Based on the presentation, '
                  'what diagnosis should be considered, and which examination or '
                  'test finding would distinguish it from the closest mimic?')
    item['daily_prompt'] = item['prompt'] = prompt
    return True


def install(data_module, app_module):
    edits = 0
    for modules in data_module.DEEP_MODULES_V6.values():
        for module in modules:
            for field in FIELDS:
                before = module.get(field)
                after = clean(before)
                if after != before:
                    module[field] = after
                    edits += 1
    daily._excerpt = excerpt
    original_get = data_module.get_adaptive_items_v120

    def checked_get():
        items = original_get()
        for item in items:
            for field in ('answer', 'daily_prompt', 'prompt'):
                if isinstance(item.get(field), str):
                    item[field] = clean(item[field])
            repair_blind(item)
        return items

    data_module.get_adaptive_items_v120 = checked_get
    app_module.get_adaptive_items_v120 = checked_get
    sample = checked_get()
    labels = [i['blind_case_label'] for i in sample if i.get('blind_reveal')]
    if len(labels) != len(set(labels)) or any(not x.strip() for x in labels):
        raise RuntimeError('v40.3 blind labels are empty or duplicated')
    if any(topic_leaked(i.get('topic', ''), i.get('daily_prompt', ''))
           for i in sample if i.get('blind_reveal')):
        raise RuntimeError('v40.3 diagnosis leak remains in a blinded card')
    return {'clinical_fields_edited': edits, 'blind_cases': len(labels)}
