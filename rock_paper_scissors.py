# Steps:
# Ask user to enter a choice
# If choice is not valid, display proper error message
# If valid choice, let the computer make a choice.
# Print the choices
# Determine the winner
# Ask the user if they want to continue

import random

choices=('r','p','s') # using a tuple so that it is read only and it is not accidentally modified
emojis = {'r':'🪨', 'p':'📄', 's':'✂️'}
while True:
    user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
    if user_choice in choices:
        computer_choice = random.choice(choices)
        print(f"You chose {emojis[user_choice]}")
        print(f"Computer chose {emojis[computer_choice]}")
        if (user_choice, computer_choice) in [('r','s'), ('p','r'), ('s','p')]:
            print("You won")
        elif (user_choice, computer_choice) in [('r','p'), ('p','s'), ('s','r')]:
            print("You lose")
        elif user_choice == computer_choice:
            print("It is a draw")
    else:
        print("Invalid choice!")

    is_continue = input("Continue? (y/n): ").lower()
    if not is_continue == "n" and not is_continue == "y":
        print("Invalid choice!")
        break
    elif is_continue == "n":
        break
    

    

