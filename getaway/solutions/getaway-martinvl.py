# @EXPECTED_RESULTS@: CORRECT

from sys import stdin, exit

m, n = map(int, stdin.readline().split())
bi, bj, ri, rj = map(int, stdin.readline().split())
b = (bi, bj)
r = (ri, rj)
p = [map(int, line.split()) for line in stdin]

visited = [n*[False] for i in xrange(m)]

# mark police route
for pi, pj in p:
    visited[pi][pj] = True

# BFS stuff
def visit(p):
    visited[p[0]][p[1]] = True

def valid(p):
    return (p[0] >= 0) and (p[1] >= 0) and (p[0] < m) and (p[1] < n) and not visited[p[0]][p[1]]

def bfs(start, goal):
    current = []
    next = [start]
    steps = 0

    while next:
        current = next
        next = []

        for p in current:
            if p == goal:
                return steps

            for dir in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                p_ = (p[0]+dir[0], p[1]+dir[1])

                if valid(p_):
                    visit(p_)
                    next.append(p_)


        steps += 1

    return -1

# initiate search
steps = bfs(b, r)

if steps == -1:
    print 'no deal'
else:
    print 10*steps
