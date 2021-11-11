N, M = map(int, input().split())
castle = []
for _ in range(N):
    castle.append(list(input()))
res = 0
for i in range(N):
    if 'X' not in castle[i]:
        for j in range(M):
            if 'X' not in castle[:][j]:
                castle[i][j] = 'X'
                res += 1
print(res // 2)
