# Bacterial growth
To primary ways to solve:

## Using [breadth-first search](http://en.wikipedia.org/wiki/Breadth-first_search)
Start by finding the positions of the bacteria cells, put these in a list. From each of the cells in the list, try to grow in all direction. Make sure that you only grow into cells with `.` in them. Mark all these cells with `#`. Put all the new-grown bacteria into a list. Repeat this process _t_ times.

Finally count the number of `#` in the grid, or keep track of the number of bacteria as you grow them.

Note that it's impossible to grow _from_ a specific bacteria cell more than once, so we only need to keep track of the cells that we've just grown.

Time should not be an issue here, plenty of time for O(MN).

## Using [binary morphology](http://en.wikipedia.org/wiki/Mathematical_morphology#Dilation)
Growing a bacteria in this problem is exactly the same as doing binary dilation on the bacterial cells with a standard "pluss" structuring element and with a mask defined by the `X`-s.

The complete solution is to run _t_ iterations of dilations, then count the number of bacteria.

SciPy has a built-in function for binary dilation, so implementation is trivial.