import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

stream = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role":"user",
            "content":"Explain how the internet works in detail"
        }
    ],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content,end="",flush=True)

print()


