# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

n=int(stdin.readline().split()[0])

v=[]
for i in range(n):
    v.append(0)

def inc(i,j):
    while(i<n):
        v[i]=v[i]+j
        i=i|(i+1)
    return;

def q(i):
    c=0
    while(i>-1):
        c=c+v[i]
        i=(i&(i+1))-1
    return c;


lines=stdin.readlines()

for line in lines:
    s=line.split()
    if (len(s)==0):
        break
    
    a=int(s[0])
    b=s[1]
    if (b=="opened"):
        inc(a,-1)
    if (b=="blocked"):
        inc(a,1)
    if (b=="status"):
        if (q(a)==0 or (q(n-1)-q(a-1))==0):
            print "good service"
        else:
            print "no service"

        
