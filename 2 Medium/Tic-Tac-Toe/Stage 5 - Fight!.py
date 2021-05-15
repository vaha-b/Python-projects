# About the project
# https://hyperskill.org/projects/73

# Stage description
# https://hyperskill.org/projects/73/stages/403/implement

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
playing = True


def play_game():
    display_board()
    your_turn()


def display_board():
    print("---------")
    print("|" + " " + board[0] + " " + board[1] + " " + board[2] + " " + "|")
    print("|" + " " + board[3] + " " + board[4] + " " + board[5] + " " + "|")
    print("|" + " " + board[6] + " " + board[7] + " " + board[8] + " " + "|")
    print("---------")


def your_turn():
    while playing:
        z = x, y = input("Enter the coordinates: ").split()
        position = " ".join(z)

        if position == "1 1":
            board[6] = "X"
        elif position == "1 2":
            board[3] = "X"
        elif position == "1 3":
            board[0] = "X"
        elif position == "2 1":
            board[7] = "X"
        elif position == "2 2":
            board[4] = "X"
        elif position == "2 3":
            board[1] = "X"
        elif position == "3 1":
            board[8] = "X"
        elif position == "3 2":
            board[5] = "X"
        elif position == "3 3":
            board[2] = "X"

        display_board()
        winner()


def winner():
    row_1 = board[0] == board[1] == board[2] != " "
    row_2 = board[3] == board[4] == board[5] != " "
    row_3 = board[6] == board[7] == board[8] != " "

    collum_1 = board[0] == board[3] == board[6] != " "
    collum_2 = board[1] == board[4] == board[7] != " "
    collum_3 = board[2] == board[5] == board[8] != " "

    cross_1 = board[0] == board[4] == board[8] != " "
    cross_2 = board[6] == board[4] == board[2] != " "

    global playing

    if row_1:
        print(board[0] + " wins")
        playing = False
    elif row_2:
        print(board[3] + " wins")
        playing = False
    elif row_3:
        print(board[6] + " wins")
        playing = False
    elif collum_1:
        print(board[0] + " wins")
        playing = False
    elif collum_2:
        print(board[1] + " wins")
        playing = False
    elif collum_3:
        print(board[2] + " wins")
        playing = False
    elif cross_1 or cross_2:
        print(board[4] + " wins")
        playing = False
    else:
        if " " not in board:
            print("draw")
            playing = False


play_game()
