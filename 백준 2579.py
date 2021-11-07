n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))
dp = [0 for _ in range(n+1)]
dp[1] = stairs[n-1]
print(stairs)
for i in range(2, n+1):
    dp[i] = max(stairs[n-i] + dp[i-1], stairs[n-i] + dp[i-2])
    print(dp)
print(dp[n])
