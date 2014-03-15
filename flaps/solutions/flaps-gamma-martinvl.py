# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
from scipy.special import gamma, gammaincc
from scipy import exp, log

def v_integral(v0, t, p):
    return -v0*exp(p)*pow(p, -p)*gammaincc(p + 1, p + t)*gamma(p + 1)

def pos(v0, t, p):
    return v_integral(v0, t, p) - v_integral(v0, 0, p)

print '%.8f' % pos(*map(float, stdin.readline().split()))
