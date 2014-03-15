# @EXPECTED_RESULTS@: TIMELIMIT

from sys import stdin
from numpy import zeros

n = int(stdin.readline())
blocked = zeros(n, dtype=bool)

for line in stdin:
    i, w = line.split()
    i = int(i)

    if w == 'status':
        if blocked[:i+1].any() and blocked[i:].any():
            print 'no service'
        else:
            print 'good service'
    else:
        blocked[i] = (w == 'blocked')
