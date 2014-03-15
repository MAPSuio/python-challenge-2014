# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

print 'FIGHT!' if int(stdin.readline()) % 6 else 'BEER!'
