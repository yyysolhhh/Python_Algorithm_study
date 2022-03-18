import sys


def solve(a):
    sum = 0
    for i in a:
        sum += i
    return sum


# a = []
a = list(map(int, sys.stdin.readline().split()))

print(solve(a))
