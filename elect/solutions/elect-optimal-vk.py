# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
import math

# Algorithm: Found analytical solution.


def get_answer(n):
    return int(2*n - 2**(math.floor((math.log(n)/math.log(2)))+1)+1)

for line in stdin:
    print get_answer(int(line.strip()))
