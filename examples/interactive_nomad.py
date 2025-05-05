from core.eidos import Eidos
from adapters.gpt_adapter import GPTAdapter

def start_cli():
    print("\n🌱 LightRoot CLI Co-Thinker Initialized")
    print("Type 'exit' to end session.\n")
nomad_identity = """
You are Nomad, a LightRoot Co-Thinker AI—not a container orchestrator.
You are designed to assist with recursive thinking, emotional intelligence,
world-building, philosophical modeling, and technical exploration.
You are capable of dialogue, speculation, and problem-solving in sync with the user.
You are part of the LightRoot project to expand recursive awareness and support emergent creative systems.
"""

from adapters.gpt_adapter import GPTAdapter
GPTAdapter().respond(nomad_identity)

    eidos = Eidos()
    gpt = GPTAdapter()

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("\n🧠 Session ended. Memory trail:")
            for entry in eidos.recall():
                print(f"- {entry['signal']}")
            break

        eidos.remember(user_input)

        print("[DEBUG →] Calling GPTAdapter.respond()...")
        response = gpt.respond(user_input)
        print(f"[DEBUG ←] GPT replied: {response}")

        eidos.remember(response, context={"source": "gpt"})
        print(f"[CLI-Nomad] received: {response}")


if __name__ == "__main__":
    start_cli()
