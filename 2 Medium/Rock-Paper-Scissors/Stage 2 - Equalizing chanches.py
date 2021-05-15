# About the project:
# https://hyperskill.org/projects/78

# Stage description:
# https://hyperskill.org/projects/78/stages/432/implement


# I made two solutions

from random import choice

win_conditions = {"paper": "rock",
                  "scissors": "paper",
                  "rock": "scissors"
                  }

player = input()
computer = choice(list(win_conditions.keys()))

# First solution using dictionaries

if win_conditions[player] == computer:
    print(f"Well done. The computer chose {computer} and failed")
elif win_conditions[player] != computer:
    print(f"Sorry, but the computer chose {computer}")
else:
    print(f"There is a draw {computer}")

# Second solution using if elif statements
# if player == computer:
#     print(f"There is a draw {computer}")
# elif player == "paper" and computer == "rock":
#     print(f"Well done. The computer chose {computer} and failed")
# elif player == "rock" and computer == "paper":
#     print(f"Sorry, but the computer chose {computer}")
# elif player == "scissors" and computer == "paper":
#     print(f"Well done. The computer chose {computer} and failed")
# elif player == "paper" and computer == "scissors":
#     print(f"Sorry, but the computer chose {computer}")
# elif player == "rock" and computer == "scissors":
#     print(f"Well done. The computer chose {computer} and failed")
# elif player == "scissors" and computer == "rock":
#     print(f"Sorry, but the computer chose {computer}")
