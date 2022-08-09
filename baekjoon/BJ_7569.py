from collections import deque
import sys

dx, dy, dh = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]


def bfs():
    while queue:
        h, y, x = queue.popleft()
        print(h, y, x)
        if h == H - 1 and y == Y - 1 and x == X - 1:
            return box[h][y][x]
        for i in range(6):
            ny = y + dy[i]
            nx = x + dx[i]
            nh = h + dh[i]
            if 0 <= ny < N and 0 <= nx < M and 0 <= nh < H and box[nh][ny][nx] == 0 and box[nh][ny][nx] != -1:
                box[nh][ny][nx] = box[h][y][x] + 1
                queue.append((h, y, x))
    return (-1)


input = sys.stdin.readline
M, N, H = map(int, input().split())
box = [[] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        box[i].append(list(map(int, input().split())))
print(box)
queue = deque()
for h, H in enumerate(box):
    for y, Y in enumerate(H):
        for x, X in enumerate(Y):
            if X == 1:
                queue.append((h, y, x))
print(bfs())
