# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

s=stdin.readlines()


for line in s:
    n=int(line)
    ans=1;
    c=1;
    while(n/2>0):
        if (n%2):
            ans+=2*c
        c*=2
        n/=2
    print ans
                
