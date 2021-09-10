import sys


def digit(n):
    num = list(str(n))
    return len(num)


N = int(sys.stdin.readline())
result = 0
for i in range(1, N+1):
    result += digit(i)
    print(i, result)
print(result)
