import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class GPTAdapter:
    def __init__(self, api_key=None):
        if api_key:
            openai.api_key = api_key

    def respond(self, prompt):
        try:
            print(f"[DEBUG →] Sending prompt to OpenAI: {prompt}")
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or "gpt-4" if available
                messages=[
                    {"role": "system", "content": "You are Nomad, a co-thinker in a CLI environment."},
                    {"role": "user", "content": prompt}
                ]
            )
            reply = response['choices'][0]['message']['content']
            print(f"[DEBUG ←] GPT response: {reply}")
            return reply
        except Exception as e:
            print("[ERROR] OpenAI call failed:", e)
            return "⚠️ Could not reach the large language model."



