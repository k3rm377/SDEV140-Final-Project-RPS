# Program name: Rock Paper Scissors Game
# Author: Kira Emmett Buck
# Date: 4/22/2022
# Summary: User plays a basic game of rock, paper, scissors
# Variables:
#   user_action: The user's action choice
#   possible_actions: action chosen between rock, paper, or scissors
#   computer_action: the random action chosen by the program
#   play_again: Option to play the game again

import random

while True:
    user_action = input("Enter a choice between rock, paper, or scissors: ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
    else:
        print("Thanks for playing!")
