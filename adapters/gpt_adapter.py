import os
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print(f"[DEBUG] Loaded API Key: {api_key[:5]}...")  # Show first few chars to confirm load

openai.api_key = api_key

class GPTAdapter:
    def __init__(self, api_key=None):
        if api_key:
            openai.api_key = api_key

    def respond(self, prompt):
        try:
            print(f"[DEBUG →] Prompt to GPT: {prompt}")
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or "gpt-4" if available to your account
                messages=[
                    {"role": "system", "content": "You are Nomad, a Co-Thinking AI in a CLI."},
                    {"role": "user", "content": prompt}
                ]
            )
            reply = response['choices'][0]['message']['content']
            print(f"[DEBUG ←] GPT responded: {reply}")
            return reply
        except Exception as e:
            print(f"[ERROR] GPT call failed: {e}")
            return "⚠️ Could not contact GPT model."




