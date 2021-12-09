def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], " " , end="")
        print("")

def cellule_vide(arr, l):
    for ligne in range(9):
        for colonne in range(9):
            if arr[ligne][colonne] == 0:
                l[0] = ligne
                l[1] = colonne
                return True
    return False


def possibilite_ligne(arr, ligne, num):
    for i in range(9):
        if arr[ligne][i] == num:
            return True
    return False


def possibilite_colonne(arr, colonne, num):
    for i in range(9):
        if arr[i][colonne] == num:
            return True
    return False


def possibilite_box(arr, ligne, colonne, num):
    for i in range(3):
        for j in range(3):
            if arr[i + ligne][j + colonne] == num:
                return True
    return False


def cellule_valide(arr, ligne, colonne, num):
    return not possibilite_ligne(arr, ligne, num) and not possibilite_colonne(arr, colonne, num) and not possibilite_box(arr, ligne - ligne % 3, colonne - colonne % 3, num)



def resolution_sudoku(arr):

    l = [0, 0]

    if (not cellule_vide(arr, l)):
        return True

    ligne = l[0]
    colonne = l[1]

    for num in range(1, 10):

        if (cellule_valide(arr, ligne, colonne, num)):

            arr[ligne][colonne] = num

            if resolution_sudoku(arr):
                return True

            arr[ligne][colonne] = 0

    return False


if __name__ == "__main__":

    sudoku = [[0 for x in range(9)] for y in range(9)]

    sudoku = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if resolution_sudoku(sudoku):
        print_grid(sudoku)
    else:
        print
        "Pas de solution"
