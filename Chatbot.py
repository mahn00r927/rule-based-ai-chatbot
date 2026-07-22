print("=" * 50)
print("Welcome to DecodeBot")
print("Type 'bye' to exit the chatbot.")
print("=" * 50)

greetings = ["hi", "hello", "hey", "good morning", "good evening"]
farewells = ["bye", "exit", "quit"]
thanks = ["thanks", "thank you", "thank u"]
help_commands = ["help", "commands"]

while True:
    user_input = input("\nYou: ").strip().lower().replace("?", "")

    if user_input in greetings:
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user_input:
        print("Bot: I am doing well. Thank you for asking.")

    elif "name" in user_input:
        print("Bot: My name is DecodeBot.")

    elif "who are you" in user_input:
        print("Bot: I am a rule-based AI chatbot developed using Python.")

    elif "what can you do" in user_input:
        print("Bot: I can respond to greetings, answer simple questions, and end the conversation.")

    elif user_input in thanks:
        print("Bot: You're welcome.")

    elif user_input in help_commands:
        print("\nAvailable Commands:")
        print("- hi")
        print("- hello")
        print("- how are you")
        print("- what is your name")
        print("- who are you")
        print("- what can you do")
        print("- thanks")
        print("- bye")

    elif user_input in farewells:
        print("Bot: Goodbye. Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")