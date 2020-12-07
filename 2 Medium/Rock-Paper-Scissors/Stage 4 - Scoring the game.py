# https://hyperskill.org/projects/78/stages/434/implement

import random
import sys

moves = ["rock", "paper", "scissors"]
win_cond = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

file = open("rating.txt", "r+")
elements = file.read().split()

name = input("Enter your name: ")
print("Hello,", name)

dict = {elements[i]: elements[i+1]
        for i in range(0, len(elements), 2)}

if name not in dict:
    score = dict[name] = "0"
else:
    score = dict.get(name)

while True:

    user_move = input()

    if user_move == "!exit":
        print("Bye!")
        file.close()
        sys.exit()
    elif user_move in moves:
        ai_move = random.choice(moves)
        if user_move == ai_move:
            print(f"There is a draw ({ai_move})")
            score = str(int(score) + 50)
        elif win_cond[user_move] == ai_move:
            print(f"Well done. The computer chose {ai_move} and failed")
            score = str(int(score) + 100)
        else:
            print(f"Sorry, but the computer chose {ai_move}")
    elif user_move == "!rating":
        print(score)
    else:
        print("Invalid input")
