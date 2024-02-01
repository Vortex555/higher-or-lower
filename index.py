import random

def higher_lower_game():
    target_number = random.randint(1, 100)
    attempts = 0

    while attempts < 7:
        guess = input("Guess a number between 1 and 100 | You get 7 attempts! (or type 'quit' to exit): ")
        
        if guess.lower() == "quit":
            print(f"The number was {target_number}! Thanks for playing!")
            return
        
        guess = int(guess)
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
    
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() == "y":
        higher_lower_game()
    else:
        print("Thanks for playing!")
        return
        


higher_lower_game()