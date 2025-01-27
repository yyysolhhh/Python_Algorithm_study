# 시간초과
#def solve(n):
#    for i in range(n // 2 + 1):
#        if i * i == n:
#            return 1
#    return 0

def solve(n):
    if int(n ** 0.5) ** 2 == n:
        return 1
    return 0

N = int(input())
X = list(map(int, input().split()))
ans = map(solve, X)
print(*ans)
