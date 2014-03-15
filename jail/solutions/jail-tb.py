# @EXPECTED_RESULTS@: CORRECT

from sys import stdin;

class Solver:

	def __init__(self):
		self.read_parameters();
		self.read_walls();

	def read_parameters(self):
		line = stdin.next();
		par = line.split();
		self.M = int(par[0]); self.N = int(par[1]);
		self.I = int(par[2]);

	def read_walls(self):
		M = self.M; N = self.N;
		self.vertical = [];
		self.horizontal = [];
		self.dp = [[0 for m in range(M)] for n in range(N)];
		self.dp[0][0] = self.I;
	
		for n in range(N):
			line = stdin.next();
			self.vertical.append([int(w) for w in line.split()]);
		for n in range(N-1):
			line = stdin.next();
			self.horizontal.append([int(w) for w in line.split()]);

	def calc_opt(self, m,n):
		if(m == 0 and n == 0):
			return;
		self.dp[n][m] = max(self.left(m,n), self.over(m,n),0);

	def over(self, m, n):
		if(n == 0):
			return 0;
		return self.dp[n-1][m]-self.horizontal[n-1][m];

	def left(self,m,n):
		if(m==0):
			return 0;
		return self.dp[n][m-1] -self.vertical[n][m-1];

	def ans(self):
		for m in range(self.M):
			for n in range(self.N):
				self.calc_opt(m,n);
		return self.dp[-1][-1];


sol = Solver();
print(sol.ans());
