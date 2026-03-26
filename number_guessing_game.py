# User is asked to guess a number between 1 and 100. The program generates a random number and gives feedback on whether the guess is too low,
# too high, or correct. The game continues until the user guesses the correct number.
import random

number_to_guess = random.randint(1, 100)
guess = None

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

while guess != number_to_guess:
    try:
        guess = int(input("Enter your guess: "))
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(
                f"Congratulations! You've guessed the number {number_to_guess} correctly!")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")

