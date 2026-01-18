GENERIC_WORDS = {
    "data", "learning", "model", "models", "system", "systems",
    "experience", "performance", "real", "world", "build", "face"
}

def extract_keywords(text, top_n=15):
    words = text.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # Sort by frequency
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return [word for word, _ in sorted_words[:top_n]]


def explain_match(resume_text, job_text):
    resume_keywords = set(extract_keywords(resume_text))
    job_keywords = set(extract_keywords(job_text))

    matched = [w for w in resume_keywords.intersection(job_keywords) if w not in GENERIC_WORDS]
    missing = [w for w in job_keywords - resume_keywords if w not in GENERIC_WORDS]


    return {
        "matched_skills": list(matched),
        "missing_skills": list(missing)
    }
