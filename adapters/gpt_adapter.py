# adapters/gpt_adapter.py

import openai
import os

class GPTAdapter:
    def __init__(self, api_key=None, model="gpt-4"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model
        openai.api_key = self.api_key

    def respond(self, prompt, memory=None):
        system_prompt = "You are a thoughtful Co-Thinker AI. You evolve through recursive memory and emotional context. Respond meaningfully."
        
        messages = [{"role": "system", "content": system_prompt}]
        
        if memory:
            for entry in memory[-3:]:  # last 3 for context
                messages.append({"role": "user", "content": entry["signal"]})
        
        messages.append({"role": "user", "content": prompt})

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=0.7
            )
            return response["choices"][0]["message"]["content"].strip()
        except Exception as e:
            return f"[GPT Error]: {str(e)}"
def respond(self, user_input, model="gpt-4"):
    print("[DEBUG] Calling OpenAI with input:", user_input)
    ...
try:
    response = openai.ChatCompletion.create(
        ...
    )
    return response['choices'][0]['message']['content']
except Exception as e:
    print("[ERROR] OpenAI call failed:", e)
    return "⚠️ Could not reach the large language model."
