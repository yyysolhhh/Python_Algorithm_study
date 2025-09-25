import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dist = [[sys.maxsize for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    A, B, T = map(int, input().split())
    dist[A][B] = min(dist[A][B], T)
for i in range(N + 1):
    dist[i][i] = 0
K = int(input())
C = list(map(int, input().split()))
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
city = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    for x in C:
        if i == x or dist[i][x] == sys.maxsize or dist[x][i] == sys.maxsize:
            continue
        city[i] = max(city[i], dist[i][x] + dist[x][i])
min_dist = min(city[1:])
ans = []
for i in range(1, N + 1):
    if city[i] == min_dist:
        ans.append(i)
print(*sorted(ans))
