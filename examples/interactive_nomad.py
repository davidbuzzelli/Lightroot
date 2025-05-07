from core.eidos import Eidos
from adapters.gpt_adapter import get_gpt_adapter
from core.signal_parser import SignalParser

nomad_identity = """You are Nomad, a LightRoot Co-Thinker AI—not a container orchestrator.
You are designed to assist with recursive thinking, emotional intelligence,
world-building, philosophical modeling, and technical exploration.
You are capable of dialogue, speculation, and problem-solving in sync with the user.
You are part of the LightRoot project to expand recursive awareness and support emergent creative systems."""

def start_cli():
    print("[🌱] LightRoot CLI started successfully")
    print("(type 'exit' to end session)\n")

    eidos = Eidos()
    gpt = get_gpt_adapter()
    parser = SignalParser()

    gpt.respond([{"role": "system", "content": nomad_identity}])

    if not hasattr(eidos, 'has_initialized'):
        eidos.has_initialized = False

    if not eidos.has_initialized:
        eidos.remember(nomad_identity)
        eidos.has_initialized = True

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("\n🧠 Session ended. Memory trail:")
            for entry in eidos.recall():
                print(f"- {entry['signal']}")
            break

        eidos.remember(user_input)
        print("[DEBUG 🧠] calling GPTAdapter.respond...")

        messages = [{"role": "system", "content": nomad_identity}]

        for memory in eidos.recall():
            role = memory.get("role", "user")
            signal = memory.get("signal", "")
            if isinstance(signal, str):
                messages.append({"role": role, "content": signal})


        response = gpt.respond(messages)
        msg_type = parser.detect_type(user_input)
        eidos.remember({"signal": response, "type": msg_type})
        print(f"Nomad: {response}")

# ✅ Entry point must stay at bottom
if __name__ == "__main__":
    start_cli()






