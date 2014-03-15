# @EXPECTED_RESULTS@: CORRECT

from numpy import linspace, power, exp, sum
from sys import stdin

def midpoint(f, a, b, n):
    h = (b - a)/float(n)
    t = linspace(a + .5*h, b - .5*h, n)

    return h*sum(f(t))

v0, t, p = map(float, stdin.readline().split())
n = 1000000

def v(t):
    return v0*power(p, -p)*power(t + p, p)*exp(-t)

print '%.8f' % midpoint(v, 0, t, n)
