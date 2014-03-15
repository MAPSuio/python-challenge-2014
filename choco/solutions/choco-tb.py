# @EXPECTED_RESULTS@: CORRECT

from sys import stdin;

#Let f(R,C) be optimal nb. of divisions.
#
#Suppose f(R,C) = R*C-1. This holds for R=C=1.
#Suppose then that f(R+1, C) < (R+1)*C-1. Then
#f(R,C) < f(R+1, C)-C= R*C-1. Contradiction.

line = stdin.next();
line = line.split();
R = int(line[0]);
C = int(line[1]);
ans = R*C-1;
print(ans);


