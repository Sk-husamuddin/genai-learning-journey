# PDF Q&A RAG Chatbot

A retrieval-augmented generation chatbot that answers questions from PDF documents and shows source citations.

## Overview

This project lets you:

1. Load one or more PDF files.
2. Extract and chunk the text.
3. Store embeddings in ChromaDB.
4. Ask questions about the uploaded documents.
5. Get answers grounded in the retrieved context.

## How It Works

1. You provide a PDF path.
2. PyMuPDF extracts text page by page.
3. The text is split into overlapping chunks.
4. Sentence Transformers creates embeddings for each chunk.
5. ChromaDB stores the vectors and metadata.
6. Your question is embedded and searched against ChromaDB.
7. The top matching chunks are sent to Groq for answer generation.
8. The app prints the answer and the source pages.

## Tech Stack

| Component | Technology |
| --- | --- |
| PDF Loading | PyMuPDF |
| Chunking | Custom overlap strategy |
| Embeddings | Sentence Transformers (`all-MiniLM-L6-v2`) |
| Vector Database | ChromaDB |
| LLM | Groq (`llama-3.3-70b-versatile`) |
| Interface | CLI |

## Project Structure

```text
RAG-chatbot/
|-- main.py
|-- pdf_loader.py
|-- vector_store.py
|-- rag_engine.py
|-- testing.pdf
|-- .env
|-- .gitignore
`-- readme.md
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Sk-husamuddin/genai-learning-journey
cd week5-RAG/RAG-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install pymupdf chromadb sentence-transformers groq python-dotenv
```

### 4. Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the chatbot

```bash
python main.py
```

## Usage

1. Enter a PDF path when prompted.
2. Repeat for any additional PDFs.
3. Type `done` to start chatting.
4. Ask questions about the uploaded files.
5. Type `quit` to exit.

Example:

```text
Enter the pdf path or 'done' to start chatting: testing.pdf
testing.pdf loading...
Chatbot Ready !!
You: What is machine learning?
```

## Features

- Multiple PDF support
- Source citations with page numbers
- Semantic search instead of keyword matching
- Overlapping chunks to reduce information loss
- Answers grounded in retrieved context
- Fallback behavior when the answer is not in the documents

## Security

- API keys live in `.env`
- `.gitignore` excludes `.env`, `venv/`, `__pycache__/`, and `chroma_db`
- No sensitive data should be committed

## Part of GenAI Learning Journey

This is Project 3 in the learning roadmap.

| Project | Description | Status |
| --- | --- | --- |
| Project 1 | Prompt System Designer | Complete |
| Project 2 | Terminal Chatbot | Complete |
| Project 2.5 | Live Web Chatbot | Complete |
| Project 3 | PDF Q&A RAG Chatbot | CLI Done |
| Project 4 | Research Agent | Coming Soon |
| Project 5 | Capstone App | Coming Soon |

## Author

Shaik Husamuddin

- GitHub: [Sk-husamuddin](https://github.com/Sk-husamuddin/genai-learning-journey)
- Live App: [chatbot-project-two-delta.vercel.app](https://chatbot-project-two-delta.vercel.app)
- Degree: B.Tech CSE/AI-ML, Vijayawada
