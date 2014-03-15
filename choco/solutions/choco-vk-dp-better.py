# @EXPECTED_RESULTS@: TIMELIMIT
from sys import stdin

line = stdin.readline()
line = line.split()
R = int(line[0])
C = int(line[1])

grid = [C * [0] for i in range(R)]
for r in range(1, R):
    grid[r][0] = r

for c in range(1, C):
    grid[0][c] = c

for r in range(1, R):
    for c in range(1, C):
        min = None
        candidate = grid[0][c] + grid[r-1][c]
        if candidate < min or min is None:
            min = candidate

        if min is None:
            grid[r][c] = 0
        else:
            grid[r][c] = min + 1

print grid[R-1][C-1]
