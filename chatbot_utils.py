import ast
import json
import operator
import random
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "responses.json", "r", encoding="utf-8") as file:
    responses = json.load(file)


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}


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
    with open(BASE_DIR / "chat_history.txt", "a", encoding="utf-8") as file:
        file.write(f"You: {user}\n")
        file.write(f"Bot: {bot}\n")
        file.write("-" * 50 + "\n")


def evaluate(node):
    if isinstance(node, ast.Constant):
        return node.value

    if isinstance(node, ast.BinOp):
        left = evaluate(node.left)
        right = evaluate(node.right)

        if isinstance(node.op, ast.Div) and right == 0:
            raise ZeroDivisionError

        return OPERATORS[type(node.op)](left, right)

    raise TypeError


def calculate(expression):
    try:
        tree = ast.parse(expression, mode="eval")
        result = evaluate(tree.body)

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        return f"Result: {result}"

    except ZeroDivisionError:
        return "Cannot divide by zero."

    except Exception:
        return None


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
        "hy",
        "good morning",
        "good afternoon",
        "good evening",
        "good night"
    ]

    if user_input in greetings:
        return random.choice(responses["greetings"]), "greeting"

    elif user_input in ["how are you", "how are you doing"]:
        return "I am doing well. Thank you for asking.", "general"

    elif user_input in [
        "what is your name",
        "your name",
        "name"
    ]:
        return responses["name"], "general"

    elif user_input == "who are you":
        return responses["identity"], "general"

    elif user_input in [
        "who created you",
        "who made you"
    ]:
        return responses["creator"], "general"

    elif user_input == "where are you from":
        return responses["origin"], "general"

    elif user_input == "what is your purpose":
        return responses["purpose"], "general"

    elif user_input == "what can you do":
        return responses["skills"], "general"

    elif user_input in [
        "what is ai",
        "what is artificial intelligence"
    ]:
        return responses["ai"], "general"

    elif user_input == "what is python":
        return responses["python"], "general"

    elif user_input == "date":
        today = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {today}.", "general"

    elif user_input == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}.", "general"

    elif user_input in [
        "day",
        "today",
        "today's day",
        "what day is today"
    ]:
        today = datetime.now().strftime("%A")
        return f"Today is {today}.", "general"

    elif user_input.startswith("square of"):
        try:
            number = float(
                user_input.replace("square of", "").strip()
            )
            return f"Result: {number ** 2:g}", "calculation"

        except ValueError:
            return "Please enter a valid number.", "general"

    elif user_input.startswith("cube of"):
        try:
            number = float(
                user_input.replace("cube of", "").strip()
            )
            return f"Result: {number ** 3:g}", "calculation"

        except ValueError:
            return "Please enter a valid number.", "general"

    elif user_input.startswith("sqrt"):
        try:
            number = float(
                user_input.replace("sqrt", "").strip()
            )

            if number < 0:
                return (
                    "Square root of a negative number is not supported.",
                    "general"
                )

            return f"Result: {number ** 0.5:g}", "calculation"

        except ValueError:
            return "Please enter a valid number.", "general"

    elif user_input in [
        "thanks",
        "thank you",
        "thank u"
    ]:
        return random.choice(responses["thanks"]), "general"

    elif user_input == "help":
        show_help()
        return None, None

    elif user_input in [
        "bye",
        "exit",
        "quit"
    ]:
        return random.choice(responses["farewells"]), "general"

    calculation = calculate(user_input)

    if calculation:
        return calculation, "calculation"

    return responses["unknown"], "general"


def show_summary(stats, start_time):

    end_time = datetime.now()

    duration = end_time - start_time

    print("\n" + "=" * 60)
    print("Session Summary")
    print("=" * 60)
    print(f"Messages        : {stats['messages']}")
    print(f"Greetings       : {stats['greetings']}")
    print(f"Calculations    : {stats['calculations']}")
    print(f"Started At      : {start_time.strftime('%I:%M:%S %p')}")
    print(f"Ended At        : {end_time.strftime('%I:%M:%S %p')}")
    print(f"Duration        : {duration}")
    print("=" * 60)