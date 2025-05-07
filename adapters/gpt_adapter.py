import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

class GPTAdapter:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file. Please create a .env file with your OpenAI API key.")
        self.client = openai.OpenAI(api_key=api_key)

    def respond(self, messages: list):
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.85,
            top_p=0.95
        )
        return response.choices[0].message.content

def get_gpt_adapter():
    return GPTAdapter()











