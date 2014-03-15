# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
from math import log

v = [sum(s[1:])*log(s[0]) for s in [map(int, line.split()) for line in stdin]]

print max(xrange(len(v)), key=v.__getitem__)
