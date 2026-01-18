from sentence_transformers import SentenceTransformer

# Load pretrained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text):
    return model.encode(text)

if __name__ == "__main__":
    sample = "Python developer with machine learning experience"
    vector = embed_text(sample)
    print("Vector length:", len(vector))
    print(vector[:10])
