# @EXPECTED_RESULTS@: CORRECT

"""
Solution based on VK's solution, (Just calculating the best option for each of the three cases (win, loose and
draw) on the first match by hand.), but correct.
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
random.seed(769786)

def answer(commands):
    q=random.randint(1,3)
    if beats(commands[0]) == commands[1]:
        if (q<3):
            return commands[1]
        else:
            return beats(commands[1])
        
    elif beats(commands[1]) == commands[0]:
        if (q<3):
            return commands[1]
        else: 
            return beats(commands[0])
    else:
        return beats(commands[0])


T = int(stdin.readline())
for test_case in range(T):
    for match in range(10000):
        print answer(stdin.readline().split())
