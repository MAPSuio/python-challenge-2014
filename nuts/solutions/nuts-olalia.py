# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
import math
ans=0
f=0
c=0
l=stdin.readlines()
for line in l:
    s=line.split()
    if (len(s)==0):
        break
    n=int(s[0])
    k=-n
    for i in s:
        k=k+int(i)
    if (math.log(n)*k>f):
        f=math.log(n)*k
        ans=c
    #if (c==276 or c==720):
     #   print s, f, math.log(n)*k
    
    c=c+1
    n=int(s[0])
    
    
print ans,

