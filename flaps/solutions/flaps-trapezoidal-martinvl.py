# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
from math import exp

def trapezoidal(f, a, b, n):
    h = (b - a)/float(n)
    s = f(a)/2 + f(b)/2
    t = a + h

    for i in xrange(1, n):
        s += f(t)
        t += h

    return h*s

v0, t, p = map(float, stdin.readline().split())
n = 100000

def v(t):
    return v0*pow(p, -p)*pow(t + p, p)*exp(-t)

print '%.8f' % trapezoidal(v, 0, t, n)
