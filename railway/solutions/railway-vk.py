# @EXPECTED_RESULTS@: TIMELIMIT

import sys

n = int(sys.stdin.readline())

segments = [1]*n


def has_bad_segment(a, b):
    for i in range(b-a+1):
        if segments[a+i] == 0:
            return True
    return False


def answer(line):
    segment_string, request = line.strip().split()
    segment = int(segment_string)
    if request == "blocked":
        segments[segment] = 0
    elif request == "opened":
        segments[segment] = 1
    else:
        if segments[segment] == 0:
            return "no service"
        else:
            if not has_bad_segment(0, segment):
                return "good service"
            if not has_bad_segment(segment, n-1):
                return "good service"
            return "no service"


for line in sys.stdin:
    ans = answer(line.strip())
    if ans:
        print ans
