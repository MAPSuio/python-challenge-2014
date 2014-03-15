# @EXPECTED_RESULTS@: CORRECT

import Queue
import pprint
from sys import stdin
pp = pprint.PrettyPrinter(indent=4)

# This solution uses A* search

# input
l = stdin.readline().split()
n = int(l[0])
m = int(l[1])

l = stdin.readline().split()
b1 = int(l[0])
b2 = int(l[1])
r1 = int(l[2])
r2 = int(l[3])

# model of city
city = [[0]*n for i in range(m)]

# input police path
for line in stdin:
    l = line.split()
    a = int(l[0])
    b = int(l[1])
    city[a][b] = 1


# heuristic function
def h(x, y):
    return abs(x-r1) + abs(y-r2)


# function to check if coordinates are inside the city
def insideCity(x, y):
    return not (x < 0 or y < 0 or x >= n or y >= m)

# creating priority queue and inserting the tuple representing the bank
# tuples have three coordinates:
# 1: (distance to bank + assumed distance to goal , assumed distance to goal)
# 2: distance from bank
# 3: coordinates of point
pq = Queue.PriorityQueue()
pq.put(((h(b1, b2), h(b1, b2)), 0, (b1, b2)))
city[b1][b2] = 2

result = "no deal"
while not pq.empty():
    item = pq.get()

    # check if the goal is reached
    if item[2] == (r1, r2):
        result = item[0][0]*10
        break

    # for each direction add to priority queue if not visited before
    for d in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
        p1 = item[2][0] + d[0]
        p2 = item[2][1] + d[1]
        if insideCity(p1, p2):
            if city[p1][p2] != 1 and city[p1][p2] != 2:
                city[p1][p2] = 2
                pq.put(((item[1] + h(p1, p2) + 1, h(p1, p2)), item[1] + 1, (p1, p2)))

print result
