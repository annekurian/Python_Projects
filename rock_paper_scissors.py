# Steps:
# Ask user to enter a choice
# If choice is not valid, display proper error message
# If valid choice, let the computer make a choice.
# Print the choices
# Determine the winner
# Ask the user if they want to continue

import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = {ROCK:'🪨', PAPER:'📄', SCISSORS:'✂️'}
# using a tuple so that it is read only and it is not accidentally modified
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")

def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It is a draw")
    elif (user_choice, computer_choice) in [(ROCK,SCISSORS), (PAPER,ROCK), (SCISSORS,PAPER)]:
        print("You won")
    else:
        print("You lose")

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)
        
        determine_winner(user_choice, computer_choice)

        is_continue = input("Continue? (y/n): ").lower()
        if is_continue not in ('y','n'):
            print("Invalid choice!")
            break
        elif is_continue == "n":
            break
    
play_game()