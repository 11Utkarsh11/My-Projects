questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type is used to store True or False?",
        "options": ["int", "str", "bool", "float"],
        "answer": "bool"
    },
    {
        "question": "Which method is used to add an item to the end of a list?",
        "options": ["add()", "insert()", "append()", "push()"],
        "answer": "append()"
    },
    {
        "question": "Which symbol is used to start a comment in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    },
    {
        "question": "What does len() return when used with a list?",
        "options": [
            "The last item",
            "The number of items",
            "The largest item",
            "The list's memory size"
        ],
        "answer": "The number of items"
    },
    {
        "question": "Which data structure stores key-value pairs?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "Dictionary"
    },
    {
        "question": "Which operator checks whether a value exists inside a collection?",
        "options": ["has", "in", "exists", "contains"],
        "answer": "in"
    },
    {
        "question": "What does the break statement do inside a loop?",
        "options": [
            "Skips the current iteration",
            "Restarts the loop",
            "Exits the loop",
            "Pauses the program"
        ],
        "answer": "Exits the loop"
    },
    {
        "question": "What does the continue statement do inside a loop?",
        "options": [
            "Exits the loop",
            "Skips to the next iteration",
            "Restarts the program",
            "Stops the function"
        ],
        "answer": "Skips to the next iteration"
    },
    {
        "question": "Which keyword is used to create a class in Python?",
        "options": ["object", "class", "struct", "define"],
        "answer": "class"
    },
    {
        "question": "What is self used for inside a Python class?",
        "options": [
            "It refers to the current object",
            "It creates a new class",
            "It deletes an object",
            "It imports a module"
        ],
        "answer": "It refers to the current object"
    },
    {
        "question": "Which method is automatically called when a new object is created?",
        "options": ["__start__()", "__create__()", "__init__()", "__newclass__()"],
        "answer": "__init__()"
    },
    {
        "question": "What does the not operator do to a Boolean value?",
        "options": [
            "Combines two values",
            "Reverses the Boolean value",
            "Checks membership",
            "Creates a Boolean value"
        ],
        "answer": "Reverses the Boolean value"
    },
    {
        "question": "What will this code print?\n\nx = [10, 20, 30]\nprint(x[1])",
        "options": ["10", "20", "30", "1"],
        "answer": "20"
    },
    {
        "question": "What will this code print?\n\nx = 10\nif x > 5:\n    print(\"Yes\")\nelse:\n    print(\"No\")",
        "options": ["Yes", "No", "10", "Error"],
        "answer": "Yes"
    }
]

def python_quiz(points):
    print("""
================================
          PYTHON QUIZ
================================
""")
    while True:
        choice = input("If you want to start quiz press (y/n) to proceed: ")

        if choice.lower() == "y":
            start_quiz(points)

        elif choice.lower() == "n":
            print("See you later!")
            break

        else:
            print("Invalid input!")
            continue
        
points = 0

def start_quiz(points):
    print("""
================================
          PYTHON QUIZ
================================
""")
    
    for number, question in enumerate(questions, start=1):

        print(f'Question {number}:\n{question["question"]}\n')

        for option_number, option in enumerate(question["options"], start=1):
            print(f"{option_number}. {option}")

        while True:

            try:
                choice = int(input("\nEnter the option number from (1-4): "))

                if choice >= 1 and choice <= 4:
                    break

                else:
                    print("Invalid option! Please enter 1-4.")

            except ValueError:
                print("Please enter a number!")

        selected_option = question["options"][choice - 1]

        if selected_option == question["answer"]:
            print("\nCorrect answer!")
            print("You received 1 point")
            points += 1
            print(f"Total points: {points}\n")
    
        else:
            print("\nYour answer was incorrect!")
            print(f"The correct answer was: {question['answer']}")
            print(f"Your points are : {points}\n")

    print("""
================================
          QUIZ RESULT
================================
""")
    print("The quiz has concluded!")
    print(f"Your total points are: {points}")

python_quiz(points)