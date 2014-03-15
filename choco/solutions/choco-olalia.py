# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
s = stdin.readline().split()
d=int(s[0])
n=int(s[1])

print d*n-1
