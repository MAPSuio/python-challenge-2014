# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
n=int(stdin.readline())
if (n%6):
    print "FIGHT!"
else:
    print "BEER!"
