# @EXPECTED_RESULTS@: CORRECT

"""
Every time Sverre does a split, he get one more chocolate bar, so it does not
matter how he divides it. The number of splits needed is R * C - 1.
"""
from sys import stdin

line = stdin.readline();
line = line.split();
R = int(line[0]);
C = int(line[1]);
print R * C - 1
