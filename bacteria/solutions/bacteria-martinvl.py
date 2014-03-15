# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
from numpy import array, sum
from scipy.ndimage import binary_dilation

c_to_v = {'#':1, '.':0, 'X':-1}

m, n, t = map(int, stdin.readline().split())
dish = array([[c_to_v[c] for c in l[:-1]] for l in stdin])
mask = 1 - (dish == -1)
result = binary_dilation(dish == 1, iterations=t, mask=mask)

print sum(result)
