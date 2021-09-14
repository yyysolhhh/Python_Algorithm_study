import sys
input = sys.stdin.readline
N = int(input())
T, P = [], []
dp = [0 for i in range(N+1)]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
for i in range(N-1, -1, -1):
    if T[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i] + dp[i+T[i]])
print(dp[0])

# 실패
# case1 = 0
# case2 = 0
# for i in range(N-1, -1, -1):
#     if T[i] > N - i:
#         continue
#     else:
#         current = max(case1, P[i] + )
#         case2 = case1
#         case1 = current
# print(max(case1, case2))
