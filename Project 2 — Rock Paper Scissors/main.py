import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    computer_choice = random.choice(choices)
    user_choice = input("Choose between rock, paper, and scissors: ")

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw")

    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        user_score += 1

    elif user_choice == "rock" and computer_choice == "paper":
        print("You lost!")
        computer_score += 1

    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        user_score += 1

    elif user_choice == "paper" and computer_choice == "scissors":
        print("You lost!")
        computer_score += 1

    elif user_choice == "scissors" and computer_choice == "paper":
            print("You win!")
            user_score += 1

    elif user_choice == "scissors" and computer_choice == "rock":
        print("You lost!")
        computer_score += 1

    else:
        print("Invalid Input!")
        continue

    print(f"Your score: {user_score} | computer's score: {computer_score}")

    if user_score == 3 or computer_score == 3:
        if user_score == 3:
            print("Game ended you won the game!")
        else:
            print("Game ended computer won the game!")
        break