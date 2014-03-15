# @EXPECTED_RESULTS@: WRONG-ANSWER

from sys import stdin
from scipy.special import gamma, gammainc
from scipy import exp, log

def v_integral(v0, t, p):
    return v0 * exp(p*(1 - log(p)))*gammainc(p + 1, p + t)*gamma(p + 1)

def pos(v0, t, p):
    return v_integral(v0, t, p) - v_integral(v0, 0, p)

print '%.7f' % pos(*map(float, stdin.readline().split()))
