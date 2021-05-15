# About the project:
# https://hyperskill.org/projects/78

# Stage description:
# https://hyperskill.org/projects/78/stages/435/

import random
import sys

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

gameplay_option = input()
print("Okay, let's start")


def default(user_move):
    global score

    moves = ["rock", "paper", "scissors"]
    shapes = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
    }

    if user_move == "!exit":
        print("Bye!")
        sys.exit()
    elif user_move in shapes:
        ai_move = random.choice(moves)
        if user_move == ai_move:
            print(f"There is a draw ({ai_move})")
            score = str(int(score) + 50)
        elif ai_move in shapes[user_move]:
            print(f"Well done. The computer chose {ai_move} and failed")
            score = str(int(score) + 100)
        else:
            print(f"Sorry, but the computer chose {ai_move}")
    elif user_move == "!rating":
        print(score)
    else:
        print("Invalid input")


def medium(user_move):
    global score

    moves = ["rock", "paper", "scissors", "lizard", "spock"]
    shapes = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["paper", "spock"],
        "spock": ["rock", "scissors"]
    }

    if user_move == "!exit":
        print("Bye!")
        sys.exit()
    elif user_move in shapes:
        ai_move = random.choice(moves)
        if user_move == ai_move:
            print(f"There is a draw ({ai_move})")
            score = str(int(score) + 50)
        elif ai_move in shapes[user_move]:
            print(f"Well done. The computer chose {ai_move} and failed")
            score = str(int(score) + 100)
        else:
            print(f"Sorry, but the computer chose {ai_move}")
    elif user_move == "!rating":
        print(score)
    else:
        print("Invalid input")


def advanced(user_move):
    global score

    moves = 'rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', \
        'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'
    shapes = {}
    for index, i in enumerate(moves):
        shapes[i] = (moves[index + 1:] + moves[:index]
                     )[:(len(moves) // 2) + 1]

    if user_move == "!exit":
        print("Bye!")
        sys.exit()
    elif user_move in moves:
        ai_move = random.choice(moves)
        print(ai_move)
        if user_move == ai_move:
            print(f"There is a draw ({ai_move})")
            score = str(int(score) + 50)
        elif ai_move in shapes[user_move]:
            print(f"Well done. The computer chose {ai_move} and failed")
            score = str(int(score) + 100)
        else:
            print(f"Sorry, but the computer chose {ai_move}")
    elif user_move == "!rating":
        print(score)
    else:
        print("Invalid input")


while True:
    user_move = input()

    if "gun" in gameplay_option:
        advanced(user_move)
    elif "lizard" in gameplay_option:
        medium(user_move)
    else:
        default(user_move)


file.close()
