from cmath import pi
from collections import deque
import sys

dx, dy = [1, 0], [0, -1]


def bfs():
    queue = deque([(0, 0)])
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for i in range(2):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and picture[ny][nx] != 0:
                if picture[ny][nx] != picture[y][x]:
                    cnt += 1
                queue.append((ny, nx))
                picture[ny][nx] = 0
    return cnt


input = sys.stdin.readline
N = int(input())
picture = []
for _ in range(N):
    picture.append(list(input()))
print(bfs())
