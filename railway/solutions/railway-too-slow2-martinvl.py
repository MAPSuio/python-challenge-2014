# @EXPECTED_RESULTS@: TIMELIMIT

from sys import stdin

n = int(stdin.readline())
blocked = n*[False]

def blocked_left(i):
    for j in xrange(i):
        if blocked[j]:
            return True

    return False

def blocked_right(i):
    for j in xrange(i+1, len(blocked)):
        if blocked[j]:
            return True

    return False

def reachable(i):
    if blocked[i]:
        return False

    return not blocked_left(i) or not blocked_right(i)

for line in stdin:
    i, w = line.split()
    i = int(i)

    if w == 'status':
        print 'good service' if reachable(i) else 'no service'
    else:
        blocked[i] = (w == 'blocked')
