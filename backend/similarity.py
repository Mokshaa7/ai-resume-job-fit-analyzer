from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed(text):
    return model.encode(text)


def similarity_score(text1, text2):
    vec1 = embed(text1)
    vec2 = embed(text2)

    score = cosine_similarity([vec1], [vec2])[0][0]
    return score


if __name__ == "__main__":
    resume_text = """
    Data science student skilled in Python, machine learning,
    data analysis, and deep learning projects.
    """

    job_text = """
    Looking for a machine learning intern with Python,
    data analysis, and model building experience.
    """

    score = similarity_score(resume_text, job_text)
    print("Similarity score:", round(score, 3))
