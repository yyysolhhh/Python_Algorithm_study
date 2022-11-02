# 틀림
from collections import deque


def solve():
    survive = 0
    while queue:
        y, x = queue.popleft()
        if y == N or x == N:
            return survive
        for i in range(y - M, y + M + 1):
            for j in range(x - M, x + M + 1):
                if 0 <= i < N and 0 <= j < N and abs(y - i) + abs(x - j) <= M and arr[i][j] == 1:
                    survive += 1
                    arr[y][x] = -1
    return survive


N, M = map(int, input().split())
arr = []
queue = deque()
for _ in range(N):
    arr.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            queue.append((i, j))
print(solve())
