# @EXPECTED_RESULTS@: TIMELIMIT

from sys import stdin, exit

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.d = (x2 - x1, y2 - y1) # direction

    def par(self, l): # is parallell
        x, y = self.d
        lx, ly = l.d

        return x*ly == y*lx

    def orth(self, l): # is orthogonal
        x, y = self.d
        lx, ly = l.d

        return x*lx == -y*ly

n = int(stdin.readline())
lines = [Line(*map(int, line.split())) for line in stdin]

for i in xrange(len(lines)):
    l1 = lines[i]

    for j in xrange(i+1, len(lines)):
        l2 = lines[j]

        if not l1.par(l2) and not l1.orth(l2):
            print 'broken'
            exit(0)

print 'wire it up'
