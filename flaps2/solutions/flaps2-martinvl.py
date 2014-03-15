# @EXPECTED_RESULTS@: CORRECT

from sys import stdin, exit
from scipy.special import gamma, gammaincc
from scipy import exp, log

def end_pos(v0, p):
    return v0*exp(p)*pow(p, -p)*gammaincc(p + 1, p)*gamma(p + 1)

v0, s = map(float, stdin.readline().split())

lo = 0.
hi = 1.
eps = 1e-10

while hi - lo > eps:
    p = (hi + lo)/2

    if end_pos(v0, p) < s:
        lo = p
    else:
        hi = p

print '%.8f' % ((hi + lo)/2)
