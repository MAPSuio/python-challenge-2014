# Wired
Must be able to check parallellism and orthogonalism without error, so integer arithmetics is required.

For this problem all we really care about is the direction of each line, so it's a good idea to just represent the lines by `dx = x2 - x1` and `dy = y2 - y1`.

## Checking if two lines are parallell
Two lines (represented by `(dx1, dy1)` and `(dx2, dy2)`) are parallell if `dy1/dx1 == dy2/dx2`. This is a problematic equation to evaluate however, because `dx1` and `dx2` might be `0`. Also we have to use floats, which leads to precision loss. The trick is simply to rewrite the equation to `dy1*dx2 == dy2*dx1`, which is easy to check.

## Checking if two lines are orthogonal
This is a little easier, simply checking that the dot product of the direction vectors is `0`:

`dx1*dx2 + dy1*dy2 == 0`

## Checking that this property holds for all pairs of lines
First observe that if a and b, and b and c are parallell lines, then a and c must also be parallell. A similar argument holds for orthogonality. 

We can select _one_ line (for instance the first line), and then check if this line is parallell or orthogonal to all the other lines. If this holds true, then by the observation above all lines are either parallell or orthogonal.

This means that we can check whether all pairs of lines are parallell or orthogonal in O(n) time. Checking all pairs (for instance using two for-loops) is too slow on this problem, as this takes O(n<sup>2</sup>) time.