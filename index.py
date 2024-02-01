import random

def higher_lower_game():
    target_number = random.randint(1, 100)
    attempts = 0

    while attempts < 10:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < target_number:
            print("Higher!")
        elif guess > target_number:
            print("Lower!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    if attempts == 10:
        print(f"Game over! The number was {target_number}.")


higher_lower_game()