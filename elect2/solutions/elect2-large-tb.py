# @EXPECTED_RESULTS@: CORRECT

#Analytical solution
from sys import stdin;
import math;

elim = [False];


class Solver:

	def __init__(self):
		self.elim = [False];

	def solve_const(self,N):
		p = int(math.floor(math.log(N, 2)));
		l = N % 2**p;
		return 2*l+1;

sol = Solver();
line = stdin.readline().strip();
N = int(line);
ans = sol.solve_const(N);
print(ans);
