import sys
from z3 import *

grid = [[Int("c_%s_%s" % (i, j)) for j in xrange(9)] for i in xrange(9)]

f = open(sys.argv[1], 'r')

s = f.read().replace('\n', '')
solver = Solver()

for i in range(9):
    for j in range(9):
        solver.add(And(1 <= grid[i][j], grid[i][j] <= 9))
        c = s[i * 9 + j]
        if c != '.':
            solver.add(grid[i][j] == int(c))

for i in range(9):
    solver.add(Distinct(grid[i]))

for i in range(9):
    col = []
    for j in range(9):
        col.append(grid[j][i])
    solver.add(Distinct(col))

for i in xrange(0, 9, 3):
    for j in xrange(0, 9, 3):
        small_grid = []
        for k in xrange(i, i + 3):
            for l in xrange(j, j+3):
                small_grid.append(grid[k][l])
        solver.add(Distinct(small_grid))


if solver.check() == sat:
    m = solver.model()
    print m
    for i in range(9):
        for j in range(9):
            print m.evaluate(grid[i][j]),
        print
