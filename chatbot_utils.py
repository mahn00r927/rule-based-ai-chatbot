import json
import random
from datetime import datetime

with open("responses.json", "r") as file:
    responses = json.load(file)


def display_welcome():
    print("\n" + "=" * 60)
    print("                 DecodeBot AI Assistant")
    print("=" * 60)
    print("Welcome!")
    print("Type 'help' to view available commands.")
    print("Type 'bye' to exit the chatbot.")
    print("=" * 60)


def show_help():
    print("\n" + "-" * 45)
    print("Available Commands")
    print("-" * 45)

    for command in responses["help"]:
        print(f"• {command}")

    print("-" * 45)


def save_chat(user, bot):
    with open("chat_history.txt", "a") as file:
        file.write(f"You: {user}\n")
        file.write(f"Bot: {bot}\n")
        file.write("-" * 40 + "\n")


def get_response(user_input):

    user_input = (
        user_input
        .strip()
        .lower()
        .replace("?", "")
        .replace(".", "")
    )

    greetings = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
        "good night"
    ]

    if user_input in greetings:
        return random.choice(responses["greetings"])

    elif "how are you" in user_input:
        return "I am doing well. Thank you for asking."

    elif "name" in user_input:
        return responses["name"]

    elif "who are you" in user_input:
        return responses["identity"]

    elif "who created you" in user_input or "who made you" in user_input:
        return responses["creator"]

    elif "where are you from" in user_input:
        return responses["origin"]

    elif "purpose" in user_input:
        return responses["purpose"]

    elif "what can you do" in user_input:
        return responses["skills"]

    elif "artificial intelligence" in user_input or user_input == "what is ai":
        return responses["ai"]

    elif "python" in user_input:
        return responses["python"]

    elif "date" in user_input:
        today = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {today}."

    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif "day" in user_input:
        day = datetime.now().strftime("%A")
        return f"Today is {day}."

    elif user_input in ["thanks", "thank you", "thank u"]:
        return random.choice(responses["thanks"])

    elif "help" in user_input:
        show_help()
        return None

    elif user_input in ["bye", "exit", "quit"]:
        return random.choice(responses["farewells"])

    return responses["unknown"]