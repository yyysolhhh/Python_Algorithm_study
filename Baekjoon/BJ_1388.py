import sys

input = sys.stdin.readline
N, M = map(int, input().split())
floor = []
ans = 0
for _ in range(N):
    floor.append(list(input()))

for y in range(N):
    for x in range(M):
        if floor[y][x] == '-':
            ny, nx = y, x
            while nx < M and floor[ny][nx] == '-':
                floor[ny][nx] = 1
                nx += 1
            ans += 1
        elif floor[y][x] == '|':
            ny, nx = y, x
            while ny < N and floor[ny][nx] == '|':
                floor[ny][nx] = 1
                ny += 1
            ans += 1
print(ans)
