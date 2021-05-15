# About the project:
# https://hyperskill.org/projects/78

# Stage description:
# https://hyperskill.org/projects/78/stages/433/implement

import random
import sys

while True:
    moves = ["rock", "paper", "scissors"]
    win_cond = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    user_move = input()
    if user_move == "!exit":
        print("Bye!")
        sys.exit()
    elif user_move in moves:
        ai_move = random.choice(moves)
        if user_move == ai_move:
            print(f"There is a draw ({ai_move})")
        elif win_cond[user_move] == ai_move:
            print(f"Well done. The computer chose {ai_move} and failed")
        else:
            print(f"Sorry, but the computer chose {ai_move}")
    else:
        print("Invalid input")
