# Saying hello [sample]
You want to test your programming skills by making a modified version of the classic `Hello, world!`-program. Your program should read a number _n_, and then print _n_ lines containing `Hello, world!`.

## Input
Input consists of a single line with an integer _n_, the number of `Hello, world!` you should output.

## Output
Output _n_ lines containing `Hello, world!`.

## Constraints
1 &le; n &le; 10<sup>3</sup>

## Sample input 1
```
1
```

## Sample output 1
```
Hello, world!
```

## Sample input 2
```
5
```

## Sample output 2
```
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!
```

## Solution
```
from sys import stdin

n = int(stdin.read())

for i in xrange(n):
    print 'Hello, world!'
```