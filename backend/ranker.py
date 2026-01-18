from backend.confidence import generate_confidence_flags
from backend.skills import skill_match_score
from backend.explain import explain_match
from backend.preprocessor import clean_text
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from backend.parser import load_resumes_from_folder

# Load embedding model once
model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    local_files_only=True
)


def embed(text):
    return model.encode(text)


def rank_resumes(resumes, job_text):
    job_vec = embed(job_text)
    scores = []

    for name, resume_text in resumes.items():
        cleaned_resume = clean_text(resume_text)

        low_quality = len(cleaned_resume) < 200

        resume_vec = embed(cleaned_resume)

        semantic = cosine_similarity([resume_vec], [job_vec])[0][0]
        skill_score, matched_core_skills, missing_core_skills = skill_match_score(cleaned_resume, job_text)



        final_score = 0.6 * semantic + 0.4 * skill_score

        explanation = explain_match(cleaned_resume, job_text)

        flags = generate_confidence_flags(
    semantic_score=semantic,
    skill_score=skill_score,
    cleaned_resume=cleaned_resume,
    missing_skills=missing_core_skills
)


        scores.append({
        "resume": name,
        "semantic": semantic,
        "skill_score": skill_score,
        "final_score": final_score,
        "matched_core_skills": matched_core_skills,
        "missing_core_skills": missing_core_skills,
        "matched_skills": explanation["matched_skills"],
        "missing_skills": explanation["missing_skills"],
        "flags": flags
})

        

    scores.sort(key=lambda x: x["final_score"], reverse=True)
    return scores


if __name__ == "__main__":
    resumes_folder = "data/resumes"
    job_file = "data/requirements/aiml.txt"

    resumes = load_resumes_from_folder(resumes_folder)

    with open(job_file, "r", encoding="utf-8") as f:
        job_text = clean_text(f.read())

    ranked = rank_resumes(resumes, job_text)

    print("\n🔹 Resume Ranking 🔹")

    for i, r in enumerate(ranked, 1):
        print(f"\n{i}. {r['resume']}")

        print(f"   Final Score: {round(r['final_score'] * 100, 2)}%")
        print(f"   Semantic Score: {round(r['semantic'] * 100, 2)}%")
        print(f"   Skill Match Score: {round(r['skill_score'] * 100, 2)}%")

        print(f"   Core skills matched: {', '.join(r['matched_core_skills']) or 'None'}")
        print(f"   Core skills missing: {', '.join(r['missing_core_skills']) or 'None'}")

        print(f"   Matched keywords: {', '.join(r['matched_skills'][:5])}")
        print(f"   Missing keywords: {', '.join(r['missing_skills'][:5])}")

        if r["flags"]:
            print("   ⚠️ Flags:")
            for flag in r["flags"]:
                print(f"      - {flag}")
