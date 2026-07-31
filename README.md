# 🤖 Support Knowledge Copilot with Verified Citations

An enterprise-style Retrieval-Augmented Generation (RAG) application that answers support questions using internal documentation with **Hybrid Retrieval (Dense + BM25)** and **grounded citations**.

Built using **Python, FastAPI, ChromaDB, BM25, Sentence Transformers, Groq Llama 3.3, and Streamlit**.

---

## 📌 Features

- 🔍 Hybrid Retrieval
  - Dense Vector Search (Sentence Transformers + ChromaDB)
  - Sparse Keyword Search (BM25)
  - Reciprocal Rank Fusion (RRF)

- 📚 Grounded Answers
  - Answers generated only from retrieved documents
  - Source document citations
  - Prevents unsupported responses

- ⚡ FastAPI Backend
  - REST API for inference
  - Interactive Swagger documentation

- 💬 Streamlit Chat Interface
  - ChatGPT-style UI
  - Source citations
  - Sample questions
  - Chat history
  - Clear chat button

- 🧠 Enterprise RAG Pipeline
  - Markdown document ingestion
  - Automatic chunking
  - Embedding generation
  - Persistent vector database
  - BM25 indexing

---

# 🏗 Architecture

```text
                User
                  │
                  ▼
        Streamlit Chat UI
                  │
             HTTP Request
                  │
                  ▼
             FastAPI API
                  │
           generate_answer()
                  │
          Hybrid Retriever
        ┌─────────┴─────────┐
        ▼                   ▼
   Dense Search         BM25 Search
   (ChromaDB)          (Keyword Search)
        │                   │
        └─────────┬─────────┘
                  ▼
      Reciprocal Rank Fusion
                  ▼
       Top Relevant Chunks
                  ▼
         Prompt Construction
                  ▼
          Groq Llama 3.3
                  ▼
     Answer + Source Citations
                  ▼
          Streamlit Response
```

---

# 🚀 Tech Stack

| Component | Technology |
|------------|------------|
| Language | Python 3.11+ |
| API | FastAPI |
| UI | Streamlit |
| Embeddings | BAAI/bge-small-en-v1.5 |
| Vector Database | ChromaDB |
| Sparse Retrieval | BM25 (rank_bm25) |
| LLM | Groq (Llama 3.3 70B Versatile) |
| Retrieval Fusion | Reciprocal Rank Fusion (RRF) |
| Environment | python-dotenv |

---

# 📂 Project Structure

```text
support-copilot/
│
├── app/
│   ├── api.py
│   ├── generator.py
│   ├── hybrid_retriever.py
│   ├── retriever.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── bm25_index.py
│   ├── chunker.py
│   ├── loaders.py
│   ├── prompts.py
│   ├── ingest.py
│   └── .env
│
├── docs/
│      *.md
│
├── vector_db/
│
├── bm25.pkl
│
├── streamlit_app.py
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/support-knowledge-copilot.git

cd support-copilot
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create:

```
app/.env
```

Add:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# 📄 Index Documents

Place your Markdown documents inside

```
docs/
```

Then run

```bash
python -m app.ingest
```

This will

- Load documents
- Chunk documents
- Generate embeddings
- Store vectors in ChromaDB
- Build BM25 index

---

# ▶️ Run FastAPI

```bash
uvicorn app.api:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 💬 Run Streamlit

Open another terminal

```bash
streamlit run streamlit_app.py
```

---

# 💡 Example Questions

- How do I reset my password?
- Explain OAuth authentication.
- What is the refund policy?
- What does AUTH-401 mean?
- How many devices can I connect?

---

# 🔄 Retrieval Pipeline

```
User Question
        │
        ▼
Generate Query Embedding
        │
        ▼
Dense Search (ChromaDB)

+

Sparse Search (BM25)

        │
        ▼
Reciprocal Rank Fusion
        │
        ▼
Top Relevant Chunks
        │
        ▼
Prompt Builder
        │
        ▼
Groq Llama 3.3
        │
        ▼
Answer + Verified Sources
```

---

# 🎯 Why Hybrid Retrieval?

Dense retrieval captures semantic meaning.

Example

```
reset credentials

↓

password recovery
```

BM25 captures exact keywords.

Example

```
AUTH-401

OAuth

API Keys

SKU-203
```

Combining both improves retrieval quality.

---

# 📸 Demo

## Chat Interface

<img width="1919" height="951" alt="Screenshot 2026-07-31 220825" src="https://github.com/user-attachments/assets/57527312-232e-46d8-bb59-4d7e54857c58" />


# 🔮 Future Improvements

- Conversation Memory
- Citation Verification
- Confidence Scoring
- Reranking using Cross Encoder
- Evaluation using RAGAS
- Docker Support
- Authentication
- Deployment on Render

---

# 👨‍💻 Author

**Your Name**

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

# ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.
