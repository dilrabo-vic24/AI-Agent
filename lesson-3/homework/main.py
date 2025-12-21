import os
from dotenv import load_dotenv
from google.genai import Client, types
from tools import db_tool

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
client = Client(api_key=API_KEY)
MODEL_NAME = "gemini-2.5-flash-lite" #name
SYSTEM_PROMPT = """You are a database assistant.
1. Convert the user's question into an SQL query.
2. Call the db_tool function and get the result.
3. Based on the result, provide user with clear and well-written conclusion"""


config = types.GenerateContentConfig(
    tools=[db_tool],
    system_instruction=SYSTEM_PROMPT
)

def run_chat():
    user_input = input("User: ")

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=user_input,
        config=config
    )

    first_part = response.candidates[0].content.parts[0]
    if first_part.function_call:
        fn = first_part.function_call
        print(f"AI: {fn.args['sql_query']}")

        db_result = db_tool(**fn.args)
        final_response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[
                types.Content(role="user", parts=[types.Part.from_text(user_input)]),
                types.Content(role="model", parts=[first_part]),
                types.Content(role="user", parts=[
                    types.Part.from_function_response(
                        name=fn.name,
                        response={'result': db_result}
                    )
                ])
            ],
            config = config
        )
        print("AI:", final_response.text)
    else:
        print("AI:", response.text)


if __name__ == "__main__":
    run_chat()