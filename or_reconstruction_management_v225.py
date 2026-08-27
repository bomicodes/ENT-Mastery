"""v22.5+ reconstruction OR Tomorrow planning and postoperative management.

Adds high-confidence decision points and rescue priorities for reconstruction cases
whose operative choreography and anatomy are already procedure-specific. Later
reviewed sleep-surgery management is chained here so the existing decision hook
remains atomic.
"""

from or_sleep_management_v229 import apply_or_sleep_management_v229

TARGETS = [
    {
        "slug": "free-flap-basics",
        "title_terms": ("free", "flap"),
        "setup": [
            "Before free-flap reconstruction, define the defect requirements first—lining, cover, bulk, bone/support, dead space, oral competence, speech/swallow function and expected adjuvant therapy—then choose the donor tissue that best matches those needs rather than selecting a flap by familiarity alone.",
            "Review recipient-vessel options and prior neck treatment before incision: previous neck dissection, radiation, vessel sacrifice, atherosclerosis, central access and prior free-flap surgery should lower the threshold for a documented primary and backup recipient-vessel plan, with vein grafting or contralateral exposure considered only when necessary.",
        ],
        "postop": [
            "Treat a new loss or major change in flap Doppler signal, increasing congestion, pallor, brisk dark bleeding, absent bleeding to scratch/pinprick, progressive firmness or unexplained flap swelling as possible vascular compromise until proven otherwise. Correct external compression immediately and escalate for operative exploration without prolonged diagnostic delay when perfusion remains concerning.",
            "Differentiate venous from arterial failure clinically because the appearance and salvage maneuver differ: venous congestion tends to produce a dark, swollen flap with rapid dark bleeding, whereas arterial insufficiency more often produces pallor/coolness with sluggish or absent bleeding. Either pattern is time-critical and should not be managed by observation alone when persistent.",
        ],
    },
    {
        "slug": "free-flap-takeback",
        "title_terms": ("free", "flap", "takeback"),
        "setup": [
            "At suspected free-flap compromise, prioritize time to re-exploration over exhaustive bedside testing when the clinical examination or monitoring signal is convincingly abnormal. Before incision, confirm which artery and vein were used, the pedicle course, any vein graft or coupler, anticoagulation issues and likely mechanical compression points so the takeback is directed rather than exploratory from first principles.",
        ],
        "postop": [
            "After successful flap salvage, increase vigilance rather than returning immediately to routine monitoring: document the revised anastomosis/recipient vessel, cause of failure, pedicle geometry correction, anticoagulation strategy if used, and a very low threshold for repeat exploration because recurrent thrombosis or compression can occur early.",
        ],
    },
    {
        "slug": "facial-nerve-reanimation",
        "title_terms": ("facial", "reanimation"),
        "setup": [
            "Match the reconstruction to denervation duration and available anatomy. When distal facial musculature remains reinnervatable, nerve repair, interposition grafting or nerve transfer can restore dynamic movement; with longstanding denervation and motor end-plate loss, plan a functional muscle transfer rather than expecting a nerve-only procedure to animate chronically denervated native muscle.",
            "Choose donor nerve according to the desired tradeoff: masseteric transfer provides strong, relatively rapid excursion but initially requires bite-driven activation, whereas hypoglossal-based transfer can provide resting tone and spontaneity potential at the cost of tongue-motor morbidity depending on technique. Static eye or oral-commissure procedures may still be necessary when immediate protection/support is needed.",
        ],
        "postop": [
            "Set expectations for delayed recovery after neurorrhaphy or nerve transfer: absence of immediate facial movement is expected, and rehabilitation should begin around the anticipated reinnervation window with neuromuscular retraining rather than maximal strengthening before motor return. New tongue weakness, mastication weakness, wound hematoma or loss of previously present facial function warrants focused examination of the donor and recipient territories.",
        ],
    },
    {
        "slug": "microtia-reconstruction",
        "title_terms": ("microtia",),
        "setup": [
            "Before autologous microtia reconstruction, confirm that chest wall size/cartilage maturity can support the planned framework and map the final auricular position from the contralateral ear, hairline, facial asymmetry and any future external-auditory-canal reconstruction. Sequence canal surgery and framework reconstruction deliberately so one operation does not compromise the soft-tissue envelope required by the other.",
        ],
        "postop": [
            "A tense hematoma, dusky or blistering skin over the framework, rapidly increasing pain, purulent drainage or exposed cartilage requires prompt assessment because pressure necrosis or infection can threaten the framework. Bolsters/suction should maintain contour without creating ischemic pressure, and any concern for pleural injury after rib harvest should trigger respiratory examination and chest evaluation rather than routine discharge assumptions.",
        ],
    },
]


def _resolve(registry, target):
    reg = registry or {}
    if target["slug"] in reg:
        return target["slug"], reg[target["slug"]]
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in target["title_terms"]):
            return slug, op
    return None, None


def _prepend_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in reversed(additions):
        marker = text[:64].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def apply_or_reconstruction_management_v225(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target.get("setup", []))
        op["postop"], c2 = _prepend_unique(op.get("postop"), target.get("postop", []))
        op["reconstruction_management_v225"] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    v229 = apply_or_sleep_management_v229(registry)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing, "v229": v229}
