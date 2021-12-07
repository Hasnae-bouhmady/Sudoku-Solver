sudoku =[
        [0,0,0, 6,0,0, 4,0,0],
        [7,0,0, 0,0,3, 3,6,0],
        [0,0,0, 0,9,1, 0,8,0],

        [0,0,0, 0,0,0, 0,0,0],
        [0,5,0, 1,8,0, 0,0,3],
        [0,0,0, 3,0,6, 0,4,5],

        [0,4,0, 2,0,0, 0,6,0],
        [9,0,3, 0,0,0, 0,0,0],
        [0,2,0, 0,0,0, 1,0,0],]
def list_the_possibilities(liste,x,y):
    possibility = [1,2,3,4,5,6,7,8,9]
    for number in range(9):
        try:
            possibility.remove(liste[number][y])
        except:
            pass
        try:
            possibility.remove(liste[x][number])
        except:
            pass

    X,Y = (x//3)*3,(y//3)*3
    for x in range(X,X+3):
        for y in range(Y,Y+3):
            try:
                possibility.remove(liste[x][y])
            except:
                pass

    return possibility

def backtracking_fonction(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                possibility = list_the_possibilities(sudoku,x,y)
                for p in possibility:
                    sudoku[x][y] = p
                    backtracking_fonction(sudoku)
                    sudoku[x][y] = 0
                return
    print()
    for ligne in sudoku:
        print(ligne)

backtracking_fonction(sudoku)
