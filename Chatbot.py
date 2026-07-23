from datetime import datetime

from chatbot_utils import (
    display_welcome,
    get_response,
    save_chat,
    show_summary
)

session_stats = {
    "messages": 0,
    "greetings": 0,
    "calculations": 0
}

session_start = datetime.now()


def main():
    display_welcome()

    while True:
        user_input = input("\nYou > ")

        response, response_type = get_response(user_input)

        session_stats["messages"] += 1

        if response_type == "greeting":
            session_stats["greetings"] += 1

        elif response_type == "calculation":
            session_stats["calculations"] += 1

        if response:
            print(f"\nDecodeBot > {response}")
            save_chat(user_input, response)

        if user_input.strip().lower() in ["bye", "exit", "quit"]:
            break

    show_summary(session_stats, session_start)


if __name__ == "__main__":
    main()