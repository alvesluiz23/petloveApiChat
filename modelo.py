from google import genai
import os



def generate_answer(question:str) -> str:
    client = genai.Client(api_key=os.environ["api_germini_key"])

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question,
    )

    return response.text