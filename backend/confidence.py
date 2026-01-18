def generate_confidence_flags(
    semantic_score,
    skill_score,
    cleaned_resume,
    missing_skills
):
    flags = []

    # Low text quality / OCR issue
    if len(cleaned_resume) < 200:
        flags.append("Low resume text quality (possible OCR issue)")

    # Possible false positive
    if semantic_score > 0.75 and skill_score < 0.4:
        flags.append("High semantic match but low skill coverage")

    # Possible false negative
    if semantic_score < 0.5 and skill_score > 0.75:
        flags.append("Strong skills but weak semantic alignment")

    # Missing critical skills
    if len(missing_skills) > 0:
        flags.append("Missing one or more required skills")

    return flags
