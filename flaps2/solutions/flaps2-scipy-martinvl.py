# @EXPECTED_RESULTS@: CORRECT

from numpy import linspace, power, exp, sum, inf
from scipy.integrate import quad
from scipy.optimize import bisect
from sys import stdin

def v(v0, p, t):
    return v0*power(p, -p)*power(t + p, p)*exp(-t)

v0, s = map(float, stdin.readline().split())

print '%.8f' % bisect(lambda p: quad(lambda t: v(v0, p, t), 0, inf)[0] - s, 0, 1.0000000001)
