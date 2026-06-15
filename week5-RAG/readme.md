# 📄 PDF Q&A RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions from your PDF documents with accurate source citations (filename + page number).

Built from scratch to understand every stage of the RAG pipeline—without relying on LangChain abstractions. This project demonstrates document ingestion, chunking, embeddings, vector search, retrieval, and LLM-powered answer generation.

---

## 🚀 Overview

Upload one or more PDF documents and ask questions in natural language.

The chatbot:

* Extracts text from PDFs
* Splits content into overlapping chunks
* Generates embeddings using Sentence Transformers
* Stores vectors in ChromaDB
* Retrieves the most relevant chunks using semantic search
* Generates grounded answers using Groq LLM
* Displays source citations with filename and page number

---

## 🧠 System Architecture

```text
PDF Upload (multiple PDFs supported)
        │
        ▼
PyMuPDF Text Extraction
        │
        ▼
Chunking (500 chars, 50 overlap)
        │
        ▼
Sentence Transformers Embeddings
(all-MiniLM-L6-v2)
        │
        ▼
ChromaDB Vector Storage
(filename + page metadata)
        │
        ▼
User Question
        │
        ▼
Question Embedding
        │
        ▼
Semantic Similarity Search
(Top-K Relevant Chunks)
        │
        ▼
Retrieved Context + Question
        │
        ▼
Groq LLM
(llama-3.3-70b-versatile)
        │
        ▼
Answer + Source Citations
```

---

## ✨ Features

### Document Processing

* Multiple PDF upload support
* Page-wise text extraction using PyMuPDF
* Overlapping chunking strategy
* Metadata tracking for source attribution

### Retrieval-Augmented Generation

* Semantic search using vector embeddings
* ChromaDB persistent vector storage
* Top-k relevant chunk retrieval
* Grounded responses based on retrieved context

### Source Attribution

* Displays source filename
* Displays source page number
* Improves answer transparency and trustworthiness

### Interfaces

* Command Line Interface (CLI)
* Modern Web Interface
* FastAPI Backend
* Vanilla HTML/CSS/JavaScript Frontend

### Reliability

* Prevents hallucinations by restricting answers to retrieved context
* Returns fallback responses when information is unavailable

---

## 🛠️ Tech Stack

| Layer                | Technology              |
| -------------------- | ----------------------- |
| Programming Language | Python                  |
| PDF Processing       | PyMuPDF                 |
| Embeddings           | Sentence Transformers   |
| Embedding Model      | all-MiniLM-L6-v2        |
| Vector Database      | ChromaDB                |
| LLM Provider         | Groq                    |
| LLM Model            | llama-3.3-70b-versatile |
| Backend API          | FastAPI                 |
| Frontend             | HTML, CSS, JavaScript   |
| Deployment           | Railway + Vercel        |

---

## 📂 Project Structure

```text
PDF-Q-A-Chatbot/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── pdf_loader.py
├── vector_store.py
├── rag_engine.py
├── backend.py
├── main.py
│
├── requirements.txt
├── .env
├── .gitignore
├── Procfile
└── README.md
```

### File Description

| File            | Purpose                         |
| --------------- | ------------------------------- |
| pdf_loader.py   | PDF extraction and chunking     |
| vector_store.py | ChromaDB storage operations     |
| rag_engine.py   | Retrieval and answer generation |
| backend.py      | FastAPI server                  |
| main.py         | CLI chatbot                     |
| frontend/       | Web application                 |

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/Sk-husamuddin/PDF-Q-A-Chatbot.git

cd PDF-Q-A-Chatbot
```

### 2. Create Virtual Environment

Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 💻 Running the Application

### Option A — CLI Version

```bash
python main.py
```

Example:

```text
Enter PDF path or 'done' to start chatting:
resume.pdf

✅ Extracted 15 chunks from resume.pdf
✅ Added 15 chunks from resume.pdf

Enter PDF path or 'done' to start chatting:
done

Chatbot Ready!!
===================================

You: What skills does the candidate have?

Answer:
The candidate has experience in Python, FastAPI,
Machine Learning, and Generative AI.

Sources:
📄 resume.pdf (page 1)
```

---

### Option B — Web Version

Start FastAPI:

```bash
uvicorn backend:app --reload
```

Open:

```text
frontend/index.html
```

in your browser.

---

## 📸 Screenshots

### Upload PDF

*Add screenshot here*

```text
screenshots/upload.png
```

### Chat Interface

*Add screenshot here*

```text
screenshots/chat.png
```

### Source Citations

*Add screenshot here*

```text
screenshots/sources.png
```

---

## 🔍 Key Learning Outcomes

Through this project I learned:

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Text Chunking Strategies
* Embeddings and Similarity Search
* Source Attribution
* FastAPI Development
* REST APIs
* Frontend-Backend Integration
* LLM Integration using Groq
* End-to-End AI Application Development

---

## 🌐 Deployment

### Backend

Deploy FastAPI application on Railway.

Set:

```env
GROQ_API_KEY=your_api_key
```

as an environment variable.

### Frontend

Deploy frontend on Vercel.

Update:

```javascript
const BACKEND_URL = "YOUR_RAILWAY_URL"
```

inside `script.js`.

---

## 🚀 Future Improvements

* Drag and drop PDF upload
* Upload multiple PDFs in a single request
* Streaming LLM responses
* Chat history persistence
* Hybrid Search (Keyword + Semantic)
* Docker Containerization
* User Authentication
* PDF Preview Support
* Reranking Models
* Conversational Memory

---

## 📍 GenAI Learning Roadmap

This project is part of a structured Generative AI learning journey.

| Project     | Description                | Status         |
| ----------- | -------------------------- | -------------- |
| Project 1   | Prompt System Designer     | ✅ Completed    |
| Project 2   | Terminal Chatbot           | ✅ Completed    |
| Project 2.5 | Full-Stack Web Chatbot     | ✅ Completed    |
| Project 3   | PDF Q&A RAG Chatbot        | ✅ Completed    |
| Project 4   | Research Agent             | 🔄 Coming Soon |
| Project 5   | Capstone GenAI Application | 🔄 Coming Soon |

---

## 👨‍💻 Author

**Shaik Husamuddin**

B.Tech Computer Science & Engineering

GitHub:
https://github.com/Sk-husamuddin

GenAI Learning Journey:
https://github.com/Sk-husamuddin/genai-learning-journey

---

## 📄 License

This project is licensed under the MIT License.

Feel free to fork, modify, and build upon it for educational purposes.
