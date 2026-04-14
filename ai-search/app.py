import streamlit as st
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

doc_embeddings = [model.encode(doc["text"]) for doc in documents]

# Similarity
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Explain
def explain_match(query, text):
    query_words = set(query.lower().split())
    text_words = set(text.lower().split())
    common = query_words.intersection(text_words)
    return f"Matched keywords: {', '.join(common) if common else 'semantic similarity'}"

# Search
def search(query):
    query_embedding = model.encode(query)

    scores = []
    for i, emb in enumerate(doc_embeddings):
        score = cosine_similarity(query_embedding, emb)
        scores.append((score, documents[i]["text"]))

    scores.sort(reverse=True)
    return scores[:3]

# UI
st.set_page_config(page_title="AI Resume Search", page_icon="🤖")
st.title("🤖 AI Resume Search Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat display
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
query = st.chat_input("Ask something like 'Java developer'...")

if query:
    # User message
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    # AI response
    results = search(query)

    response = "### 🔍 Top Matches:\n\n"
    for score, text in results:
        response += f"📄 **{text}**\n"
        response += f"🔢 Score: {round(score, 3)}\n"
        response += f"💡 {explain_match(query, text)}\n\n"

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)