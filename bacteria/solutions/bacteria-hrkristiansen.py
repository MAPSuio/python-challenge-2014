# @EXPECTED_RESULTS@: CORRECT

import sys

m, n, t = [int(x) for x in sys.stdin.readline().split()]
#print d, t
lines = []
try:
    for line in sys.stdin.readlines():
        lines.append([x for x in line])
except:
    pass

def infect(l, n):
    if l < 0 or l >= len(lines):
        return
    if n < 0 or n >= len(lines[l]):
        return
    if lines[l][n] is '.':
        lines[l][n] = '#'

for x in range(t):
    bacterias = []
    for l, line in enumerate(lines):
        for n, ch in enumerate(line):
            if ch is '#':
                bacterias.append((l,n))
    for l, n in bacterias:
        infect(l-1, n)
        infect(l+1, n)
        infect(l, n-1)
        infect(l, n+1)

print sum([sum([1 for x in line if x is '#' ]) for line in lines])
