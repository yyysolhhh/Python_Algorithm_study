from collections import deque

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]


def bfs():
    while queue:
        y, x = queue.popleft()
        if y == n and x == n:
            return
        sq[y][x] += 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                sq[ny][nx] += 1


n, k = map(int, input().split())
sq = [[0] * n for i in range(n)]
queue = deque()
res = 0
for _ in range(k):
    a, b = map(int, input().split())
    queue.append((a - 1, b - 1))
bfs()
for i in sq:
    res += sum(i)
print(res)
