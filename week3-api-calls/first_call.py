import os
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Create client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Make first API call
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "What is neural networks?"}
    ]
)

# Print response
print(response.choices[0].message.content)
