# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

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
lines = (Line(*map(int, line.split())) for line in stdin)

l = lines.next()
print 'wire it up' if all((l.par(line) or l.orth(line) for line in lines)) else 'broken'
