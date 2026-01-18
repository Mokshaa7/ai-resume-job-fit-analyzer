SKILL_WEIGHTS = {
    "python": 3,
    "machine learning": 3,
    "ml": 3,
    "nlp": 2,
    "deep learning": 2,
    "tensorflow": 2,
    "pytorch": 2,
    "sql": 2,
    "docker": 1,
    "aws": 1
}

#CORE_SKILLS = {
#     "python",
#     "machine learning",
#     "ml",
#     "nlp",
#     "sql",
#     "tensorflow",
#     "pytorch",
#     "deep learning",
#     "docker",
#     "aws"
# }

def skill_match_score(resume_text, job_text):
    resume_text = resume_text.lower()
    job_text = job_text.lower()

    score = 0
    max_score = 0
    matched_core_skills = []
    missing_core_skills = []

    for skill, weight in SKILL_WEIGHTS.items():
        if skill in job_text:
            max_score += weight
            if skill in resume_text:
                score += weight
                matched_core_skills.append(skill)
            else:
                missing_core_skills.append(skill)

    if max_score == 0:
        return 0.0, [], []

    return score / max_score, matched_core_skills, missing_core_skills
