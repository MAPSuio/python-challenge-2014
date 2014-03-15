from sys import stdin

m, n, k = map(int, stdin.readline().split())
grid = [[c for c in line] for line in stdin]

# find all bacteria cells
bacteria = []
for i in xrange(m):
    for j in xrange(n):
        if grid[i][j] == '#':
            bacteria.append((i, j))

num_bacteria = len(bacteria)

def grow(i, j):
    if i < 0 or i >= m or j < 0 or j >= n:
        return False

    if grid[i][j] != '.':
        return False

    grid[i][j] = '#'

    return True

new_bacteria = bacteria

# grow bacteria k days
for l in xrange(k):
    bacteria = new_bacteria
    new_bacteria = []

    for i, j in bacteria:
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            new_i = i+di
            new_j = j+dj

            if grow(new_i, new_j):
                num_bacteria += 1
                new_bacteria.append((new_i, new_j))

print num_bacteria
