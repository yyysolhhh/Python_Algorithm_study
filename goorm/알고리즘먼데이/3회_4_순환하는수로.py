# 덜 품
from collections import deque


def dfs():
    queue = deque()
    while queue:
        curr = queue.popleft()
        for next in Map[curr]:
            if tank[next] != tank[curr]:
                tank[next] = tank[curr]


N = int(input())
Map = [[] for _ in range(N)]
tank = [0 for _ in range(N)]
for _ in range(N):
    a, b = map(int, input().split())
    Map[a].append(b)
    Map[b].append(a)

dfs()
