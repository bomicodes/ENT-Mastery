"""v30.5 — source-grounded laryngeal cancer Concept Hub separation.

The duplicate audit flags Supraglottic Cancer <-> Glottic Cancer as a high-similarity
pair. These cards should not be generic copies of "laryngeal SCC." Supraglottic cancer
owns lymphatic/neck risk and swallow-preserving supraglottic treatment; glottic cancer
owns voice, cord mobility, paraglottic/cartilage spread, and early glottic preservation.
"""

import re

DOMAIN = "Head & Neck Oncology"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


LARYNX_V305 = {
    "supraglottic cancer": {
        "recognize": (
            "Recognize supraglottic SCC as a LYMPHATIC + SWALLOWING cancer phenotype, not simply glottic cancer located higher. It arises from the suprahyoid/infrahyoid epiglottis, aryepiglottic folds, arytenoids, false cords, or ventricular surface. Presenting symptoms may be throat pain, odynophagia, referred otalgia, dysphagia, muffled voice, hemoptysis, neck mass, or later airway symptoms; hoarseness can be late unless the tumor approaches the ventricle/glottis. Because the supraglottis has abundant bilateral lymphatics, occult or clinically evident cervical nodal disease is far more important at presentation than in an otherwise comparable early glottic primary."
        ),
        "localize": (
            "Map the tumor by SUPRAGLOTTIC SUBSITE and deep-space spread. Endoscopy should define epiglottic, false-cord, aryepiglottic-fold and arytenoid involvement; cross-sectional imaging should assess the pre-epiglottic and paraglottic spaces, tongue base/vallecula, pyriform sinus, thyroid cartilage, extralaryngeal extension and cervical nodes. T category is site-specific: T1 is confined to one supraglottic subsite with normal vocal-fold mobility; T2 involves more than one adjacent supraglottic subsite or an adjacent region such as tongue base/vallecula/medial pyriform wall without fixation; T3 includes vocal-fold fixation and/or invasion of key deep spaces such as the pre-epiglottic/paraglottic space, with more advanced cartilage/extralaryngeal invasion moving to T4. The neck is usually mapped bilaterally because midline and crossing lymphatics make contralateral risk clinically meaningful."
        ),
        "workup": (
            "Perform complete flexible laryngoscopy with documentation of airway, swallowing secretions, vocal-fold mobility and synchronous mucosal disease, then obtain contrast CT or MRI of the larynx/neck when deep-space, cartilage or nodal anatomy matters. Direct laryngoscopy/biopsy establishes histology and permits precise exposure mapping before a conservation operation. Chest imaging and PET/CT are used according to stage and treatment plan. Evaluate pulmonary reserve, baseline swallowing, nutrition, dentition and performance status because a technically resectable supraglottic lesion may still be a poor functional candidate for partial laryngectomy. For cN0 disease, do not let a negative palpation exam erase the supraglottis's substantial occult nodal risk."
        ),
        "manage": (
            "Treat early T1-T2 supraglottic cancer with a single definitive modality when appropriate: radiation or transoral/open supraglottic resection can both be curative, with selection driven by exposure, subsite/deep extension, swallowing reserve, voice/swallow goals and institutional expertise. Unlike early glottic cancer, management must usually include the at-risk cervical lymphatics—elective nodal irradiation or appropriately selected neck dissection, often bilateral depending on primary location. Locally advanced but larynx-preservable disease may be treated with concurrent chemoradiation; extensive cartilage destruction, major extralaryngeal invasion, a nonfunctional larynx, or disease poorly suited to conservation can favor total laryngectomy with pathology-directed adjuvant therapy."
        ),
        "operate": (
            "A supraglottic conservation operation succeeds only if it achieves both oncologic clearance and a usable airway/swallow. Transoral laser/TORS or open supraglottic laryngectomy removes the supraglottic primary while preserving the true vocal folds and enough functional larynx for rehabilitation. Preoperatively determine whether the tumor crosses into anatomy that defeats safe conservation—deep tongue-base extension, extensive paraglottic/cartilage invasion, functionally critical bilateral arytenoid involvement, or other disease requiring a larger resection. Plan the neck operation from nodal risk and clinical disease rather than treating it as an afterthought. After supraglottic resection, aspiration risk and swallowing rehabilitation are central postoperative issues; oncologic preservation of the organ is not success if the larynx remains chronically nonfunctional."
        ),
        "teach": (
            "Chief/boards discriminator: SUPRAGLOTTIS = NODES + PRE-EPIGLOTTIC/PARAGLOTTIC SPACES + SWALLOW. A small supraglottic primary can have meaningful bilateral occult nodal risk, whereas a small glottic primary usually does not. Ask three questions: (1) which supraglottic subsite/deep space is involved, (2) what neck treatment is required, and (3) can this patient functionally tolerate a conservation strategy? Supraglottic laryngectomy is a function-selective operation, not merely a smaller total laryngectomy; baseline pulmonary/swallowing reserve matters. This card intentionally ends at supraglottic-specific management rather than repeating generic laryngeal SCC staging and chemoradiation boilerplate."
        ),
        "tags": ["supraglottic cancer", "supraglottic SCC", "pre-epiglottic space", "paraglottic space", "supraglottic laryngectomy", "bilateral neck", "occult nodal disease", "larynx preservation"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — laryngeal cancer anatomy, staging, neck risk, conservation surgery and organ preservation",
            "K.J. Lee's Essential Otolaryngology, 12e — supraglottic carcinoma staging and treatment",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — Laryngeal Cancer: Supraglottic Site and supraglottic laryngectomy",
            "ASCO Clinical Practice Guideline Update: Use of Larynx-Preservation Strategies in the Treatment of Laryngeal Cancer (JCO 2018;36:1143-1169)",
            "NCI Laryngeal Cancer Treatment (PDQ), Health Professional Version — site-specific staging and treatment options",
        ],
    },
    "glottic cancer": {
        "recognize": (
            "Recognize glottic SCC as a VOICE + MOBILITY cancer phenotype. It arises from the true vocal folds/anterior or posterior commissure and commonly declares itself early through persistent hoarseness, so many tumors are diagnosed before nodal spread. Early true-cord disease has relatively sparse lymphatic drainage compared with the supraglottis; therefore an otherwise favorable T1-T2 cN0 glottic cancer usually does not require elective neck treatment. Airway symptoms, dysphagia, odynophagia, aspiration, neck nodes or vocal-fold fixation suggest larger/deeper disease and should move the resident away from an 'early cord lesion' mental model."
        ),
        "localize": (
            "Localize the lesion by cord, commissure, mobility and DEEP EXTENSION. Endoscopy must document one versus both true cords, anterior/posterior commissure involvement, subglottic/supraglottic extension and normal versus impaired versus fixed mobility. For glottic staging, T1 is confined to the vocal cord(s) with normal mobility (T1a one cord, T1b both); T2 extends to supraglottis/subglottis and/or causes impaired mobility; T3 includes vocal-fold fixation and/or paraglottic-space invasion and/or inner-cortex thyroid-cartilage invasion; T4a extends through the outer thyroid cartilage or beyond the larynx. Anterior-commissure involvement matters surgically because of exposure and the close relationship to thyroid cartilage, but it does not by itself substitute for the formal T criteria."
        ),
        "workup": (
            "Perform flexible laryngoscopy/stroboscopic assessment when useful, documenting cord mobility and the surface extent of the lesion; obtain tissue by direct laryngoscopy with careful mapping when malignancy is suspected. Thin-section contrast CT or MRI becomes increasingly important when impaired/fixed mobility, subglottic extension, paraglottic-space disease, cartilage invasion or extralaryngeal spread is suspected; a tiny superficial mobile-cord lesion may not need the same imaging burden as an advanced tumor. Evaluate the neck according to stage rather than reflexively treating it: early glottic cN0 disease has low occult nodal risk, while advanced glottic tumors acquire cervical/paratracheal nodal risk. Baseline voice, airway and pulmonary status shape which preservation strategy will actually preserve useful function."
        ),
        "manage": (
            "For most T1 and selected T2 glottic cancers, choose a single larynx-preserving modality—transoral laser microsurgery/cordectomy or definitive radiation are standard options, selected by tumor exposure/extent, voice priorities, comorbidity, patient preference and local expertise. Do not add elective neck treatment to a straightforward early cN0 glottic lesion simply because supraglottic cancer needs it. More extensive T2/T3 disease may still be approached with selected conservation surgery or concurrent chemoradiation when laryngeal function and tumor anatomy are suitable. T4a disease with cartilage penetration/extralaryngeal extension, or a severely dysfunctional larynx, commonly shifts the balance toward total laryngectomy with appropriate neck treatment and pathology-directed adjuvant therapy rather than pursuing organ preservation at any cost."
        ),
        "operate": (
            "Match resection to DEPTH and FUNCTION. Superficial T1 disease may be treated with transoral laser excision/cordectomy while preserving uninvolved vocal-fold tissue; selected open partial laryngeal procedures remain options when anatomy and expertise support them. Before conservation surgery, determine whether the lesion can be exposed adequately, whether arytenoid/cricoarytenoid function can be preserved, and whether paraglottic/cartilage spread exceeds the planned resection. A fixed cord is not just 'worse hoarseness'—it is a staging and deep-invasion clue that changes the operation. For total laryngectomy candidates, counsel about permanent stoma, alaryngeal speech options, swallowing, pulmonary rehabilitation and the distinction between an anatomically present larynx and a functional one."
        ),
        "teach": (
            "Chief/boards discriminator: GLOTTIS = HOARSENESS + CORD MOBILITY + DEPTH, with LOW early nodal risk. T1a = one cord, normal mobility; T1b = both cords, normal mobility; T2 = extension and/or impaired mobility; T3 = fixation and/or paraglottic/inner thyroid-cartilage invasion. Early cN0 glottic cancer is commonly treated with one local modality and no elective neck treatment—the opposite of the supraglottic reflex. The boards trap is to call every larynx-preservation plan equivalent: preserving the organ is worthwhile only when oncologic control and useful speech/swallow/airway function are realistic."
        ),
        "tags": ["glottic cancer", "glottic SCC", "vocal fold mobility", "T1a", "T1b", "cordectomy", "transoral laser microsurgery", "paraglottic space", "larynx preservation"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — glottic cancer staging, transoral surgery, partial laryngectomy and organ preservation",
            "K.J. Lee's Essential Otolaryngology, 12e — glottic carcinoma staging and treatment",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — Laryngeal Cancer: Glottic Site and management",
            "ASCO Clinical Practice Guideline Update: Use of Larynx-Preservation Strategies in the Treatment of Laryngeal Cancer (JCO 2018;36:1143-1169)",
            "NCI Laryngeal Cancer Treatment (PDQ), Health Professional Version — site-specific staging and treatment options",
        ],
    },
}


def apply_larynx_site_rebuild_v305(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        payload = LARYNX_V305.get(_norm(module.get("topic")))
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v305"] = True
        module["semantic_role_v305"] = (
            "supraglottic_lymphatic_swallow_pathway"
            if _norm(module.get("topic")) == "supraglottic cancer"
            else "glottic_voice_mobility_depth_pathway"
        )
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
