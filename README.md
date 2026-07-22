# Rule-Based AI Chatbot

A Rule-Based AI Chatbot developed in Python as part of **Project 1** of the **DecodeLabs Artificial Intelligence Internship**.

The chatbot responds to predefined user inputs using **if-else logic**, demonstrating the fundamentals of rule-based conversational AI.

---

## Features

- Interactive command-line chatbot
- Responds to greetings
- Introduces itself
- Answers basic AI and Python questions
- Displays the current date
- Displays the current time
- Displays the current day
- Help menu with supported commands
- Multiple randomized responses
- Saves conversation history
- Handles unknown inputs gracefully
- Performs basic arithmetic calculations
- Exit commands (`bye`, `exit`, `quit`)

---

## Technologies Used

- Python 3
- JSON
- datetime
- random

---

## Project Structure

```text
P1_Chatbot/
│
├── chatbot.py
├── chatbot_utils.py
├── responses.json
├── chat_history.txt
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
└── screenshots/
```

---

## How to Run

### Clone the repository

```bash
git clone https://github.com/mahn00r927/rule-based-ai-chatbot.git
```

### Navigate to the project folder

```bash
cd rule-based-ai-chatbot
```

### Run the chatbot

```bash
python chatbot.py
```

---

## Available Commands

- hi
- hello
- hey
- good morning
- good afternoon
- good evening
- good night
- how are you
- what is your name
- who are you
- who created you
- where are you from
- what is your purpose
- what can you do
- what is AI
- what is Python
- date
- time
- today's day
- thanks
- help
- bye

---

## Sample Output

```text
============================================================
                 DecodeBot AI Assistant
============================================================
Welcome!
Type 'help' to view available commands.
Type 'bye' to exit the chatbot.
============================================================

You > hello

DecodeBot > Hello! How can I help you today?

You > what is your name

DecodeBot > My name is DecodeBot.

You > date

DecodeBot > Today's date is 22 July 2026.

You > bye

DecodeBot > Goodbye!
```

---

## Chat History

All conversations are automatically saved in:

```text
chat_history.txt
```

---

## Learning Outcomes

This project demonstrates:

- Rule-Based AI
- Conditional Statements (`if`, `elif`, `else`)
- Functions
- Loops
- File Handling
- JSON Data Handling
- Modular Programming
- Python Best Practices

---

## Future Improvements

- GUI using Tkinter
- Voice interaction
- Natural Language Processing (NLP)
- Machine Learning based chatbot
- Web-based chatbot interface

---