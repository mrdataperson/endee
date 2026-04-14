# 🚀 AI Resume Semantic Search System

### Endee-Inspired Vector Search + Explainable AI + Chat UI

---

## 📌 Overview

This project implements a **semantic resume search system** that retrieves the most relevant candidate profiles using **vector embeddings and similarity search**.

Unlike traditional keyword-based search, this system understands the **context and meaning** of queries, enabling intelligent retrieval of resumes.

The system is designed following **modern AI architecture patterns**, including vector databases, semantic search, and retrieval pipelines.

---

## 🎯 Objective

To build a real-world AI application that demonstrates:

* Semantic search using vector embeddings
* Retrieval based on meaning (not keywords)
* Explainable AI outputs
* Chat-based interaction system

---

## 🧠 Key Concepts Demonstrated

* Vector Embeddings (Sentence Transformers)
* Semantic Search
* Cosine Similarity
* Retrieval Pipeline (RAG-inspired)
* Explainable AI (match reasoning)
* Conversational UI (Streamlit Chat Interface)

---

## ⚙️ Tech Stack

* Python
* Sentence Transformers (`all-MiniLM-L6-v2`)
* NumPy
* Streamlit (Chat UI)

---

## 🏗️ System Architecture

1. Resume text is converted into vector embeddings
2. Embeddings are stored (vector storage layer)
3. User query is converted into embedding
4. Similarity is computed using cosine similarity
5. Top matching resumes are retrieved
6. Results are explained and displayed via chat UI

---

## 💬 Chat-Based Interface

The system includes a **ChatGPT-style interface** where users can:

* Enter natural language queries
* Receive ranked results
* View similarity scores
* Understand why a result matched

---

## 🔥 Features

* 🔍 Semantic resume search
* 🤖 Chat-based interaction
* 📊 Similarity scoring
* 💡 Explainable AI (match reasoning)
* ⚡ Fast and lightweight implementation

---

## 🧪 Example Queries

* "Java backend developer"
* "Machine learning engineer"
* "React frontend developer"

---

## 📊 Sample Output

```
🔍 Top Matches:

📄 Java developer with 3 years experience in Spring Boot
🔢 Score: 0.91
💡 Matched keywords: java, developer

📄 Backend developer with Node.js and MongoDB
🔢 Score: 0.85
💡 Matched keywords: developer
```

---

## 🚀 How to Run

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd ai-search
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Chat UI

```bash
python -m streamlit run app.py
```

---

## 📸 Demo


<img width="1919" height="1199" alt="Screenshot 2026-04-14 132031" src="https://github.com/user-attachments/assets/4678f9f7-24a3-4642-b005-d79d36254b95" />
<img width="1919" height="1124" alt="Screenshot 2026-04-14 132038" src="https://github.com/user-attachments/assets/057be9c4-96f3-4a5d-8222-91fb892b174e" />
<img width="1915" height="1127" alt="Screenshot 2026-04-14 132043" src="https://github.com/user-attachments/assets/5ebbc2d6-c277-40a5-9dd0-b591c7e9075a" />
<img width="1919" height="1139" alt="Screenshot 2026-04-14 132616" src="https://github.com/user-attachments/assets/34b35b54-80d3-418b-8d3b-4bfa950683d4" />
<img width="1919" height="1143" alt="Screenshot 2026-04-14 132825" src="https://github.com/user-attachments/assets/7f9a8252-debc-450f-9052-477a953ce7c5" />


---

## ⚠️ Endee Integration Note (Important)

This project is built in alignment with the **Endee vector database architecture and workflow**.

* The system follows the same pipeline:

  * Embedding generation
  * Vector storage
  * Similarity-based retrieval

* Due to time constraints and environment limitations during the evaluation window, the vector storage layer is **implemented locally (in-memory)** while preserving the same retrieval logic used in vector databases like Endee.

This approach ensures:

* Accurate demonstration of semantic search principles
* Full understanding of vector database workflows
* A working, testable system within the given timeframe

---

## 📈 Future Enhancements

* Full integration with Endee vector database backend
* Resume upload (PDF parsing)
* Persistent vector storage
* Advanced RAG with LLM integration
* Candidate ranking dashboard

---

## 🏁 Conclusion

This project demonstrates how modern AI systems leverage **vector embeddings and semantic understanding** to build intelligent search applications.

It reflects the ability to:

* Design AI pipelines
* Implement semantic retrieval
* Build user-facing AI systems under time constraints

---

## 👨‍💻 Author

Developed as part of an AI/ML Internship Evaluation.

---

## ⭐ Acknowledgment

Inspired by modern vector database systems such as **Endee** and real-world AI retrieval architectures.

