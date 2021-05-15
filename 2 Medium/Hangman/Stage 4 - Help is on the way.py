# About the project:
# https://hyperskill.org/projects/69

# Stage description
# https://hyperskill.org/projects/69/stages/375/implement

import random

# Write your code here
print('H A N G M A N')
words = ['python', 'java', 'kotlin', 'javascript']

word = words[random.randint(0, 3)]
word_hidden = word[:3] + ('-' * (len(word) - 3))
print('You survived!' if input('Guess the word ' +
                               word_hidden + ': > ') == word else 'You lost!')
