import string
import random

while True:
    print("\n====== Password Generator ======\n")

    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    number = random.choice(string.digits)
    special = random.choice(string.punctuation)
    
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    length = int(input("Enter password length: "))

    more = [lower, upper, number, special]

    random.shuffle(more)
    result = "".join(more)

    pass_generator = list(result)

    for i in range(length - 4):
        pass_generator.append(random.choice(characters))

    random.shuffle(pass_generator)
    generated_password = "".join(pass_generator)

    print(f"\nGenerated Password: {generated_password}")

    break