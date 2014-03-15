# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
from heapq import heappop, heappush

n = int(stdin.readline())
blocked = n*[False]
lo_blocked = []
hi_blocked = []

def is_blocked(seg):
    if blocked[seg]:
        return True

    if not len(lo_blocked) or not len(hi_blocked):
        return False

    if lo_blocked[0] < seg and -hi_blocked[0] > seg:
        return True

    return False

def block(seg):
    blocked[seg] = True

    heappush(lo_blocked, seg)
    heappush(hi_blocked, -seg)

def unblock(seg): # lazy removal from heaps
    blocked[seg] = False

    while len(lo_blocked) and not blocked[lo_blocked[0]]:
        heappop(lo_blocked)

    while len(hi_blocked) and not blocked[-hi_blocked[0]]:
        heappop(hi_blocked)

for line in stdin:
    i, w = line.split()
    i = int(i)

    if w == 'blocked':
        block(i)
    elif w == 'opened':
        unblock(i)
    else:
        if is_blocked(i):
            print 'no service'
        else:
            print 'good service'

