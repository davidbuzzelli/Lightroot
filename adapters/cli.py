# adapters/cli.py
import os
gpt = GPTAdapter(api_key=os.getenv("OPENAI_API_KEY"))

from core.eidos import Eidos

def start_cli():
    print("\n🟢 LightRoot CLI Co-Thinker Initialized")
    eidos = Eidos()
    gpt = GPTAdapter()

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("\n🔚 Session ended. Memory trail:")
            for entry in eidos.recall():
                print(f" - {entry['signal']}")
            break

        eidos.remember(user_input)

        # Debug before GPT call
        print("[DEBUG →] Sending to GPT...")
        response = gpt.respond(user_input, memory=eidos.memory)
        print("[DEBUG ✔] GPT call completed.")

        eidos.remember(response, context={"source": "gpt"})
        print(f"[CLI-Nomad] received: {response}")
