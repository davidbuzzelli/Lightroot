from core.eidos import Eidos
from adapters.gpt_adapter import GPTAdapter

def start_cli():
    print("\n🧠 LightRoot CLI Co-Thinker Initialized\n")
    print("Type 'exit' to end session.\n")

    eidos = Eidos()
    gpt = GPTAdapter()

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("\n👣 Session ended. Memory trail:")
            for entry in eidos.recall():
                print(f" - {entry['signal']}")
            break

        eidos.remember(user_input)

        # Ask GPT and print the response
        response = gpt.respond(user_input)
        eidos.remember(response, context={"source": "gpt"})

        print(f"[CLI-Nomad] received: {response}")

