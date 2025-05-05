# adapters/cli.py

from nomad.base_nomad import Nomad

def start_cli():
    print("🌱 LightRoot CLI Co-Thinker Initialized")
    print("Type 'exit' to end session.\n")

    agent = Nomad(identity="CLI-Nomad")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = agent.engage(user_input)
        print(response)

    print("\n🌀 Session ended. Memory trail:")
    for m in agent.get_history():
        print(f" - {m['signal']}")

if __name__ == "__main__":
    start_cli()
