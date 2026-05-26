import os
import time
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

HISTORY_FILE="history.json"
system_prompt={
    "role": "system",
    "content": """You are an expert study assistant named HMN. 
    You help students understand any topic clearly.
    Always explain Simply first, then deeply.
    Use real world analogies.
    End every explanation with 3 quiz questions."""
}

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE,"r") as f:
           print("History loaded from history")
           return json.load(f)
    else:
        print("Starting fresh conversation !!")
        return [system_prompt]

def save_history(messages):
    with open(HISTORY_FILE,"w") as f:
        json.dump(messages,f,indent=2)

def chat(messages,retries=3):
    for attempts in range(retries):
        try:
            stream = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                stream=True
            )
            print(f"HMN:",end="",flush=True)
            full_reply=""
            for chunck in stream:
                if chunck.choices[0].delta.content:
                    text=chunck.choices[0].delta.content
                    print(text,end="",flush=True)
                    full_reply+=text
            print("\n")
            return full_reply
        except Exception as e:
            print(f"Attempt {attempts+1} failed {e}")
            if attempts<retries-1:
                print("Retrying in 2 seconds")
                time.sleep(2)
            else:
                print("All retries are failed")
                return None

def main():
    print("="*40)
    print("HMN-Your Study Assistant")
    print("="*40)
    print("Type 'quit' to exit | 'clear' to reset\n")

    messages=load_history()

    while True:
        user_input=input("You:").strip()

        if not user_input:
            continue
        if user_input.lower()=="quit":
            save_history(messages)
            print("Conversation saved ! Goodbye !!")
            break

        if user_input.lower()=="clear":
            messages=[system_prompt]
            save_history(messages)
            print("History cleared Successfully !!")
            continue

        messages.append(
            {
                "role":"user",
                "content":user_input
            }
        )
        reply = chat(messages)
        if reply:
            messages.append(
                {
                "role":"assistant",
                "content":reply
                }
            )
            save_history(messages)

main()