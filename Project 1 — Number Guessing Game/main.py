import random

# This is where python will chose a random number
secret_number = random.randint(1, 100)

# print(secret_number)

i = 0
while True:
    number = int(input("Enter a number here: "))

    if number > 100:
        print("Enter a positive integer value between 1 and 100")

    elif number < 1:
        print("Enter a positive integer value above 0")

    else:
        i += 1

        if number > secret_number:
            print("Too High!")

        elif number < secret_number:
            print("Too Low!")
            
        else:
            print("You got it!")
            break

        print(f"Number of attempts are {i}")