# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
import math

# Count number of cells, and multiply this by log(n) for each schema.

max = 0.0
counter = 0
for line in stdin:

    l = line.split()
    n = int(l.pop(0))

    sum_cells = 0
    for c in l:
        sum_cells += int(c)

    if sum_cells * math.log(n) > max:
        max_index = counter
        max = sum_cells * math.log(n)

    counter += 1

print max_index
