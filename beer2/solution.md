# Beer shopper 2
The task is to check if _f_ is divisible by 198, but _f_ is so large (bigint) that modulo (and division etc) is too slow.

Coincidentally 198 can be written as 2 * 9 * 11, so it suffices to check if _f_ is divisible by 2, 9 _and_ 11.

It's easy to check if _f_ is divisible by 2: just check that the last digit is divisible by 2.

_f_ is divisible by 9 if its digit sum is divisible by 9. So just check that `digit_sum_of_f % 9 == 0`.

_f_ is divisible by 11 if its alternating digit sum is divisible by 11. So if _f_ is `1234` then `alternating_digit_sum_of_f = 1 - 2 + 3 - 4`. Check that `alternating_digit_sum_of_f % 11 == 0`.

In this problem _f_ could have up to a million digits, and taking the sum of a million digits is perfectly doable in the alloted time.

One last tip is to keep _f_ as a string (don't convert it to an integer). By keeping _f_ as a string it is easy to access each digit. Besides, converting to int takes a lot of time, and only causes trouble in this case.