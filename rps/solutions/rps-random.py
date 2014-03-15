# @EXPECTED_RESULTS@: WRONG-ANSWER

from sys import stdin
from random import randint

R = 'Rock'
P = 'Paper'
S = 'Scissors'

first_moves = [R, P, S]
second_moves = {R:[P, S], P:[R, S], S:[R, P]}

T = int(stdin.readline())
N = int(1e4)

for i in xrange(T):
    for j in xrange(N):
        you, friend = stdin.readline().split()
        print second_moves[you][randint(0, 1)]
