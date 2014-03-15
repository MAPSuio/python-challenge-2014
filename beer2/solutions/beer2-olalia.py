# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
n=stdin.readline().split()[0]
ans=0
ans2=0
s=1
for i in range(len(n)):
    k=int(n[i])
    ans+=k
    ans2+=k*s
    s*=-1
if (((ans%9)!=0) or (int(n[-1])%2)!=0 or ans2%11!=0):
    print "FIGHT!"
else:
    print "BEER!"
