import os
import openai

class GPTAdapter:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def respond(self, prompt):
        try:
            print(f"[DEBUG →] Sending message to OpenAI: {prompt}")
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            reply = completion['choices'][0]['message']['content']
            print(f"[DEBUG ←] GPT response: {reply}")
            return reply
        except Exception as e:
            print(f"[ERROR] OpenAI call failed: {e}")
            return "⚠️ Could not reach the large language model."




