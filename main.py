
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key= os.getenv("OPENROUTER_API_KEY")

client= OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)
print("AI Career Advisor Assistant: Get ans of all you carre related queries")

inp= input("Enter you skills or career related query:")

response= client.chat.completions.create(
    model="mistralai/mistral-7b-instruct",
    messages=[
        {"role": "system", "content": "You are a helpul career advisor and suggest best advices."},
        {"role": "user","content": inp}
    ],
    max_tokens=300
)
print("\nAI Carrer Advice:\n")
print(response.choices[0].message.content)