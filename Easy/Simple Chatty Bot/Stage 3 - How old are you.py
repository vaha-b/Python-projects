# https://hyperskill.org/projects/97/stages/536/implement

print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders

remainder3, remainder5, remainder7 = int(input()), int(input()), int(input())

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print("Your age is", age, "; that's a good time to start programming!")
