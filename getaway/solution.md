# Getaway
This problem can be solved using several search algorithms, with the police node marked as unreachable.

## Using [breadth-first search](http://en.wikipedia.org/wiki/Breadth-first_search)
Make a boolean two-dimensional array representing the grid, with all values set to `False`. Mark each of the points on the police route as `True`.

Put the position of the bank in a list called (for instance) `current`, and then repeat the following steps until the rendezvous point is found:

1. Make an empty list `next`
2. For each position in `current`, check first if it is the rendezvous point. If it is not, check each of the four neighboring positions in the grid. Add the ones that are `False` to `next`, and mark them as `True`.
3. Set `current = next`.

If the rendezvous point is not found, i.e. `current` is empty, then this means that there is no safe route.

Each repetition of these steps corresponds to moving one intersection from the bank. So if _r_ is the number of repetitions needed to find the rendezvous point, then the answer to the problem is `10*r`.