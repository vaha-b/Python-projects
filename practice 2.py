import random
import sys
import numpy as np


def default(user_move):
    # global user_move

    ai_move = ["rock", "paper", "scissors", "lizard", "spock"]
    shapes = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["paper", "spock"],
        "spock": ["rock", "scissors"]
    }

#!exit
    if user_move == "!exit":
        print("Bye!")
        sys.exit()
    elif user_move in shapes:
        ai_move = random.choice(ai_move) if len(list(user))
        if user_move == ai_move:
            print(f"There is a draw ({ai_move})")
        elif ai_move in shapes[user_move]:
            print(f"Well done. The computer chose {ai_move} and failed")
        else:
            print(f"Sorry, but the computer chose {ai_move}")
    else:
        print("Invalid input")


while True:
    user_move = input()

    default(user_move)
