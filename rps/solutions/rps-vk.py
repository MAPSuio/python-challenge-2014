# @EXPECTED_RESULTS@: CORRECT

"""
Decides what to do in each of the three possible cases. In two of them I have to 
make one choice 1/3 time, and the other 2/3 of the time. See rps-analysis.md
"""
from sys import stdin
import random


def beats(command):
    if command == "Scissors":
        return "Rock"
    if command == "Paper":
        return "Scissors"
    if command == "Rock":
        return "Paper"


def answer(commands):
    if beats(commands[0]) == commands[1]:
        r = random.randint(0,2)
        if r < 1:
            return beats(commands[1])
        else:
            return commands[1]
    elif beats(commands[1]) == commands[0]:
        r = random.randint(0,2)
        if r < 1:
            return beats(beats(commands[1]))
        else:
            return commands[1]
    else:
        return beats(commands[0])


T = int(stdin.readline())
for test_case in range(T):
    for match in range(10000):
        print answer(stdin.readline().split())
