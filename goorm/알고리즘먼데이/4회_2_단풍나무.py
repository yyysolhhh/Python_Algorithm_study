from collections import deque

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]


def bfs():
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] > 0:
                arr[ny][nx] -= 1


def check():
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                return 0
    return 1


N = int(input())
arr = []
queue = deque()
period = 0
for _ in range(N):
    arr.append(list(map(int, input().split())))
while True:
    if check():
        break
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                queue.append((i, j))
    bfs()
    period += 1
print(period)
