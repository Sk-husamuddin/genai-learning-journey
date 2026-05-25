import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ-API-KEY"))

message=[
    {
        "role":"user",
    "content":"What is API is one line?"
    }
]

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=message
)

print(response.choices[0].message.content)