# @EXPECTED_RESULTS@: CORRECT

from sys import stdin
s = stdin.readline().split()


m=int(s[0])
n=int(s[1])
t=int(s[2])

s=[]


for i in range(m):
    s.append(stdin.readline())

tab=[[]]
qx=[]
qy=[]
inti=0

dx=[1, -1, 0, 0]
dy=[0,0,1,-1]

for i in range(m+2):
    tab[0].append(-1)
tab.append([])
for i in range(1,m+1):
    tab[i].append(-1)
    
    for j in range(1,n+1):
        if (j>=len(s[i-1]) or s[i-1][j-1]=='X'):
            tab[i].append(-1)
        if (j<len(s[i-1]) and s[i-1][j-1]=='#'):
            tab[i].append(0)
            qx.append(i)
            qy.append(j)
        if (j<len(s[i-1]) and s[i-1][j-1]=='.'):
            tab[i].append(999999999999999)
    tab[i].append(-1)
    tab.append([])
    #print s[i-1]
        
for i in range(m+2):
    tab[m+1].append(-1)
while(inti<len(qx) and tab[qx[inti]][qy[inti]]<=t):
    for i in range(4):
        if (tab[dx[i]+qx[inti]][dy[i]+qy[inti]]!=-1):
            if (tab[dx[i]+qx[inti]][dy[i]+qy[inti]]>tab[qx[inti]][qy[inti]]+1):
                tab[dx[i]+qx[inti]][dy[i]+qy[inti]]=tab[qx[inti]][qy[inti]]+1
                qx.append(qx[inti]+dx[i])
                qy.append(qy[inti]+dy[i])
    inti=inti+1
        
print inti
"""
ans=0
for i in range (1,d+1):
    for j in range(1,d+1):
        if (tab[i][j]<=n and tab[i][j]!=-1):
            ans=ans+1
            
        
print ans
"""
