
questions = [
    {
        "question": "What is the correct way to create a variable in Python?",
        "options": ["A. x = 5", "B. var x = 5", "C. int x = 5", "D. x := 5"],
        "answer" : "A"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. def", "C. func", "D. create"],
        "answer" : "B"
    },
    {
        "question": "What does len() do in Python?",
        "options": ["A. Deletes an object", "B. Converts to integer", "C. Returns the length", "D. Sorts a list"],
        "answer" : "C"
    },
    {
        "question": "Which data type is used to store True or False?",
        "options": ["A. int", "B. str", "C. float", "D. bool"],
        "answer" : "D"
    },
    {
        "question": "What is the output of 2 ** 3?",
        "options": ["A. 5", "B. 6", "C. 8", "D. 9"],
        "answer" : "C"
    }
]

score = 0
answers = []

for question in questions:
    print(question["question"])

    for option in question["options"]:
        print(option)

    option = input("Enter the answer: ")
    answers.append(option)

    if option.upper() == question["answer"]:
        print(f"Your answer: {option}")
        print("Correct! \U00002705")
        score += 1

    else:
        print("Wrong answer!")

print("Quiz completed!")
print(f"Your score: {score}/5")

for number, answer in enumerate(answers, start=1):
    correct_answer = questions[number - 1]["answer"]

    print(f"Question {number}: Your answer: {answer} | Correct answer: {correct_answer}")