import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [
    {
        "role": "system",
        "content": "You are a helpful GenAI tutor."
    },
    {
        "role": "user",
        "content": "What is an API?"
    },
    {
        "role": "assistant",
        "content": "An API is like a waiter — it takes your request to the kitchen and brings back the response."
    },
    {
        "role": "user",
        "content": "Give me a real world example."
    }
]

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages
)

print(response.choices[0].message.content)