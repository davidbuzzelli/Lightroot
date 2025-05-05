from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class GPTAdapter:
    def respond(self, prompt):
        try:
            print(f"[DEBUG →] Sending message to OpenAI: {prompt}")
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="gpt-3.5-turbo"
            )
            reply = response.choices[0].message.content
            print(f"[DEBUG ←] GPT response: {reply}")
            return reply
        except Exception as e:
            print(f"[ERROR] OpenAI call failed: {e}")
            return "Sorry, I couldn't reach the AI."
