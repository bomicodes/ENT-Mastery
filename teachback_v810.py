"""v81.0: teach-back prompts that fit the kind of topic.

The Daily Path mastery step asked the same thing for every topic ("explain X: the mechanism, how
it presents, and the one decision that most often goes wrong"), which makes no sense for anatomy,
tests or operations ("explain Temporal Bone Anatomy... how it presents"). The prompt now depends on
whether the topic is anatomy/physiology, a test or study to interpret, an operation, or a disease.
"""
import re

ANATOMY = re.compile(r"\b(anatomy|neuroanatomy|physiology|embryology|biomechanics|tip mechanics|tip support|"
                     r"cranial nerve examination|facial analysis)\b", re.I)
TEST = re.compile(r"\b(interpretation|audiogram|tympanometry|electrophysiology|test battery|testing|"
                  r"stroboscopy|fees|modified barium|swallow study|psg|polysomnograph|dise|drug-induced sleep|"
                  r"objective assessment|imaging fundamentals|image review|cytology|localization|lemg|electromyography|"
                  r"monitoring|staging)\b", re.I)
OPERATION = re.compile(r"(ectomy|otomy|ostomy|plasty|pexy|ectomies|\bsurgery\b|\brepair\b|\bflap\b|\bgraft|"
                       r"\bapproach\b|\bexcision\b|\bdissection\b|\breconstruction\b|\bimplant(ation)?\b|\bstimulation\b|"
                       r"\bexploration\b|\bdrainage\b|\breanimation\b|\bfundamentals\b|\bsialendoscopy\b|\bmicrolaryngoscopy\b|"
                       r"\besophagoscopy\b|\binjection\b|\badvancement\b|\bdraf\b|\bfess\b|\bantrostomy\b|\bsalvage\b|\bdecannulation\b|microsurgery|\bbiopsy\b|\bligation\b)", re.I)


DISEASE_FIRST = re.compile(r"\b(hemorrhage|residual|complications?|injury|failure|syndrome)\b", re.I)
# v91: decisions and treatment/management principles have no "why it happens / how it presents".
DECISION = re.compile(r"\b(decisions?|decision-making|candidacy|management by)\b", re.I)
PRINCIPLES = re.compile(r"\b(principles|foundations|framework|immunology|immunotherapy|stewardship|safety|"
                        r"management|adjuvant therapy|radioactive iodine|surveillance|triage|nutrition|anesthesia|"
                        r"goals-of-care|hearing aids|bone-conduction devices|appliance therapy|troubleshooting|"
                        r"rehabilitation|programming|activation|phenotyping|geriatric|immunocompromised host|"
                        r"professional voice|examination)\b", re.I)


def teachback_prompt(topic):
    t = str(topic or "this topic")
    if DISEASE_FIRST.search(t) and not ANATOMY.search(t):
        return (f"Explain {t} to a junior resident in 60 seconds: why it happens, how it presents, and the one "
                f"decision that most often goes wrong.")
    if DECISION.search(t):
        return (f"Walk a junior resident through {t} in 60 seconds: who the decision applies to, the factors that "
                f"tip it one way or the other, and the mistake that most often leads to the wrong choice.")
    if PRINCIPLES.search(t) and not ANATOMY.search(t):
        return (f"Teach {t} to a junior resident in 60 seconds: the core principles, how they change what you do "
                f"for the patient, and the mistake that most often causes harm.")
    if ANATOMY.search(t):
        return (f"Walk a junior resident through {t} in 60 seconds: the key structures and how they relate, the "
                f"landmarks you use to find them, and the one relationship that most often leads to an injury or a "
                f"wrong answer.")
    if TEST.search(t):
        return (f"Teach {t} to a junior resident in 60 seconds: what the test measures or shows, what normal looks "
                f"like, and the finding that is most often misread.")
    if OPERATION.search(t):
        return (f"Brief a junior resident on {t} in 60 seconds: who needs it, the critical steps and danger "
                f"structures, and the complication you must recognize early.")
    return (f"Explain {t} to a junior resident in 60 seconds: why it happens, how it presents, and the one "
            f"decision that most often goes wrong.")


def install_teachback_v810(app):
    app.jinja_env.globals["teachback_prompt_v810"] = teachback_prompt
    return True
