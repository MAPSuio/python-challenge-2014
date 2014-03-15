# @EXPECTED_RESULTS@: TIMELIMIT

from sys import stdin
from math import log

v = [s[0]**sum(s[1:]) for s in [map(int, line.split()) for line in stdin]]

print max(xrange(len(v)), key=v.__getitem__)
