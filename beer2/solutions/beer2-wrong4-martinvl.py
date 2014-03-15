# @EXPECTED_RESULTS@: WRONG-ANSWER

from sys import stdin

def is_div(num):
    e = sum(map(int, num[0::2]))
    o = sum(map(int, num[1::2]))

    if sum(map(int, num)) % 198:
        return False

    return True

num = stdin.readline().replace('\n', '')
print 'BEER!' if is_div(num) else 'FIGHT!'
