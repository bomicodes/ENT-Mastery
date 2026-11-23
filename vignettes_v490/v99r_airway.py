"""v99: anastomotic risk and optimization before tracheal / cricotracheal resection."""

SGS = "v6-laryngology-voice-swallowing-subglottic-tracheal-stenosis"

VIGNETTES = [
    {
        "topic": "Subglottic / Tracheal Stenosis",
        "concept_id": SGS,
        "stem": "A 58-year-old man with insulin-dependent diabetes has grade III post-intubation subglottic stenosis 1.5 cm below the vocal folds, 4.5 cm long, after a failed tracheal resection 2 years ago. He has had a tracheostomy since then. He is evaluated for repeat cricotracheal resection. Which feature of his case is NOT an independent risk factor for anastomotic complications?",
        "choices": ["Reoperation after prior resection", "Diabetes", "Resection length of 4 cm or more", "Male sex"],
        "answer": 3,
        "explanation": "In the largest tracheal and laryngotracheal resection series (about 900 patients, 9% anastomotic complications), the independent predictors were reoperation, diabetes, resection length of 4 cm or more, laryngotracheal rather than tracheal resection, age 17 or younger, and a preoperative tracheostomy. This patient carries most of them, so staging with a T-tube or tracheostomy, maximal release maneuvers, or a nonresection alternative deserves discussion. Sex was not a predictor.",
        "why_wrong": ["Prior resection is one of the strongest independent predictors of anastomotic failure.", "Diabetes independently predicted anastomotic complications in the series.", "Resections of 4 cm or more carry more tension and more failures.", "Correct."],
        "board_pearl": "Anastomotic failure risk: reoperation, diabetes, at least 4 cm, laryngotracheal resection, age 17 or younger, preoperative tracheostomy.",
        "curveball": "Postoperative day 5 he develops subcutaneous emphysema and an air leak. What is the first step?",
        "curveball_answer": "Suspect anastomotic dehiscence. Secure the airway first, ideally by flexible bronchoscopy to assess the anastomosis and pass a tube beyond the defect, or by a tracheostomy placed through the defect. Then decide between drainage, repair or a T-tube, and image for mediastinitis.",
        "learning_stage": "senior_decision",
        "focus": "complication",
    },
    {
        "topic": "Subglottic / Tracheal Stenosis",
        "concept_id": SGS,
        "stem": "A 46-year-old woman with granulomatosis with polyangiitis has grade III subglottic stenosis that recurred after three dilations. She takes prednisone 20 mg daily for active renal and sinonasal disease, her HbA1c is 9.1%, and she smokes. She asks to proceed with cricotracheal resection now. What is the most appropriate next step?",
        "choices": ["Proceed with cricotracheal resection this month while her airway is still patent", "Defer resection and optimize: achieve GPA remission, wean steroids, control diabetes and stop smoking, using endoscopic treatment meanwhile", "Perform laryngotracheal reconstruction with a rib graft instead, which tolerates steroids", "Place a permanent tracheostomy and abandon reconstruction"],
        "answer": 1,
        "explanation": "Open airway surgery in an inflamed airway on systemic steroids, with poorly controlled diabetes and ongoing smoking, has a high risk of anastomotic dehiscence and restenosis. Endoscopic dilation, incision and intralesional steroid can bridge her while rheumatology induces remission. Steroids are weaned (ideally off before resection), glycemic control and smoking cessation are achieved, and resection is reconsidered once the disease is quiescent.",
        "why_wrong": ["Operating during active GPA on steroids invites dehiscence and restenosis.", "Correct.", "Grafted reconstruction heals poorly in the same inflamed, steroid-treated airway.", "A permanent tracheostomy is premature when endoscopic control and optimization remain options."],
        "board_pearl": "Before open airway surgery: quiet airway, steroids weaned, diabetes controlled, no smoking, inflammatory disease in remission.",
        "curveball": "Her GPA is in remission off prednisone, but her BMI is 41 and she has untreated severe OSA. What do you address before resection?",
        "curveball_answer": "Treat the sleep apnea and pursue weight loss where feasible. Obesity and untreated OSA raise airway and perioperative risk, and a short, heavy neck limits extension and increases anastomotic tension. Assess cardiopulmonary reserve as well before an elective resection.",
        "learning_stage": "application",
        "focus": "management",
    },
]
