# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

N = int(stdin.readline())
frequency = {}
for test_case in range(N):
    label = stdin.readline().strip()
    if label in frequency:
        frequency[label] += 1
    else:
        frequency[label] = 1

socksess = True
remove_list = []
for label in frequency:
    if frequency[label] == 1:
        remove_list.append(label)
        socksess = False

if socksess:
    print "Sock-sess"
else:
    remove_list.sort()
    for label in remove_list:
        print label
