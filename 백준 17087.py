import sys
input = sys.stdin.readline

# 동생들과의 거리의 최대공약수 찾기


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


N, S = map(int, input().split())
A = list(map(int, input().split()))
D = list(set(abs(i-S) for i in A))
ans = []
for i in range(len(D)-1):
    for j in range(i+1, len(D)):
        ans.append(gcd(D[i], D[j]))
print(min(ans))
