# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
from collections import Counter

N = int(stdin.readline())

# find the labels occuring only once
removed = [l for l, c in Counter(stdin).items() if c == 1]

print ''.join(sorted(removed)).strip() if removed else 'Sock-sess'
