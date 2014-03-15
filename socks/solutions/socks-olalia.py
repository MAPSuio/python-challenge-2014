# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
T = int(stdin.readline())
s=[];

for i in range(T):
    s.append(stdin.readline())
s.sort()
c=0
d=0
while (c<T):
    if ((c+1==T or s[c]!=s[c+1]) and (c==0 or s[c]!=s[c-1])):
        print s[c],
        d=1
    c=c+1
if (d==0):
    print "Sock-sess"


