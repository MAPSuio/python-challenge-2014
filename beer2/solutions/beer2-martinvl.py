# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

def is_div(num):
    if int(num[-1]) % 2:
        return False

    e = sum(map(int, num[0::2]))
    o = sum(map(int, num[1::2]))

    if (e + o) % 9:
        return False

    if (e - o) % 11:
        return False

    return True

num = stdin.readline().replace('\n', '')
print 'BEER!' if is_div(num) else 'FIGHT!'
