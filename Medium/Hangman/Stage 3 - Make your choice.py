# https://hyperskill.org/projects/69/stages/374/implement

import random

mylist = ['python', 'java', 'kotlin', 'javascript']

b = random.choice(mylist)

a = input("Guess the word. ")
print("You survived!" if a == b else "You are hanged!")
