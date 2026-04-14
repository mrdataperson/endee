from sentence_transformers import SentenceTransformer
import numpy as np

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample data
documents = [
    {"id": "1", "text": "Java developer with 3 years experience in Spring Boot"},
    {"id": "2", "text": "Frontend developer with React and JavaScript"},
    {"id": "3", "text": "Machine learning engineer with Python and TensorFlow"},
    {"id": "4", "text": "Backend developer with Node.js and MongoDB"}
]

# Convert to embeddings
doc_embeddings = [model.encode(doc["text"]) for doc in documents]


# Cosine similarity
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# Search function
def search(query):
    query_embedding = model.encode(query)

    scores = []
    for i, emb in enumerate(doc_embeddings):
        score = cosine_similarity(query_embedding, emb)
        scores.append((score, documents[i]["text"]))

    scores.sort(reverse=True)

    print("\n🔍 Top Results:")
    for score, text in scores[:3]:
        print(f"{round(score, 3)} → {text}")


# Run
if __name__ == "__main__":
    print("✅ System Ready (Endee-based logic simulated)\n")

    while True:
        query = input("Enter your query: ")
        search(query)