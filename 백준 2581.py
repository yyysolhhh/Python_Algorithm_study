import sys
input = sys.stdin.readline


def prime_num(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True


M = int(input())
N = int(input())
result = []
for i in range(M, N+1):
    if prime_num(i):
        result.append(i)
if not result:
    print(-1)
else:
    print(sum(result))
    print(min(result))
