# About the project:
# https://hyperskill.org/projects/69

# Stage description
# https://hyperskill.org/projects/69/stages/378/implement

import random
from string import ascii_lowercase as lowercase_letters

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

    if len(user_input) >= 2:
        print("You should input a single letter")
        #lives += 1
        continue
    elif user_input not in lowercase_letters:
        print("Please enter a lowercase English letter")
        #lives += 1
        continue

    input_list.append(user_input)

    if user_input in word:

        # Check if the letter isn't already discovered
        if user_input in hidden_word_list:
            if user_input in input_list:
                print("You've already guessed this letter")
                #lives -= 1

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

        if user_input in input_list[:-1]:
            print("You've already guessed this letter")
        else:
            print("That letter doesn't appear in the word")
            lives -= 1

        if lives == 0:
            print("You lost!")
