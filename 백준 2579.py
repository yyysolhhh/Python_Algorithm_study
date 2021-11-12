n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))
dp = [0 for _ in range(n+1)]

for i in range(2, n+1):
    dp[i] = dp[i-1] + max(stairs[i-1], stairs[i-2])
    print(dp)
print(dp[n])
