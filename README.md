# 🤖 AI Document Assistant (RAG)

An AI-powered Document Question Answering System built using **Retrieval-Augmented Generation (RAG)**.

Users can upload one or more PDF documents and ask questions in natural language. The application retrieves the most relevant document sections using semantic search and generates answers using **Google Gemini**.

---

# 🚀 Features

- 📄 Upload one or multiple PDF documents
- 📚 Automatic PDF text extraction
- ✂️ Smart text chunking
- 🧠 Semantic Search using Sentence Transformers
- 💾 ChromaDB Vector Database
- 🎯 Cross Encoder Re-ranking
- 🤖 AI Answer Generation using Google Gemini
- 💬 Chat History
- 📖 Source Citation
- 🎨 Streamlit Web Interface

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Frontend | Streamlit |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers |
| Re-ranking | Cross Encoder |
| LLM | Google Gemini |
| PDF Parsing | PyPDF |
| Version Control | Git & GitHub |

---

# ⚙️ How It Works

1. Upload PDF
2. Extract Text
3. Split Text into Chunks
4. Generate Embeddings
5. Store Embeddings in ChromaDB
6. Search Similar Chunks
7. Re-rank Results
8. Generate Final Answer using Gemini

---

# 📁 Project Structure

```text
AI Document Assistant/
│
├── version32_ap.py
├── RAGversion32.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
└── chroma_db/
```

---

# 📸 Screenshots

Screenshots will be added after deployment.

---

# 👨‍💻 Author

**Abhishek Singh**

Aspiring AI Product Manager

LinkedIn: *(Add after updating your profile)*

GitHub: https://github.com/abhisheksingh-aipm

---

# ⭐ Future Improvements

- Multi-document comparison
- Image OCR support
- Voice input
- User authentication
- Cloud deployment
- Conversation memory across sessions
- Citation highlighting