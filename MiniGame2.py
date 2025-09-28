import random

def number_guessing_game():
    # Pick a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = None

    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Loop until the user guesses correctly
    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"✅ Correct! You guessed it in {attempts} attempts.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

# Run the game
number_guessing_game()
