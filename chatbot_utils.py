import json
import random
import ast
import operator
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

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}


def evaluate(node):
    if isinstance(node, ast.Constant):
        return node.value

    elif isinstance(node, ast.BinOp):
        left = evaluate(node.left)
        right = evaluate(node.right)

        if isinstance(node.op, ast.Div) and right == 0:
            raise ZeroDivisionError

        operation = OPERATORS[type(node.op)]
        return operation(left, right)

    else:
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
    
    elif "square of" in user_input:
        try:
            number = float(user_input.replace("square of", "").strip())
            return f"Result: {number ** 2:g}"
        except ValueError:
            return "Please enter a valid number."
        
    elif "cube of" in user_input:
        try:
            number = float(user_input.replace("cube of", "").strip())
            return f"Result: {number ** 3:g}"
        except ValueError:
            return "Please enter a valid number."
            
    elif "sqrt" in user_input:
        try:
            number = float(user_input.replace("sqrt", "").strip())

            if number < 0:
                return "Square root of a negative number is not supported."

            return f"Result: {number ** 0.5:g}"

        except ValueError:
            return "Please enter a valid number."

    calculation = calculate(user_input)

    if calculation:
        return calculation

    return responses["unknown"]