# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
from math import exp

def midpoint(f, a, b, n):
    h = (b - a)/float(n)
    t = a + .5*h
    s = 0

    for i in xrange(n):
        s += f(t)
        t += h

    return h*s

v0, t, p = map(float, stdin.readline().split())
n = 100000

def v(t):
    return v0*pow(p, -p)*pow(t + p, p)*exp(-t)

print '%.8f' % midpoint(v, 0, t, n)
