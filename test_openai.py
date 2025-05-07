import os
from dotenv import load_dotenv
import openai

print("🔍 Loading .env...")
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print("✅ API KEY:", "Loaded" if api_key else "MISSING")

if not api_key:
    print("❌ OPENAI_API_KEY not loaded.")
    exit()

openai.api_key = api_key

print("🚀 Sending test prompt to OpenAI...")

try:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say hello from LightRoot"}]
    )
    print("✅ GPT Response:")
    print(completion['choices'][0]['message']['content'])
except Exception as e:
    print("❌ OpenAI call failed:", e)
