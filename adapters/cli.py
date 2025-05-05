from core.eidos import Eidos
from adapters.gpt_adapter import GPTAdapter

def start_cli():
    print("\n🌱 LightRoot CLI Co-Thinker Initialized")
    print("Type 'exit' to end session.\n")

    eidos = Eidos()
    gpt = GPTAdapter()

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("\n🧠 Session ended. Memory trail:")
            for entry in eidos.recall():
                print(f"- {entry['signal']}")
            break

        # Save input to memory
        eidos.remember(user_input)

        # DEBUG: Confirm GPTAdapter is being used
        print("[DEBUG] Calling GPTAdapter.respond()...")

        # Get GPT response
        response = gpt.respond(user_input)

        # Save response
        eidos.remember(response, context={"source": "gpt"})

        # Print response
        print(f"[CLI-Nomad] received: {response}")

