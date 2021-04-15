# About the project:
# https://hyperskill.org/projects/74

# Stage description
# https://hyperskill.org/projects/74/stages/410/implement


while True:
    value = input()
    try:
        x, y = value.split()
        print(int(x) + int(y))
    except:
        try:
            print(int(value))
        except:
            if value == "/exit":
                print("Bye!")
                break
            else:
                continue
