# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

# Algorithm: Simulating the process.


def get_next(l, p, n):
    c = 0
    while c < 2:
        p = (p+1) % n
        if l[p] == 0:
            c += 1
    return p


def get_answer(n):
    l = [0]*n

    pos = 1 % n
    for it in range(n-1):
        l[pos] = 1
        pos = get_next(l, pos, n)
    return pos + 1


for line in stdin:
    line.strip()
    print get_answer(int(line))
