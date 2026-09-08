from src.agent import run_agent


def main():
    print("=" * 60)
    print("AI IT HELPDESK AGENT")
    print("=" * 60)
    print("Type an IT problem and press Enter.")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        if not question:
            continue

        print("\nAgent:")
        answer = run_agent(question)
        print(answer)
        print()


if __name__ == "__main__":
    main()