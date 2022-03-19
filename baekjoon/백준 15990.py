# 앞의 3 경우를 더하는데 같은 수 연속을 피하기 위해 1로 끝난 경우는 2, 3으로 끝난 경우를 더해주는 식으로 2차원 배열을 이용하여 구함
import sys
input = sys.stdin.readline
T = int(input())
mod = 1000000009
dp = [[0] * 4 for _ in range(100001)]
dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]
for i in range(4, 100001):
    for j in range(1, 4):
        dp[i][j] = (dp[i-j][1] + dp[i-j][2] + dp[i-j][3] - dp[i-j][j]) % mod
for _ in range(T):
    n = int(input())
    print(sum(dp[n]) % mod)
