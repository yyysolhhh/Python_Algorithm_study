import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
M = int(input())

# 2
dp = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    dp[i][i] = 1
for i in range(N - 1):
    if nums[i] == nums[i + 1]:
        dp[i][i + 1] = 1
for k in range(2, N):
    for i in range(N - k):
        if nums[i] == nums[i + k] and dp[i + 1][i + k - 1]:
            dp[i][i + k] = 1
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S - 1][E - 1])

# 1 - 시간초과
#for _ in range(M):
#    S, E = map(int, input().split())
#    if nums[S - 1:E] == nums[E - 1:(S - 2 if S > 1 else None):-1]:
#        print(1)
#    else:
#        print(0)
