# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

n=int(stdin.readline())
for i in range(n):
    s=stdin.readline().split()
    if (len(s)==1 and s[0]=="Complaint"):
        print "Reject"
    else:
        print "Investigate"
