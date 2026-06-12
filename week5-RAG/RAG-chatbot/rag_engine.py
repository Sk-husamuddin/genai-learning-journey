import os
from dotenv import load_dotenv
from groq import Groq
from vector_store import search

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def build_prompt(question, chunks, metadatas):
    context = ""
    for i, (chunk, meta) in enumerate(zip(chunks, metadatas)):
        context += f"""
Source {i+1}: {meta['source']} (page {meta['page']})
Content: {chunk}
─────────────────────────────
"""
    return f"""You are a helpful assistant that answers questions 
based ONLY on the provided context.

Rules:
1. Answer ONLY from the context below
2. If answer not in context → say "I don't know"
3. Never make up information
4. Be concise and clear

Context:
{context}

Question: {question}

Answer:"""

def get_answer(question):
    chunks, metadatas = search(question, n_results=3)
    prompt = build_prompt(question, chunks, metadatas)
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message.content
    
    sources = []
    for meta in metadatas:
        source = f"📄 {meta['source']} (page {meta['page']})"
        if source not in sources:
            sources.append(source)
    
    return answer, sources