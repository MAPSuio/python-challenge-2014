# @EXPECTED_RESULTS@: TIMELIMIT

from sys import stdin

print 'FIGHT!' if int(stdin.readline()) % 198 else 'BEER!'
