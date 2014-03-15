# Nuts
The number of combinations for each scheme is given by n<sup>c<sub>1</sub> + c<sub>2</sub> + ... + c<sub>r</sub></sup>. The constraints given for this problem allows this number to get as large as 10<sup>6*10<sup>7</sup></sup>, which takes way too long to calculate (it requires arbitrary size integers which is slow). The trick is to take the logarithm of this number:

log(n<sup>c<sub>1</sub> + c<sub>2</sub> + ... + c<sub>r</sub></sup>) = (c<sub>1</sub> + c<sub>2</sub> + ... + c<sub>r</sub>) log(n)

This number on the right side is a lot smaller, and can be calculated efficiently since it is guaranteed to be less than 6 * 10<sup>7</sup> log(10). The logarithm is a strictly increasing function, so if a > b then log(a) > log(b). This means that the sorting order is preserved.

So this problem boils down to calculating (c<sub>1</sub> + c<sub>2</sub> + ... + c<sub>r</sub>) log(n) for each line, and then find the index for the highest such value.