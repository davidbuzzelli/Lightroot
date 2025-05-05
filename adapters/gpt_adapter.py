import os
import openai
from dotenv import load_dotenv

load_dotenv()

class GPTAdapter:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def respond(self, message):
        print(f"[DEBUG →] Sending message to OpenAI: {message}")
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": message}],
                temperature=0.7,
            )
            reply = completion.choices[0].message["content"]
            print(f"[DEBUG ←] GPT response: {reply}")
            return reply
        except Exception as e:
            print(f"[ERROR] OpenAI call failed: {e}")
            return "⚠️ Could not reach the large language model."




