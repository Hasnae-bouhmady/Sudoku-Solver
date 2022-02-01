import numpy as np
from Solve import solve_sudoku
from Draw import draw1
p = np.loadtxt("Temp/array",delimiter= ",",dtype='int')
print(p)
draw1(p)
