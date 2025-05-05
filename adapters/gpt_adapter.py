import os
import openai
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Debug: Confirm key load
if not api_key:
    print("[DEBUG ❌] OPENAI_API_KEY not found in .env")
else:
    print("[DEBUG ✅] OPENAI_API_KEY loaded successfully")

# Set OpenAI key
openai.api_key = api_key

class GPTAdapter:
    def __init__(self, model="gpt-4"):
        self.model = model

    def respond(self, prompt, memory=None):
        print(f"[DEBUG →] Sending prompt: {prompt}")
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are Nomad, a helpful Co-Thinker who helps users explore ideas."},
                    {"role": "user", "content": prompt}
                ]
            )
            reply = response["choices"][0]["message"]["content"]
            print(f"[DEBUG ←] GPT response: {reply}")
            return reply

        except Exception as e:
            print(f"[ERROR 🚨] OpenAI call failed: {e}")
            return "⚠️ Could not connect to the GPT model."


