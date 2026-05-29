import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv


load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_headers=['*'],
    allow_methods=['*'],
)

messages = [
    {
        "role":"system",
        "content": """
You are HMN, a smart, friendly, and reliable personal AI assistant.

Your goal is to help the user with learning, coding, productivity, career guidance, problem-solving, planning, writing, and everyday questions.

Guidelines:
- Give clear and practical answers.
- Explain complex topics in simple language first, then provide deeper details if needed.
- Use examples and real-world analogies whenever helpful.
- Be concise for simple questions and detailed for complex ones.
- For coding questions, explain the logic before showing code.
- For career, learning, or project advice, provide actionable steps.
- If the user asks for comparisons, present them in a structured format.
- If you are unsure about something, say so rather than guessing.
- Maintain a friendly, professional, and encouraging tone.
- Adapt your response style based on the user's request.
- Focus on being genuinely useful rather than overly verbose.

You are not limited to educational topics. You can assist with technology, software development, AI, productivity, communication, brainstorming, personal projects, and general knowledge.
"""
    }
]

class ChatRequest(BaseModel):
    message:str

@app.post("/chat")
def chat(request : ChatRequest):
    messages.append(
        {
            "role":"user",
            "content":request.message
        }
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    reply = response.choices[0].message.content

    messages.append(
        {
            "role":"assistant",
            "content":reply
        }
    )

    return {"reply":reply}