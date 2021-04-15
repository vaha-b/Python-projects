# https://hyperskill.org/projects/73/stages/401/implement

cells = input('Enter cells')
list('cells')
print("---------")
print("| " + cells[0] + " " + cells[1] + " " + cells[2] + " |")
print("| " + cells[3] + " " + cells[4] + " " + cells[5] + " |")
print("| " + cells[6] + " " + cells[7] + " " + cells[8] + " |")
print("---------")

cells_matrix_hor = [[cells[0], cells[1], cells[2]], [
    cells[3], cells[4], cells[5]], [cells[6], cells[7], cells[8]]]
cells_matrix_ver = [[cells[0], cells[3], cells[6]], [
    cells[1], cells[4], cells[7]], [cells[2], cells[5], cells[8]]]
cells_matrix_dia = [[cells[0], cells[4], cells[8]],
                    [cells[2], cells[4], cells[6]], ["K", "K", "K"]]
print(cells_matrix_hor[0][0])
print(cells_matrix_ver[2])


char = [str(n) for n in cells]
X_char = [str(n) for n in char if n == "X"]
O_char = [str(n) for n in char if n == "O"]
_char = [str(n) for n in char if n == "_"]

X_wins = []
for nr in range(0, 3):
    if cells_matrix_hor[nr] == ["X", "X", "X"] or cells_matrix_ver[nr] == ["X", "X", "X"] or cells_matrix_dia[nr] == ["X", "X", "X"]:
        X_wins.append(nr)

O_wins = []
for nr in range(0, 3):  # [0, 1, 2]
    if cells_matrix_hor[nr] == ["O", "O", "O"] or cells_matrix_ver[nr] == ["O", "O", "O"] or cells_matrix_dia[nr] == ["O", "O", "O"]:
        O_wins.append(nr)

if (abs(len(X_char) - len(O_char)) > 1 or ((X_wins == [0] or X_wins == [1] or X_wins == [2]) and (O_wins == [0] or O_wins == [1] or O_wins == [2]))):
    print("Impossible")

elif (X_wins == [0] or X_wins == [1] or X_wins == [2]):
    print("X wins")

elif (O_wins == [0] or O_wins == [1] or O_wins == [2]):
    print("O wins")

elif len(X_char) + len(O_char) < 9:
    print("Game not finished")

else:
    print('Draw')
