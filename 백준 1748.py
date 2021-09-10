import sys


def digit(n):
    num = list(str(n))
    return len(num)


N = int(sys.stdin.readline())
result = 0
if N < 10:
    result = N
else:
    result += 9
    for i in range(10, N+1):
        result += digit(i)
print(result)
