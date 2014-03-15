# @EXPECTED_RESULTS@: WRONG-ANSWER

from sys import stdin
from numpy import array
from numpy.linalg import norm

eps = 1e-8

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.d = array((float(x2 - x1), float(y2 - y1))) # direction
        self.d /= norm(self.d)

    def par(self, l): # is parallell
        return abs(1 - abs(self.d.dot(l.d))) < eps

    def orth(self, l): # is orthogonal
        return abs(self.d.dot(l.d)) < eps

n = int(stdin.readline())
lines = (Line(*map(int, line.split())) for line in stdin)

l = lines.next()
print 'wire it up' if all((l.par(line) or l.orth(line) for line in lines)) else 'broken'
