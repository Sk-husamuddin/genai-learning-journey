import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages=[
    {
        "role":"assistant",
        "content":"You are a helpful GENAI tutor"
    }
]
print("Chat Started !!\n")
print("Type 'quit' to exit\n")
while True:

    user_input=input("You:")

    if user_input.lower() == "quit":
        print("\nGoodbye !!\n")
        break

    messages.append(
        {
            "role":"user",
            "content":user_input
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
    print(f"\nAi:{reply}\n")
