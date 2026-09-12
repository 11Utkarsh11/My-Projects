import time

sentence = "Python is a powerful programming language"

def typing_test():
    print(f"""
========================================
          TYPING SPEED TEST
========================================

Type the following sentence:

{sentence}
""")
    
    start_time = time.time()

    typed_text = input("Start typing: ")

    end_time = time.time()

    time_taken = end_time - start_time

    # character length
    character_length = len(typed_text.replace(" ", ""))
    # print(f"Character length: {character_length}")

    # Word length
    word_length = len(typed_text.split())
    # print(f"Word length: {word_length}")

    # Typing speed
    time_in_minutes = time_taken / 60
    typing_speed = word_length / time_in_minutes
    # print(f"Your typing speed was: {typing_speed:.2f} WPM")

    # Errors
    error_count = 0

    shorter_length = min(len(typed_text), len(sentence))

    for i in range(shorter_length):
        if typed_text[i] != sentence[i]:
            error_count += 1

    # Count missing or extra characters
    if len(typed_text) < len(sentence):
        error_count += len(sentence) - len(typed_text)

    elif len(typed_text) > len(sentence):
        error_count += len(typed_text) - len(sentence)

    # Accuracy
    correct_characters = len(sentence) - error_count
    if correct_characters >= 0:
        # print(f"Number of errors: {error_count}")
        accuracy = ((correct_characters / len(sentence)) * 100)

    else:
        accuracy = 0

    # Result
    print(f"""
========================================
             YOUR RESULT
========================================

Time taken: {time_taken:.2f} seconds
Characters typed: {character_length}
Words typed: {word_length}

Typing speed: {typing_speed:.2f}
Accuracy: {accuracy:.2f}%

Good job!
""")

typing_test()