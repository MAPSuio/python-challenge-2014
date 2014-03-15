# @EXPECTED_RESULTS@: CORRECT

from numpy import linspace, power, exp, sum
from sys import stdin

v0, s = map(float, stdin.readline().split())
n = 100000
p = 0

def midpoint(f, a, b, n):
    h = (b - a)/float(n)
    t = linspace(a + .5*h, b - .5*h, n)

    return h*sum(f(t))

def v(t):
    return v0*power(p, -p)*power(t + p, p)*exp(-t)

def end_pos():
    return midpoint(v, 0, 50, n)

lo = 0.
hi = 1.
eps = 1e-10

while hi - lo > eps:
    p = (hi + lo)/2

    if end_pos() < s:
        lo = p
    else:
        hi = p

print '%.8f' % ((hi + lo)/2)
