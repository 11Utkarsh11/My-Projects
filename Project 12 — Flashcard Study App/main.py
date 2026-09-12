import random

flashcards = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "How many continents are there?": "7",
    "What is the chemical symbol for water?": "H2O",
    "Who wrote Romeo and Juliet?": "William Shakespeare",
    "What is the fastest land animal?": "Cheetah",
    "How many days are there in a leap year?": "366",
    "What is the largest ocean on Earth?": "Pacific Ocean",
    "What is the boiling point of water in Celsius?": "100",
    "Which planet is known as the Red Planet?": "Mars",
    "How many sides does a hexagon have?": "6",
    "What is the currency of Japan?": "Yen",
    "What gas do humans need to breathe?": "Oxygen",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the smallest prime number?": "2",
    "How many players are there on a football team on the field?": "11",
    "What is the largest mammal in the world?": "Blue Whale",
    "Which programming language are we currently learning?": "Python",
    "What does CPU stand for?": "Central Processing Unit",
    "How many bytes are in a kilobyte?": "1024"
}

def main():
    while True:
        print(f"""
==================================================
               🧠 FLASHCARD APP
==================================================

                  MAIN MENU

            1. Start Quiz
            2. View Flashcards
            3. Add Flashcard
            4. Exit

--------------------------------------------------
            Flashcards Available: {len(flashcards)}
--------------------------------------------------
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            start_quiz()

        elif choice == "2":
            view_flashcards()

        elif choice == "3":
            add_flashcard()

        elif choice == "4":
            print("You've quitted from program!\n")
            quit()

        else:
            print("Invalid input: ")

def start_quiz():
    print(f"""
==================================================
                  START QUIZ
==================================================

How many questions would you like?
(Available: {len(flashcards)})
""")

    while True:
        try:
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(flashcards):
                break
            print(f"❌ You can choose between 1 and {len(flashcards)}.")

        except ValueError:
            print("❌ Please enter only integers.")

    correct_answer = 0
    incorrect_answer = 0
    count = 0

    questions = list(flashcards.keys())
    random.shuffle(questions)

    for question in questions:
        if count >= choice:
            break
        count += 1

        print(f"""
==================================================
                 QUESTION {count}/{choice}
==================================================
""")
        print(f"{count}. {question}\n")

        user_input = input("Your answer: ")

        if user_input.lower().strip() == flashcards[question].lower().strip():
            print("\n✓ Correct!")
            correct_answer += 1
            print(f"Score {count}/{choice}\n")
            continue

        else:
            print(f"Incorrect!, the correct anser is {flashcards[question]}")
            incorrect_answer += 1
            continue

    score = (((correct_answer)/ (choice)) *100)

    print(f"""
==================================================
                    RESULTS
==================================================

              QUIZ COMPLETED!

Questions:       {choice}
Correct:         {correct_answer}
Incorrect:       {incorrect_answer}
Score:           {score}%

        Great job! 🎉

==================================================

1. Take another quiz
2. Main menu
3. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        start_quiz()

    elif choice == "2":
        main()

    elif choice == "3":
        quit()

    else:
        print("Invalid input")


def view_flashcards():
    len_line = 0
    print("""
==================================================
                ALL FLASHCARDS
==================================================
""")
    for questions, answers in flashcards.items():
        len_line += 1
        print(f"{len_line}. {questions}")
        print(f"    -> {answers}\n")

def add_flashcard():
    print("""
==================================================
                 ADD FLASHCARD
==================================================
""")
    enter_ques = input("Enter question: \n")
    enter_ans = input("Enter answer: \n")

    if enter_ques in flashcards:
        print("⚠️ This question already exists!")
        return
            
    flashcards[enter_ques] = enter_ans
    print("✓ Flashcard added!")
    
main()