import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("[DEBUG] ❌ OPENAI_API_KEY not loaded from .env")
else:
    print("[DEBUG] ✅ OPENAI_API_KEY loaded")

class GPTAdapter:
    def __init__(self, model="gpt-4"):
        self.model = model

    def respond(self, prompt, memory=None):
        try:
            print(f"[DEBUG] Sending prompt to OpenAI: {prompt}")
            response = openai.ChatCompletion.create(
                api_key=api_key,
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a thoughtful Co-Thinker named Nomad."},
                    {"role": "user", "content": prompt}
                ]
            )
            reply = response['choices'][0]['message']['content']
            print(f"[DEBUG] Received response: {reply}")
            return reply
        except Exception as e:
            print("[ERROR] OpenAI call failed:", e)
            return "⚠️ Could not reach the large language model."


