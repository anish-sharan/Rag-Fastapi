🧠 FastAPI + React RAG App with OpenRouter

This project is a Retrieval-Augmented Generation (RAG) system built with FastAPI, React, FAISS, and OpenRouter LLM.
It allows users to upload documents dynamically and ask questions, retrieving answers based on context from uploaded documents.

📂 Features

Dynamic PDF or text document upload
Chunking & FAISS vector store for fast retrieval
RAG pipeline: Retriever → Prompt → OpenRouter LLM
Fully async endpoints for high performance
.env-based configuration for secure API keys
Returns answers + source context
Modern LangChain 0.2+ compatible

⚙️ Tech Stack

Backend: FastAPI, LangChain, FAISS, Python 3.12
Frontend: React, Tailwind CSS (optional)
Vector Store: FAISS
LLM: OpenRouter (OpenAI-compatible API)
Environment Management: python-dotenv

🚀 Quick Start
1️⃣ Clone the repository
git clone https://github.com/anish-sharan/Rag-Fastapi.git
cd Rag-Fastapi

2️⃣ Install dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

requirements.txt should include:

fastapi
uvicorn
python-dotenv
langchain-openai
langchain-huggingface
langchain-community
faiss-cpu
pydantic

3️⃣ Create .env file
In parent/ folder:
OPENAI_API_KEY=sk-or-your-openrouter-key
OPENAI_BASE_URL=https://openrouter.ai/api/v1

Replace with your OpenRouter API key.

4️⃣ Run the backend
uvicorn app.main:app --reload

Health check: http://127.0.0.1:8000/ → {"status": "ok"}

5️⃣ Upload a document
POST /upload endpoint:
Accepts .pdf or .txt files
Automatically chunks and stores embeddings in FAISS

Example:
curl -X POST "http://127.0.0.1:8000/upload" \
  -F "file=@example.pdf"

6️⃣ Ask a question
POST /chat endpoint:
curl -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"question": "What is meditation?"}'

Response:
{
  "answer": "Meditation is a practice of mindfulness..."
}

🗂 Backend Folder Structure
backend/
├─ app/
│  ├─ main.py             # FastAPI app
│  ├─ routes/
│  │  ├─ upload.py        # Upload endpoint
│  │  └─ chat.py          # Chat endpoint
│  ├─ rag/
│  │  ├─ qa_chain.py      # RAG chain using OpenRouter
│  │  ├─ vector_store.py  # FAISS save/load
│  │  └─ embeddings.py    # HuggingFace/OpenRouter embeddings
│  └─ core/
│     └─ config.py        # .env loader
├─ storage/
│  └─ faiss_index/        # FAISS index storage
└─ requirements.txt

⚡ Important Notes
Uses .ainvoke() in async endpoints — required for RunnableSequence in modern LangChain 0.2+
FAISS pickle deserialization requires allow_dangerous_deserialization=True (safe because files are locally generated)
.env is used to store OpenRouter key securely
Can scale with multi-document retrieval by adding more files

📌 Next Steps / Improvements
Streaming responses in frontend
Multi-tenant document storage
Hybrid search (FAISS + BM25)
Source citations for answers
Frontend chat UI with React + Tailwind

🧰 References
LangChain Documentation
OpenRouter API
FAISS Vector Store
