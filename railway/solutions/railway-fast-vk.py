# @EXPECTED_RESULTS@: TIMELIMIT

"""
Always keeping track of index of the lowest and highest broken segment.
This makes status fast
"""
import sys

n = int(sys.stdin.readline())
current_min = None
current_max = None
bad_segments = []


def answer(line):
    global current_min
    global current_max
    segment_string, request = line.strip().split()
    segment = int(segment_string)

    if request == "blocked":
        bad_segments.append(segment)
        if current_min is None and current_max is None:
            current_min = segment
            current_max = segment
        else:
            current_min = min([segment, current_min])
            current_max = max([segment, current_max])

    elif request == "opened":
        bad_segments.remove(segment)
        if segment == current_min:
            current_min = min(bad_segments)
        if segment == current_max:
            current_max = max(bad_segments)

    else:
        if current_min is None and current_max is None:
            return "good service"
        if segment <= current_max and segment >= current_min:
            return "no service"
        return "good service"


for line in sys.stdin:
    ans = answer(line.strip())
    if ans:
        print ans
