from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages = [
    {
        "role" : "system",
        "content" : "You are a helpful AI chatbot. Keep your answers concise and to the point."
    }
]

while True:
    user_input = input("You: ")
    if user_input.lower() =="bye":
        print("Bot: Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model ="llama-3.3-70b-versatile",
        messages=messages
    )

    bot_reply = response.choices[0].message.content
    print("Bot: "+bot_reply)

    messages.append({
        "role": "assistant",
        "content": bot_reply
    })