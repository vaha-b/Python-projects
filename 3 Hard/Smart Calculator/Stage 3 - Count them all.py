# About the project:
# https://hyperskill.org/projects/74

# Stage description
# https://hyperskill.org/projects/74/stages/411/implement

while True:
    numbers = input().split()
    if '/exit' in numbers:
        print('Bye!')
        break
    elif "/help" in numbers:
        print("The program calculates the sum of numbers")
    elif not numbers:
        pass
    else:
        numbers = [int(x) for x in numbers]
        print(sum(numbers))
