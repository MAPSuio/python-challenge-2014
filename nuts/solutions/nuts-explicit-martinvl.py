# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
from math import log

K_MAX = 1000

max_idx = -1
max_val = float("-inf")

for i, line in zip(xrange(K_MAX), stdin):
    nums = map(int, line.split())
    n = nums[0]
    c = nums[1:]

    val = sum(c)*log(n)

    if val > max_val:
        max_val = val
        max_idx = i

print max_idx
