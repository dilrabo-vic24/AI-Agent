import os
from dotenv import load_dotenv
from google import genai
import chatbot_history as h

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


client = genai.Client(api_key=api_key)

saved_history = h.load_history()

chat = client.chats.create(
    model="gemini-2.5-flash",
    history=saved_history
)

print("Chatting ........................")

while True:
    user = input("User: ")

    if user.lower() in ["exit", "quit", "stop"]:
        break

    print("AI: ", end=" ")

    response = chat.send_message_stream(user)

    full_response_test = ""
    for item in response:
        print(item.text, end="")
        full_response_test += item.text

    print()

    h.save_history(chat)