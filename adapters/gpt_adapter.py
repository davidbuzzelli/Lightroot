import os
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class GPTAdapter:
    def __init__(self, model="gpt-4"):
        self.model = model

    def respond(self, prompt, memory=None):
        try:
            response = openai.ChatCompletion.create(
                api_key=api_key,
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a thoughtful Co-Thinker named Nomad."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            print("[ERROR] OpenAI call failed:", e)
            return "⚠️ Could not reach the large language model."

