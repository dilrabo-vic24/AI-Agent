import os
from dotenv import load_dotenv
from google.genai import Client

load_dotenv()
client = Client(api_key=os.getenv("GOOGLE_API_KEY"))

try:
    for model in client.models.list():
        if 'generateContent' in model.supported_actions:
            print(f" - {model.name}")
except Exception as e:
    print(f"error: {e}")