# @EXPECTED_RESULTS@: TIMELIMIT
from sys import stdin

line = stdin.readline()
line = line.split()
R = int(line[0])
C = int(line[1])

grid = [C * [0] for i in range(R)]

for r in range(0, R):
    for c in range(0, C):
        min = None
        for rr in range(r):
            candidate = grid[rr][c] + grid[r-rr-1][c]
            if candidate < min or min is None:
                min = candidate
        for cc in range(c):
            candidate = grid[r][cc] + grid[r][c-cc-1]
            if candidate < min or min is None:
                min = candidate

        if min is None:
            grid[r][c] = 0
        else:
            grid[r][c] = min + 1

print grid[R-1][C-1]
