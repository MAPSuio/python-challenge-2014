# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

class FenwickTree:
    def __init__(self, n):
        self.buckets = n*[0]

    def increase(self, bucket, delta):
        i = bucket

        while i < len(self.buckets):
            self.buckets[i] += delta
            i |= i + 1

    def get_sum(self, from_bucket, to_bucket):
        return self.sum(to_bucket) - self.sum(from_bucket - 1)

    def sum(self, bucket):
        sum = 0
        i = bucket;

        while i >= 0:
            sum += self.buckets[i]
            i = (i & (i + 1)) - 1

        return sum

n = int(stdin.readline())
segments = FenwickTree(n)

for line in stdin:
    i, w = line.split()
    i = int(i)

    if w == 'blocked' or w == 'opened':
        segments.increase(i, 1 if w == 'blocked' else -1)
    else:
        if segments.get_sum(0, i) == 0 or segments.get_sum(i, n-1) == 0:
            print 'good service'
        else:
            print 'no service'

