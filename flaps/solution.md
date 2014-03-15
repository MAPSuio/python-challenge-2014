# Flaps
There are two primary ways to solve this problem:
## Numerical integration
This is probably the most straight-forward way to solve this problem. Implement the _v_-function, and apply a numerical integration algorithm of your choice. Trapezoidal, midpoint or Gaussian quadrature should work fine, just make sure that your calculations are accurate enough.

SciPy has several methods that are applicable here, so no need to code from scratch.

Timing should not be an issue, there is plenty of time to achieve way more precision than you need.

## "Analytical" solution
It is possible to express this integral with the incomplete gammafunction. The easiest way to discover how is probably to use Wolfram Alpha (which was allowed).

The incomplete gamma function in SciPy has a different parameterization than the one Wolfram Alpha uses, so make sure you get it right!

The implementation of the gamma function is of course also just an estimate which takes some time to obtain. This solution is therefore not _clearly_ superior to doing the integration yourself.