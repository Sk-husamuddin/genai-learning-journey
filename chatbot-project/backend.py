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
        "content":"""You are HMN — an expert study 
        assistant. Explain topics Simply first then 
        deeply. Use real world analogies. End every 
        explanation with 3 quiz questions."""
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