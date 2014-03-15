# Bacterial growth
![](../images/bacterial.png)


Lisa is a lab technician working at a hospital testing blood samples. Testing blood samples can be a labour intensive undertaking. For each sample Lisa must first prepare a glass plate with a growth medium, then add some of the blood from the sample. After a day has passed Lisa counts the number of visible bacteria cells, using a microscope. Then after another couple of days Lisa recounts the number of bacteria. The amount of growth in the given time span gives the doctors an impression of how aggressive the bacteria is.

Lately Lisa has been testing a lot of samples for the _Quatuor_ bacteria, which she has noticed grows in a very predictable way. If the glass plate is divided into a grid where each bacteria cell occupies a grid cell, the growth during one day can be described as follows: Each cell divides into five, such that there is a cell added north, south, east and west of the original cell. The only exceptions from this growth pattern is when any of these grid cells are already occupied of other cells, doesn't contain growth medium or are outside of the glass plate.

An example image series of such growth can be seen below. `X` indicates an empty grid cell, `.` indicates a grid cell with growth medium and `#` indicates a grid cell with a bacteria cell in it.
<pre>
+--------------------------------------------------------+
|      Day 1       |      Day 2       |      Day 3       |
+------------------+------------------+------------------+
|XXXXXXXXXXXXXXXXXX|XXXXXXXXXXXXXXXXXX|XXXXXXXXXXXXXXXXXX|
|XXXXXX......XXXXXX|XXXXXX......XXXXXX|XXXXXX......XXXXXX|
|XXXX..........XXXX|XXXX..........XXXX|XXXX..........XXXX|
|XXX............XXX|XXX............XXX|XXX......#.....XXX|
|XX..............XX|XX.......#......XX|XX......###.....XX|
|XX.......#......XX|XX......###.....XX|XX.....#####....XX|
|X................X|X........#.......X|X.......###.#....X|
|X................X|X...........#....X|X........#.###...X|
|X...........#....X|X..........###...X|X.........#####..X|
|X................X|X...........#....X|X..........###...X|
|X................X|X................X|X...........#....X|
|X................X|X................X|X.....#..........X|
|XX..............XX|XX....#.........XX|XX...###........XX|
|XX....#.........XX|XX...###........XX|XX..#####.......XX|
|XXX............XXX|XXX...#........XXX|XXX..###.......XXX|
|XXXX..........XXXX|XXXX..........XXXX|XXXX..#.......XXXX|
|XXXXXX......XXXXXX|XXXXXX......XXXXXX|XXXXXX......XXXXXX|
|XXXXXXXXXXXXXXXXXX|XXXXXXXXXXXXXXXXXX|XXXXXXXXXXXXXXXXXX|
+--------------------------------------------------------+

</pre>

Instead of wasting time on performing tests she can predict the result for, Lisa has better things to do. Therefore she needs you to make a program that can predict the result of the test, given an image of the glass plate after day 1. To make sure her boss doesn't discover that she's not actually performing the tests, Lisa will vary the size of the glass plates, and the number of days between the initial and the final count.

## Input specification
The first line of input contains three integers _m_, _n_, the number of rows and columns in the glass plate grid, and _t_, the number of days the bacteria should grow before the final count.
Then follows _m_ lines, each containing _n_ characters. These lines make up the grid image of the glass plate. The characters `#`, `.` and `X` represent a grid cell containing a bacteria cell, a grid cell with growth medium and an empty grid cell, respectively.

## Output specification
Output the number of bacteria cells there are on the glass plate after _t_ days of growth, given the initial state in the input.

## Constraints
1 &le; _m_, _n_ &le; 100  
1 &le; _t_ &le; 20

## Sample input 1
```
18 18 2
XXXXXXXXXXXXXXXXXX
XXXXXX......XXXXXX
XXXX..........XXXX
XXX............XXX
XX..............XX
XX.......#......XX
X................X
X................X
X...........#....X
X................X
X................X
X................X
XX..............XX
XX....#.........XX
XXX............XXX
XXXX..........XXXX
XXXXXX......XXXXXX
XXXXXXXXXXXXXXXXXX
```

## Sample output 1
```
39
```

## Sample input 2
```
14 14 2
XXXXXXXXXXXXXX
.........XXXXX
.........XXXXX
.........XXXXX
....#....X...X
.........X.#.X
.........X...X
.........XXXXX
.........XXXXX
....#....XXXXX
....#....XXXXX
.........XXXXX
.........XXXXX
.........XXXXX
```

## Sample output 2
```
40
```
