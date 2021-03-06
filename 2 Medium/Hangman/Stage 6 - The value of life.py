# About the project:
# https://hyperskill.org/projects/69

# Stage description
# https://hyperskill.org/projects/69/stages/377/implement

import random

# VARIABLES
lives = 8
words_list = ["python", "java", "kotlin", "javascript"]
word = random.choice(words_list)
hidden_word_list = list("-" * len(word))
input_list = []
# ---------------------------------------------------

# Game logic
print("H A N G M A N")
while lives > 0:
    print()
    print(f"{''.join(hidden_word_list)}")
    user_input = input("Input a letter: ")
    input_list.append(user_input)

    if user_input in word:

        # Check if the letter isn't already discovered
        if user_input in hidden_word_list:
            # if user_input in input_list:
            print("No improvements")
            lives -= 1

        for i in range(len(word)):
            character = word[i]
            if character == user_input:
                hidden_word_list[i] = word[i]

        if "-" not in hidden_word_list:
            print("You guessed the word!\nYou survived!")
            lives = 0
        elif lives == 0:
            print("You lost!")

    elif user_input not in word:
        lives -= 1

        # if user_input in input_list[:-1]:
        #	print("No improvements")
        # else:
        print("That letter doesn't appear in the word")

        if lives == 0:
            print("You lost!")
