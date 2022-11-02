# 덜품
from collections import deque

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]


def flow_water():
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1:
                queue.append((ny, nx))
                arr[ny][nx] = 0


def cnt_island(i, j):
    queue2 = deque()
    queue2.append((i, j))
    visited = [[0] * M for _ in range(N)]
    while queue2:
        y, x = queue2.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1 and visited[ny][nx] == 0:
                queue2.append((ny, nx))
                visited[ny][nx] = 1


N, M = map(int, input().split())
arr = []
queue = deque()
time = 0
num = 0
for _ in range(N):
    arr.append(list(map(int, input().split())))
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            queue.append((i, j))
while True:
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt_island(i, j)
                num += 1
    if num >= 2:
        print(time)
        break
    flow_water()
    time += 1
