import os
import openai

class GPTAdapter:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def respond(self, prompt):
        print(f"[DEBUG →] Sending message to OpenAI: {prompt}")
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            reply = completion['choices'][0]['message']['content']
            print(f"[DEBUG ←] GPT response: {reply}")
            return reply
        except Exception as e:
            print("[ERROR] OpenAI call failed:", e)
            return "⚠️ Could not reach the large language model."



