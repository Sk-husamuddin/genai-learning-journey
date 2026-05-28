## 📄 Project 2 — README.md

Copy this:

```markdown
# Project 2 — HMN Study Assistant Chatbot 🤖

A terminal-based AI chatbot that remembers 
conversations across sessions, built using 
Python and Groq API.

## Features
- 🧠 Persistent memory — remembers across sessions
- 🌊 Streaming responses — word by word output
- 🔄 Auto retry — handles API errors gracefully
- 🗑️ Clear command — reset conversation history
- 📚 Study assistant personality — explains 
  simply then deeply with real world analogies

## Tech Stack
- Python 3.12
- Groq API (Llama 3.3 70B)
- python-dotenv
- JSON file storage

## Project Structure
```
project-2-chatbot/
├── chatbot.py       ← main chatbot code
├── history.json     ← conversation history
├── .env             ← API key (not on GitHub)
├── .gitignore       ← ignores .env and venv
└── README.md        ← this file
```

## How to Run

### 1. Clone the repo
```bash
git clone https://github.com/Sk-husamuddin/genai-learning-journey.git
cd project-2-chatbot
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install groq python-dotenv
```

### 4. Add your API key
```bash
nano .env
```
```
GROQ_API_KEY=your-key-here
```

### 5. Run the chatbot
```bash
python3 chatbot.py
```

## Commands
| Command | Action |
|---------|--------|
| Type anything | Chat with HMN |
| `clear` | Reset conversation history |
| `quit` | Save and exit |

## What I Learned
- Groq API integration with Python
- Multi-turn conversation management
- Streaming responses implementation
- JSON file persistence
- Error handling and retries
- Virtual environments and .env files

## Built By
Husamuddin | GenAI Learning Journey | Week 3
Phase 1 — Foundations | May 2026
```

---