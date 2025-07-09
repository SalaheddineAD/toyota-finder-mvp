import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.images.generate(
        model="dall-e-3",
        prompt="A red Toyota Supra parked near the beach",
        n=1,
        size="1024x1024"
    )
    print("Image URL:", response.data[0].url)
except Exception as e:
    print("Image generation failed:", e)