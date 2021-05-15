# About the project
# https://hyperskill.org/projects/73

# Stage description
# https://hyperskill.org/projects/73/stages/402/implement

a = input("Enter cells:")


def out():
    print('---------')
    print('|', a[0], a[1], a[2], '|')
    print('|', a[3], a[4], a[5], '|')
    print('|', a[6], a[7], a[8], '|')
    print('---------')


out()

flag = 1
while flag:
    b = input("Enter the coordinates:")
    c = int(b[0])
    d = int(b[2])
    array = [[a[0], a[1], a[2]], [a[3], a[4], a[5]], [a[6], a[7], a[8]]]

    if c not in range(1, 4) or d not in range(1, 4):
        print("Coordinates should be from 1 to 3!")
        continue
    coord = array[3 - d][c - 1]
    if coord == "X" or coord == "O":
        print("This cell is occupied! Choose another one!")
    else:
        change = (3 - d) * 3 + (c - 1)
        a = list(a)
        a[change] = "X"
        "".join(a)
        flag = 0

out()
