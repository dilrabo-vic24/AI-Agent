import json
import os
from google.genai import types


def load_history(filename = "chat_history.json"):
    if not os.path.exists(filename):
        return []
    
    try:
        with open(filename, "r", encoding = "utf-8") as f:
            data = json.load(f)

            history = []
            for item in data:
                history.append(types.Content(
                    role = item["role"],
                    parts = [types.Part(text = item["parts"][0]["text"])]
                ))
            return history
    except Exception as e:
        print(f"Error while loading history")
    
def save_history(chat, filename="chat_history.json"):
    history_data = []
    for message in chat.get_history():
        
        history_data.append({
            "role": message.role,
            "parts": [{"text": message.parts[0].text}]
        })
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(history_data, f, ensure_ascii=False, indent=2)