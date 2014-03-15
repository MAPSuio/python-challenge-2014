# Railway management
_This was supposed to be one of the two hardest problems in the contest. However, the testcases for this problem turned out not to be good enough, as all the accepted solutions did the status checking in O(n) time, which should have been too slow. Because of this the problem got a lot easier. We've added some more testcases after the competition that fail the O(n) solutions._

A segment is reachable unless itself is blocked, or if any segments between it and each of the terminal stations. This can be checked quickly if you keep track of the lowest and highest blocked segment, the hard part is to update this as segments are unblocked. The point of this problem was that you had to be able to block, unblock and check segments in at least O(log n) time.

## Using two [heaps](http://en.wikipedia.org/wiki/Heap)
One way to solve this problem is to use a maxheap and a minheap, into which the indices of the blocked segments are added, and unblocked segments are removed. Performing a block/unblock then takes O(log n) time, while checks can be done in O(1). Unfortunately `heapq` in the Python standard library doesn't implement _remove_, so this can be a little cumbersome to get right.

## Using a [Fenwick tree](http://en.wikipedia.org/wiki/Fenwick_tree)
A second way is to use a Fenwick tree, with a bucket for each segment. Fenwick trees lets you efficiently calculate the sum from number _i_ to number _j_ in a list of numbers.

Blocking segment _i_ can be done by adding `1` to bucket _i_, unblocking can similarily be done by subtracting `1` from bucket _i_. The status of segment _i_ is then simply a matter of checking that either the sum from index `0` to _i_, or the sum from _i_ to _n_, are `0`.

All of these operations take O(log n), so overall complexity is O(_k_ log _n_), which is doable for this input size.
