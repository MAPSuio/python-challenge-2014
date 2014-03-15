# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

v=stdin.readline().split()
n=int(v[0])
m=int(v[1])

v=(m+2)*[-1]
w=[]
for i in range(n+2):
    w.append([])
    for j in range(m+2):
        w[i].append(-1)
    


for i in range(n):
    for j in range(m):
        w[i+1][j+1]=m*n



v=stdin.readline().split()
lines=stdin.readlines()
for line in lines:
    words=line.split()
    w[int(words[0])+1][int(words[1])+1]=-1
w[int(v[0])+1][int(v[1])+1]=0
qx=[int(v[0])+1]
qy=[int(v[1])+1]

i=0
dx=[0,0,1,-1]
dy=[1,-1,0,0]


while(i<len(qx)):
    for j in range(4):
        if (w[qx[i]+dx[j]][qy[i]+dy[j]]==m*n):
            qx.append(qx[i]+dx[j])
            qy.append(qy[i]+dy[j])
            w[qx[i]+dx[j]][qy[i]+dy[j]]=w[qx[i]][qy[i]]+1
    i+=1
if (w[1+int(v[2])][1+int(v[3])]==m*n or w[1+int(v[2])][1+int(v[3])]==-1):
    print "no deal"
else:
    print w[1+int(v[2])][1+int(v[3])]*10
