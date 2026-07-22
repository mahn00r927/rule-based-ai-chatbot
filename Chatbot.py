from chatbot_utils import (
    display_welcome,
    get_response,
    save_chat
)


def main():
    display_welcome()

    while True:

        user_input = input("\nYou > ")

        response = get_response(user_input)

        if response:
            print(f"\nDecodeBot > {response}")
            save_chat(user_input, response)

        if user_input.strip().lower() in ["bye", "exit", "quit"]:
            break
        

if __name__ == "__main__":
    main()