# About the project:
# https://hyperskill.org/projects/69

# Stage description
# https://hyperskill.org/projects/69/stages/376/implement

import random

# VARIABLES
lives = 8
words_list = ["python", "java", "kotlin", "javascript"]
chosen_word = random.choice(words_list)
hidden_word_list = list("-" * len(chosen_word))
# ---------------------------------------------------

# Game logic
print("H A N G M A N\n")
while lives > 0:
    lives -= 1
    print(f"\n {''.join(hidden_word_list)}")
    user_input = input("Input a letter: ")
    for i, letter in enumerate(chosen_word):
        if letter == user_input:
            hidden_word_list[i] = user_input
else:
    print("\nThanks for playing!")
    print("We'll see how well you did in the next stage")
