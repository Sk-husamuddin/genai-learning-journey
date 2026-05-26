import time
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat_with_retry(messages,retires=3):
    for attempt in range(retires):
        try:
            response=client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Attemp{attempt+1} is failed.\n")
            print(f"Error is {e}.\n")
            
            if attempt < retires-1:
                print(f"Retrying in 2 Seconds\n")
                time.sleep(2)
            
            else:
                print("All retries Falied !")
                return None

messages=[
    {
        "role":"user",
        "content":"What is api in one line?"
    }
]

reply = chat_with_retry(messages)

if reply:
    print(f"AI:{reply}")
else:
    print("Could not respond")