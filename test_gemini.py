import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: API key not found. Check your .env file.")
else:
    print("API key loaded successfully.")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
       model="gemini-flash-latest",
        contents="Say hello in one short sentence."
    )

    print("Gemini response:")
    print(response.text)
